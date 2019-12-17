# projects

-- A variety of projects completed for the G.T. class CSE 6242, Data and Visual Analytics 

1) Lego Rebrickable Data Manipulation and Visualization 
  -Q1:
    1 - bricks_graph.gefx - an undirected graph of related lego sets. Data mined from rebrickable API. Requires gephi 0.9.2 to view
    2 - graph.png - image of graph in its entirety
    3 - script.py - python script used to make API calls and synthesize data to readable format for gephi
  -Q2:
    1 - Q2.sql - simple sqllite script that manipulates rebrickable data for certain criteria and summary statistics
  -Q3:
    1 - lib - src files
    2 - index.html - D3 barchart showing counts of lego set by year
    3 - q3.csv - CSV output from SQL manipulation
  -Q4: 
    1 - Q4Observations.txt - changes made using GREL to clean lego dataset
    2 - changes.json - stored object of changes made
    3 - properties_clean.csv - cleaned csv
    
2) Data vis with Tableau and D3
  -Q1:
    1 - age-distribution.csv - raw data on country demographics by year
    2 - barchart.png - stacked barchart made with Tableau
    3 - population.csv - data organized by age and demographics
    4 - table.png - latex table on age distributions
  -Q2: 
    1 - lib -src files
    2 - graph.html - force directed graph made in D3
  -Q3: 
    1 - earthquakes.csv - data on earthquakes by state
    2 - explanation.txt - not used
    3 - linecharts.html - source html for d3 graph of earthquake data
    4 - linecharts.pdf - picture of above linecharts
  -Q4:
    1 - earthquakes.csv - data on earthquakes by state
    2 - heatmap.html - d3 heatmap on US states by eathquake frequency
  -Q5:
    1 - state-year-earthquakes.csv - similar to earthquakes.csv, but with additional information by year
    2 - interactive.html - d3 visualization with interactive barchart element on hover
  -Q6:
    1 - choropleth.html - d3 choropleth map with interactive tooltip on hover
    2 - state-earthquakes.csv - state data used in choropleth
    3 - states - 10m.json - additional data used in visualization
  -Q7:
    1 - analysis.txt - a comparison of visual tools used in this subset of problems (D3, R, and Tableau)
    
3) Big Data Manipulation
  -Q1:
    1 - src - src files
    2 - pom.xml - compiler
    3 - q1.output1.tsv - tab sep data compiled by running hadoop method
    4 - q1.output2.tsv - ouput from running second hadoop method
    5 - run1.sh - first hadoop instance
    6 - run2.sh - second hadoop instance
  -Q2:
    1 - q2.dbc - database connection
    2 - q2.scala - script for manipulating data using spark/scala
    3 - q2_results.csv - output from above
  -Q3:
    1 - pig-output.txt - output from pig script on large dataset
    2 - pit-script.txt - pig script
  -Q4:
    1 - src - src files
    2 - large.out - output from larger of two datasets (a few GB)
    3 - pom.xml - compiler
    4 - q4-1.0.jar - jar file used on the two datasets (run using AWS cluster)
    5 - small.out - output from smaller data set
  -Q5:
    1 - results.csv - output from using Microsoft Azure's machine learning labratory
    
4) Statistical Algorithms 
  Q1:
    1 - pagerank.py - python script for implementation of simple pagerank algorithm 
    2 - 5: outputs from running script on different seeds with differing numbers of outputs
  Q2: 
    1 - decision_tree.py - script initializing class decision tree
    2 - forest.txt - a quick overview of the success of my implementation
    3 - random_forest.py - manual implementation of a random forest algorithim
    4 - util.py - functions used in decision_tree.py
  Q3:
    1 - hw4q3.ipynb - jupyter notebook using scikit learn to fit and manipulate several different types of models 
