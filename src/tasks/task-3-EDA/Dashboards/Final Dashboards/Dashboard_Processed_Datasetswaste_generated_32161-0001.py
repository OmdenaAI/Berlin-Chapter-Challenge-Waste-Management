#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install pygwalker')


# In[11]:


#import sys
#!(sys.executable) -m pip install pygwalker -g


# In[12]:


import pandas as pd
import pygwalker as pyg


# In[15]:


df=pd.read_csv("C:\\Users\\rupas\\Downloads\\Processed_Datasetswaste_generated_32161-0001.csv")
df.head()


# In[17]:


pyg.walk(df,dark='dark')


# Inferences
# 1.The amount of waste generated in the year 2014 was the highest.
# 2.The number of etroi_establishments were higher in the year 2018
# 3.Paper and Cardboard Packing has the highest number of etroi_establishments at 39735.
# 

# In[24]:


vis_spec = r"""{"config":"[{\"visId\":\"gw_tZcr\",\"name\":\"year Vs generated_waste_quantity\",\"encodings\":{\"dimensions\":[{\"dragId\":\"gw_6PoZ\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_4Gmo\",\"fid\":\"GW_6W8NGR74JPZL79YD8TW2IX1DC\",\"name\":\"types_of_waste\",\"basename\":\"types_of_waste\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"measures\":[{\"dragId\":\"gw_teeL\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_MP8T\",\"fid\":\"GW_XH261AU4J9MH4I3XQQL97W5DAYL2R2013ZE1M8TS\",\"name\":\"generated_waste_quantity\",\"basename\":\"generated_waste_quantity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_count_fid\",\"fid\":\"gw_count_fid\",\"name\":\"Row count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\",\"computed\":true,\"expression\":{\"op\":\"one\",\"params\":[],\"as\":\"gw_count_fid\"}}],\"rows\":[{\"dragId\":\"gw_nWVD\",\"fid\":\"GW_XH261AU4J9MH4I3XQQL97W5DAYL2R2013ZE1M8TS\",\"name\":\"generated_waste_quantity\",\"basename\":\"generated_waste_quantity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"columns\":[{\"dragId\":\"gw_2uwM\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"color\":[{\"dragId\":\"gw_CmD-\",\"fid\":\"GW_XH261AU4J9MH4I3XQQL97W5DAYL2R2013ZE1M8TS\",\"name\":\"generated_waste_quantity\",\"basename\":\"generated_waste_quantity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"opacity\":[],\"size\":[],\"shape\":[{\"dragId\":\"gw_OJSg\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"radius\":[],\"theta\":[],\"longitude\":[],\"latitude\":[],\"geoId\":[],\"details\":[],\"filters\":[],\"text\":[]},\"config\":{\"defaultAggregated\":true,\"geoms\":[\"auto\"],\"showTableSummary\":false,\"coordSystem\":\"generic\",\"stack\":\"stack\",\"showActions\":false,\"interactiveScale\":false,\"sorted\":\"none\",\"zeroScale\":true,\"scaleIncludeUnmatchedChoropleth\":false,\"size\":{\"mode\":\"fixed\",\"width\":451,\"height\":246},\"format\":{},\"geoKey\":\"name\",\"resolve\":{\"x\":false,\"y\":false,\"color\":false,\"opacity\":false,\"shape\":false,\"size\":false},\"limit\":-1}},{\"visId\":\"gw_opgv\",\"name\":\"etroi_establishments_number Vs types_of_waste\",\"encodings\":{\"dimensions\":[{\"dragId\":\"gw_Gp1i\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_LcSi\",\"fid\":\"GW_6W8NGR74JPZL79YD8TW2IX1DC\",\"name\":\"types_of_waste\",\"basename\":\"types_of_waste\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"measures\":[{\"dragId\":\"gw_HXTc\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_4Zu9\",\"fid\":\"GW_XH261AU4J9MH4I3XQQL97W5DAYL2R2013ZE1M8TS\",\"name\":\"generated_waste_quantity\",\"basename\":\"generated_waste_quantity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_count_fid\",\"fid\":\"gw_count_fid\",\"name\":\"Row count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\",\"computed\":true,\"expression\":{\"op\":\"one\",\"params\":[],\"as\":\"gw_count_fid\"}}],\"rows\":[{\"dragId\":\"gw_m0sL\",\"fid\":\"GW_6W8NGR74JPZL79YD8TW2IX1DC\",\"name\":\"types_of_waste\",\"basename\":\"types_of_waste\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\",\"sort\":\"descending\"}],\"columns\":[{\"dragId\":\"gw_uXJb\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"color\":[],\"opacity\":[],\"size\":[],\"shape\":[],\"radius\":[],\"theta\":[],\"longitude\":[],\"latitude\":[],\"geoId\":[],\"details\":[],\"filters\":[],\"text\":[]},\"config\":{\"defaultAggregated\":true,\"geoms\":[\"circle\"],\"showTableSummary\":false,\"coordSystem\":\"generic\",\"stack\":\"stack\",\"showActions\":false,\"interactiveScale\":false,\"sorted\":\"none\",\"zeroScale\":true,\"scaleIncludeUnmatchedChoropleth\":false,\"size\":{\"mode\":\"fixed\",\"width\":505,\"height\":520},\"format\":{},\"geoKey\":\"name\",\"resolve\":{\"x\":false,\"y\":false,\"color\":false,\"opacity\":false,\"shape\":false,\"size\":false},\"limit\":-1}},{\"visId\":\"gw_arOM\",\"name\":\"etroi_establishments_number\\t Vs year\",\"encodings\":{\"dimensions\":[{\"dragId\":\"gw_f6av\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_S_Br\",\"fid\":\"GW_6W8NGR74JPZL79YD8TW2IX1DC\",\"name\":\"types_of_waste\",\"basename\":\"types_of_waste\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"measures\":[{\"dragId\":\"gw_OdJO\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_R4I3\",\"fid\":\"GW_XH261AU4J9MH4I3XQQL97W5DAYL2R2013ZE1M8TS\",\"name\":\"generated_waste_quantity\",\"basename\":\"generated_waste_quantity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_count_fid\",\"fid\":\"gw_count_fid\",\"name\":\"Row count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\",\"computed\":true,\"expression\":{\"op\":\"one\",\"params\":[],\"as\":\"gw_count_fid\"}}],\"rows\":[{\"dragId\":\"gw_fHAO\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"columns\":[{\"dragId\":\"gw_-Y7Y\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"color\":[{\"dragId\":\"gw_5z68\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"opacity\":[],\"size\":[],\"shape\":[],\"radius\":[],\"theta\":[],\"longitude\":[],\"latitude\":[],\"geoId\":[],\"details\":[],\"filters\":[],\"text\":[]},\"config\":{\"defaultAggregated\":true,\"geoms\":[\"auto\"],\"showTableSummary\":false,\"coordSystem\":\"generic\",\"stack\":\"stack\",\"showActions\":false,\"interactiveScale\":false,\"sorted\":\"none\",\"zeroScale\":true,\"scaleIncludeUnmatchedChoropleth\":false,\"size\":{\"mode\":\"fixed\",\"width\":478,\"height\":280},\"format\":{},\"geoKey\":\"name\",\"resolve\":{\"x\":false,\"y\":false,\"color\":false,\"opacity\":false,\"shape\":false,\"size\":false},\"limit\":-1,\"useSvg\":true}},{\"visId\":\"gw_h1lP\",\"name\":\"Chart 4\",\"encodings\":{\"dimensions\":[{\"dragId\":\"gw_rUXW\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_qf98\",\"fid\":\"GW_6W8NGR74JPZL79YD8TW2IX1DC\",\"name\":\"types_of_waste\",\"basename\":\"types_of_waste\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"}],\"measures\":[{\"dragId\":\"gw_tB_g\",\"fid\":\"GW_943084LMSK2YLWBT63C7VUGNVJYFLPBU4SKTZMLJJSPIO\",\"name\":\"etroi_establishments_number\",\"basename\":\"etroi_establishments_number\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_2AIM\",\"fid\":\"GW_XH261AU4J9MH4I3XQQL97W5DAYL2R2013ZE1M8TS\",\"name\":\"generated_waste_quantity\",\"basename\":\"generated_waste_quantity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_count_fid\",\"fid\":\"gw_count_fid\",\"name\":\"Row count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\",\"computed\":true,\"expression\":{\"op\":\"one\",\"params\":[],\"as\":\"gw_count_fid\"}}],\"rows\":[],\"columns\":[],\"color\":[],\"opacity\":[],\"size\":[],\"shape\":[],\"radius\":[],\"theta\":[],\"longitude\":[],\"latitude\":[],\"geoId\":[],\"details\":[],\"filters\":[],\"text\":[]},\"config\":{\"defaultAggregated\":false,\"geoms\":[\"auto\"],\"showTableSummary\":false,\"coordSystem\":\"generic\",\"stack\":\"stack\",\"showActions\":false,\"interactiveScale\":false,\"sorted\":\"none\",\"zeroScale\":true,\"scaleIncludeUnmatchedChoropleth\":false,\"size\":{\"mode\":\"fixed\",\"width\":320,\"height\":200},\"format\":{},\"geoKey\":\"name\",\"resolve\":{\"x\":false,\"y\":false,\"color\":false,\"opacity\":false,\"shape\":false,\"size\":false},\"limit\":-1,\"useSvg\":false}}]","chart_map":{},"version":"0.3.7"}"""
pyg.walk(df, spec=vis_spec, dark='dark')


# In[ ]:




