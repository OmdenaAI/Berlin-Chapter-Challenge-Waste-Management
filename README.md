# Berlin-Chapter-Challenge-Waste-Management
Use this Repository as a template for creating Local Chapter Repositories

The local problem we are trying to solve is the suboptimal waste management practices and the lack of data-driven decision-making in our community. We aim to tackle issues such as inefficient waste treatment, limited recycling rates, and environmental impact caused by improper waste disposal. By harnessing the potential of data science, we can identify opportunities for improvement, optimize waste treatment methods, and ultimately enhance the sustainability of our local waste management system.

## problem statements
### 1. Optimize waste composition analysis:
 Develop data-driven models to categorize waste types and identify dominant categories, enabling targeted recycling and reduction strategies.
### 2. Forecast future waste generation: 
Develop predictive models using time series analysis or machine learning algorithms to forecast future waste generation trends, aiding in capacity planning and resource allocation.
### 3. Geospatial Analysis: 
Use geographic data to create maps that display waste collection points, disposal sites, and processing facilities. This can help in route optimization and site selection.

![Alt text](%E2%80%8Eproject_architecure.%E2%80%8E001.jpeg)

## Contribution Guidelines
- Have a Look at the [project structure](#project-structure) and [folder overview](#folder-overview) below to understand where to store/upload your contribution
- If you're creating a task, Go to the task folder and create a new folder with the below naming convention and add a README.md with task details and goals to help other contributors understand
    - Task Folder Naming Convention : _task-n-taskname.(n is the task number)_  ex: task-1-data-analysis, task-2-model-deployment etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relavant location and update the README.md information table with your contribution details.
- Make sure your File names(jupyter notebooks, python files, data sheet file names etc) has proper naming to help others in easily identifing them.
- Please restrict yourself from creating unnessesary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion. 

## Project Structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers/collaborators using this project.
    ├── original           <- Original Source Code of the challenge hosted by omdena. Can be used as a reference code for the current project goal.
    │ 
    │
    ├── reports            <- Folder containing the final reports/results of this project
    │   └── README.md      <- Details about final reports and analysis
    │ 
    │   
    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        ├── visualizations <- Code and Visualization dashboards generated for the project
        │
        └── results        <- Folder to store Final analysis and modelling results and code.
--------

## Folder Overview

- Original          - Folder Containing old/completed Omdena challenge code.
- Reports           - Folder to store all Final Reports of this project
- Data              - Folder to Store all the data collected and used for this project 
- Docs              - Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referneced code/research papers and other useful documents used for this project
- Tasks             - Master folder for all tasks
  - All Task Folder names should follow specific naming convention
  - All Task folder names should be in chronologial order (from 1 to n)
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information
  - Update the [task-table](./src/tasks/README.md#task-table) whenever a task is created and explain the purpose and goals of the task to others.
- Visualization     - Folder to store dashboards, analysis and visualization reports
- Results           - Folder to store final analysis modelling results for the project.



## Resources used
The waste management data is collected from the following resources:
- [Genesis website:](https://www-genesis.destatis.de/genesis//online?operation=table&code=32121-0003&bypass=true&levelindex=0&levelid=1692960011357#abreadcrumb) 
    - collection of waste disposal
    - survey of public waste disposal
    - survey of returned sales packaging
    - collection from Transport and outer packaging
- [population data:](https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-laender.html)
- [Geospatial data:](http://overpass-turbo.eu)