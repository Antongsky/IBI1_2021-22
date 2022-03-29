import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#basic file manipulations
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")

#overall look
print(covid_data.head(5))
print(covid_data.info())
print(covid_data.describe())

#get familiar with the iloc method
print(covid_data.iloc[0,1])
print(covid_data.iloc[0:5,0:6])
print(covid_data.iloc[0:10:2,0:5])
#show the first and third columns from rows 10-20
print(covid_data.iloc[10:21,0:4:2])
#or
print(covid_data.iloc[10:21,[0,2]])
#use booleans
my_columes=[True,True,True,False,False,True]
print(covid_data.iloc[1,my_columes])

#Try to use loc method
print(covid_data.loc[0:81,'new_cases'])


#Try to print all the Afghanistan new cases
Afghanistan=[]
covid_data_location=covid_data.loc[:,'location'] #Extract location column
for i in covid_data_location:    #If the value is"Afghanistan", then assign True.
    boolean= i=='Afghanistan'
    Afghanistan+=[boolean]
print(Afghanistan)
print(covid_data.loc[Afghanistan,'new_cases'])

#data in China
new_case_china=covid_data.loc[1454:1546,'new_cases']
new_death_china=covid_data.loc[1454:1546,'new_deaths']
china_date=covid_data.loc[1454:1546,'date']
print(np.mean(new_case_china))  #mean of new cases in China
print(np.mean(new_death_china)) #mean of new deaths in China
print(np.mean(new_death_china)/np.mean(new_case_china)) #The death rate
plt.boxplot(new_case_china)#make the boxplot
plt.xlabel("China new cases boxplot") 
plt.show()
plt.clf()
plt.boxplot(new_death_china)
plt.xlabel("China new deaths boxplot")  
plt.show()
plt.clf()
plt.plot(china_date,new_case_china,'b+')
plt.xlabel("China new cases against time plot")
plt.show()
plt.clf()
plt.plot(china_date,new_death_china,'ro')
plt.xlabel("China new deathes against time plot")
plt.show()

#Asking questions
new_case_spain=covid_data.loc[6720:6812,'new_cases']
total_case_spain=covid_data.loc[6720:6812,'total_cases']
spain_date=covid_data.loc[6720:6812,'date']
plt.plot(spain_date,new_case_spain,'b+')
plt.plot(spain_date,total_case_spain,'r+')
plt.xlabel("Spain new cases and deathes against time plot")
plt.show()



    

