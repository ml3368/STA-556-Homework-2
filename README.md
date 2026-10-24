# STA-556-Homework-2
Public Repository for STA 556 Homework 2

The data for this homework came from the UC Irvine Machine Learning Repository (https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)

Fanaee-T, H. (2013). Bike Sharing [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

The data being used is the Bike Sharing data set that contains data on bike rental counts per day, along with data about the date, the weather (temp, windspeed, humidity), whether it is a holiday or not, and whether it is a workday or not.

The purpose of the project is to determine how the daily temperature and whether the day given is a workday affect bike rental counts.

To run the analysis, put the raw data in the data_raw folder (data/data_raw/day.csv). Then run all the code (in order) in the homework_2.ipynb notebook in python.

The main findings based on the research questions are that temperature and bike rental counts do have a moderately strong, positive, linear relationship with a correlation of approximately 0.63. Work day status (work day vs not work day), however, seems to have little association with bike rental counts with a correlation of approximately 0.06 and mean bike rental counts on work days of 4585 and bike rental counts on non work days of 4330.