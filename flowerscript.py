#calculate mean mode and document steps in python for iris data set
#just looked on seaborn docu and iris comes preloaded as a data set so much easier to plot visuals - tbc
#this excellent article on working with data in panda and selecting columns/index https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
import pandas as pd 
import numpy as np
# reference for read csv https://www.datacamp.com/community/tutorials/pandas-read-csv
df1 = pd.read_csv(r"C:\Users\Owner\Desktop\irisdataset/iristest.csv") #importsdatafromfolder r gets rid of the strange error by converting it into a readable string 
#data.columns "sepallength","sepalwidth","petallength","petalwidth","species"]
#print(df1["sepallength"].mean()) #prints the mean value of sepalength column UNCOMMENT THIS
#overall stats describe 
print(df1.describe()) # THIS SHOWS ALL OF THE KEY STATS SURROUNDING DATA  
#print(df1.head(5)) first 5 rows.


#import pandas as pd
#import numpy as numpy
#df = pd.read_csv(r"C:\Users\Owner\Desktop\IRISTOO\iristest.csv")
#print(df.head(5)) finding the path was a nightmare - kept on throwing file not found because I wrote the wrong thing like a numpty



#https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
#data = pd.read_csv("\Desktop\iristest.csv")
     #adapted from shawnlynn https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
#print(data.head())

#import pandas as pd
#ocation = ("\irisdataset\iristest.csv")

#df = pd.read_csv("/Users/Desktop/irisdataset/iristest.csv")
#df = pd.read_csv(

