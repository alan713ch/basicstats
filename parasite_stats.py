#Author: Alan Izar
#08/01/16

#Goal: to do basic statistics following http://www.randalolson.com/2012/08/06/statistical-analysis-made-easy-in-python/

#we'll need pandas and scipy

import pandas as pd
from scipy import stats
import numpy as np

#loading up the data frame

path = r'C:\Users\izara\PycharmProjects\parasite_data_stats\SRC\CSV data\parasite_data.csv' #indicating the path
experimentDF = pd.read_csv(path, na_values=[" "])                                           #loading the data

#print (experimentDF)                                                                        #checking data is loaded

#show all entries in the virulence column
#print (experimentDF['Virulence'])

#show the 12th row in the ShannonDiversity column
#print (experimentDF['ShannonDiversity'][12])

#show all entries in the ShannonDiversity column higher than 2.0
#print (experimentDF[experimentDF['ShannonDiversity']>2.0])                                  #print experimentDF such that experimentDF['ShannonDiversity']>2.0 is true

#blank and ommitted data
#print (experimentDF[np.isnan(experimentDF["Virulence"])])                                   #isnan extracts the values with NaN

#mean
#print ('Mean virulence across all treatments ', experimentDF['Virulence'].mean())

#you can dropnan and fillnan, they are different

#print ('Mean virulence with dropnan ', experimentDF['Virulence'].dropna().mean())
#print ('Mean virulence with fillnan ', experimentDF['Virulence'].fillna(0.0).mean())        #fillna needs a number to fill it with!

#mean of a data set
#print ('Mean Shannon Diversity w/ 0.8 Parasitic Virulence', experimentDF[experimentDF['Virulence']== 0.8]['ShannonDiversity'].mean())

#variance!
#print ('Mean Shannon Diversity w/ 0.8 Parasitic Virulence', experimentDF[experimentDF['Virulence']== 0.8]['ShannonDiversity'].var())

#standard error of the mean - not in pandas?
#standermean = stats.sem(experimentDF[experimentDF["Virulence"]==0.8]['ShannonDiversity'])
#print('SEM of Shannon Diversity w/ 0.8 Virulence', standermean)

#MWW Ranksum test
#two treatments

treatment1 = experimentDF[experimentDF["Virulence"]==0.5]['ShannonDiversity']
treatment2 = experimentDF[experimentDF["Virulence"]==0.8]['ShannonDiversity']

#print ('Data Set 1:\n', treatment1)
#print ('Data Set 2:\n', treatment2)

z_stat, p_val = stats.ranksums(treatment1, treatment2)

print ('MWW RankSum P for treatments 1 and 2 =', p_val)

