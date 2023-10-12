import pygwalker as pyg
import pandas as pd
# pip install sumy
from gensim import corpora, models
import gensim
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

df = pd.read_csv("waste_generated_32161-0001.csv", encoding='ISO-8859-1')

df.dropna(inplace = True)


# 1.Year:  This column represents the year to which the data in the row pertains.
#     
# 2.Data_belong_to:  This column specifies the geographical or organizational scope to which the data belongs.
#     
# 3.Types_of_waste:  This column provides a description of the type of waste associated with each EAV code. It explains the nature or content of the waste category in more detail.
# 
# 4.Etroi_establishments_number:  This column indicates the number of establishments or entities that generate the specified type of waste. It represents how many different places or businesses contribute to the waste stream for that particular category.
# 
# 5.Generated_waste_quantity:  This column quantifies the amount of waste generated for each waste category. It typically represents the quantity of waste in some unit of measurement (e.g., tons, kilograms, cubic meters) that was generated in the specified year and location.
# 
# In summary, the dataset provides information about waste generation in Germany, with details on the waste categories (identified by EAV codes), the number of establishments generating each type of waste, and the quantities of waste generated for each category. This data can be used for various purposes, such as environmental analysis, waste management planning, or policy development.

# Tokenize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['types_of_waste'].values)

# Create a gensim corpus
corpus = gensim.matutils.Sparse2Corpus(X, documents_columns=False)

# Create a dictionary
id2word = dict((v, k) for k, v in vectorizer.vocabulary_.items())

# Fit an LDA model
lda = models.LdaModel(corpus, num_topics=30, id2word=id2word, passes=15)

# Assign topic labels to the original data
df['Topic_Label'] = [max(lda.get_document_topics(item), key=lambda x: x[1])[0] for item in corpus]

df['Topic_Label'].unique()

num_topics = 30
for topic_id in range(num_topics):
    sample_waste_types = df[df['Topic_Label'] == topic_id]['types_of_waste'].sample(5)  # Print 5 random samples
    print(f"Topic {topic_id}:")
    for waste_type in sample_waste_types:
        print(waste_type)
    print("\n")

# Initialize the LexRank summarizer
summarizer = LexRankSummarizer()

category_names = {}

# Iterate over each unique topic label
for topic_id in df['Topic_Label'].unique():
    # Get all waste types for the current topic
    topic_text = ' '.join(df[df['Topic_Label'] == topic_id]['types_of_waste'])
    
    # Create a plaintext parser
    parser = PlaintextParser.from_string(topic_text, Tokenizer("english"))
    
    # Summarize the text to generate a category name
    summary = summarizer(parser.document, sentences_count=1)  
    
    # Store the generated category name in the dictionary
    category_names[topic_id] = str(summary[0])


df['Category_Name'] = df['Topic_Label'].map(category_names)

walker4 = pyg.walk(
    df,
    spec="./gw0.json",       
    use_kernel_calc=True,    
    use_preview=True,         
)

data = df.loc[:, ['year', 'Topic_Label', 'generated_waste_quantity']]

df1 = pd.DataFrame(df)
topic_label_totals = df.groupby('Category_Name')['generated_waste_quantity'].sum().reset_index()

