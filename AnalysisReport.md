# DSSG_assignment

This report contains the results obtained through the EDAs of the dataset given in 
[KDD Cup 2014](https://www.kaggle.com/c/kdd-cup-2014-predicting-excitement-at-donors-choose/) competition hosted on 
Kaggle.

Different IPython notebooks were made for looking at their respective datasets.
1. [EDA_projects.ipynb](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_projects.ipynb) - projects.csv
2. [EDA_donations.ipynb](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_donations.ipynb) - donations.csv
3. [EDA_resources.ipynb](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_resources.ipynb) - resources.csv

A Jupyter notebook that looked at the merged dataset was also created

[EDA_Proj_Don_Res.ipynb](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_Proj_Don_Res.ipynb) - Merged data
 of projects, donations and resources

A notebook for Geospatial analysis is also available for perusal. 

[EDA_GeoStudies.ipynb](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_GeoStudies.ipynb) - Uses Latitude
 and Longitude data on the US map

NOTE : There seems to be a rendering issue with the map elements in Jupyter notebook with the latest version of folium. 
To view the maps, they are stored locally into the system running the notebook,and are opened in a separate 
webbrowser instead. 
Screenshots of the maps will be given with the report.

### Contents : 
1. [Database and ETL Summary](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#database-and-etl-summary)
2. [Analysis](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#analysis)
3. [Projects Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#projects-data)
4. [Donations Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#donations-data)
5. [Resources Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#resources-data)
6. [Combined Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#combined-data)
7. [Questions for the Project Partner](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#questions-for-the-project-partner
)
8. [Packages required](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/AnalysisReport.md#packages-required)

### Database and ETL summary

Before the data was analysed,it went through an ETL routine given in Utils/ETL.py

The data was stored in a MySQL Schema "kdd_2014" with the following tables - 
1. projects - projects.csv
2. donations - donations.csv
3. resources - resources.csv

The date element in <b>projects</b> and <b>donations</b> was expanded to have additional columns.

Jupyter notebooks pulled only required columns from the MySQL database for analysis.

Database was hosted on the local machine. 

## Analysis 

###### Note: 
The Geo maps can be viewed 
[here](https://github.com/Srihari231092/DSaPP_RA_Project/tree/master/res).
To open them without downloading, please use https://nbviewer.jupyter.org/


### [Projects Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_projects.ipynb)
In the dataset, we do not have 12 months of data for the years 2002 and 2014. A decision was made to ignore these 2 
years in order to not represent false aggregated readings over time.

Let's take a look at the kind of resources requested by projects, when joined with the _poverty_ level of the schools
 and the _focus area_
 
![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/projects/Resource%20requests.PNG)

*Math and Science* focused projects seem to require more _supplies_ and _technology_ 

*Literacy and Language*, while not far behind, dominates requests on _books_ than the other disciplines  

Over the years however, literature focused projects are going strong, with science at second place.

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/projects/focusarea_years.PNG)


The number of projects proposals has been steadily increasing over the years.
Most project proposals are submitted on August, with the least being in June. This tallies with traiditional school 
timings.

A closer look reveals that this could be a strong trend over the years 2003 to 2013 except the 
years 2008 and 2011 (possibly due to extraneous reasons)

NOTE: in the graph "Number of projects over months in each year", the green dots are most number of proposals in 
that year, while the red dots are least number of proposals for that year.

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/projects/numproposals_time.PNG)


When we take a more geospatial look at project distributions, we can easily see hotspots using traditional heatmaps

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/projects/geo_heatmap.PNG)


---
### [Donations Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_donations.ipynb)
The total value of donations is over <b>237 Million USD</b> over all the years in the dataset!

We do not have 12 months of data for the years 2000 and 2014. But for the sake of consistency with projects data, we 
will keep the data from the years 2003-2013.

Over time, similar to projects, the number of donations have been increasing substantially.


![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/donations/numdonations_time.PNG)



Most donations seem to have happened in December. This may be due to influences of the festival season and general 
boradcasted messages focused on charity and sharing wealth.

The standard deviation of the donations received has increased greatly over the years as well, with 2013 having the 
largest spread.

How have payment modes behaved over the years? 

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/donations/payment_time.PNG)


An increased used of Credit cards is noticeable, and intersetingly, Amazon usage as well. *no_cash_received*
seems to be reducing in recent trends. 

Geospatially, where do most donations come from? 

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/donations/geo_donations.PNG)

Hotspots are easily noticeable. It would be interesting to understand why, and what factors make some regions seem 
more altruistic than others. 

---
### [Resources Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_resources.ipynb)

The total value of all the resources provided comes to over <b>747 million USD</b>.

Books seem to be the most donated resource in this dataset.

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/resources/resource_type_donated.PNG)

The top 5 most altrusitic donors are listed below - 

![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/resources/top_vendors.PNG)


---
### [Combined Data](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/EDA_Proj_Don_Res.ipynb)

Once we combine the datasets, we can understand how projects got funded (if at all)
Around 80% of all proposed projects only achieved less than 20% of their target


![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/combined/hist_bin.PNG)


The number of projects focused on SCience and Technology have had an increase in donations over time. 
It is interesting to note that while the amount of donations over time has consistently increased, the number of 
projects funded in later years (2013, 2012) has reduced. 


![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/combined/focusarea.PNG)

If we analyse just the projects that achieved at last 80% of their target over the years, it's interesting to note 
that projects that have reached or cross their 100% target is far more than the ones that end at 80-95% of their 
target. A last mile push would have brought these proposals to the final bin quite quickly.

 
![alt text](https://github.com/Srihari231092/DSaPP_RA_Project/blob/master/images/combined/top80p_time.PNG)


### Questions for the Project Partner

1. Supplies and Technology seem to be quite in demand for Schools high in poverty. Is there any additional information 
that can be provided on these?  

2. What factors can we consider when trying to understand why there are distinct hotspots for project proposals 
geo-spatially? Is there a way to estimate recurrence from certain region or an increase in frequency?   

3. Can information about the relation between the donor and his/her personal stake in the project be collected? It 
would be interesting to see if a donor was an alumni, or an ex-employee from the school.   

4. Can more information be found on *donation_optional_support*? Is it tax-free?

### Packages required
NOTE: This list is dynamic and will update as and when needed

A full package list can be found in packages.txt

Key packages used are - 
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. folium
6. pymysql
7. sqlalchemy

### 


 

