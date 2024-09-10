import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dictionary for ID, Value and Category
data = {
    'ID' : np.arange(1, 1000001), # 1 Million IDs
    'Value' : np.random.rand(1000000), #1 million random values
    'Category' : np.random.choice(['A', 'B', 'C', 'D'], size = 1000000) #random categories
    }

#setting up a dataframe for data
df=pd.DataFrame(data)

#Showing the first 10
print(df.head(10))

#Creating a new dataframe with just Value
value = pd.DataFrame(data,columns = ['Value'])

print()
#Printing the first 10 rows again
print(value.head(10))

#new dataframe with the specified names
daf=pd.DataFrame(data, columns = ["ID Number", "Random Value", "Choice"],
                index=["1", "2", "3", "4", "5"])
print()

#printing out the first 5 rows
print(daf.head(5))

#Code as given in the assignment
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001', 's002','s004'],
    'class': ['V','V','VI','VI','V','VI'],
    'name':['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002', '16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age':[12,12,13,13,14,12],
    'height':[173,192,186,167,151,159],
    'weight':[35,32,33,30,31,32],
    'address': ['street1','street2','street3','street1','street2','street4']},
    #Had to include index in the dataframe
    index = ['S1','S2','S3','S4','S5','S6'])

#printing out the origininal dataframe
print("Original DataFrame:")
print(student_data)

#splitting it up based on school code and class
print('\nSplit the said data on school_code, class wise:')
result = student_data.groupby(['school_code','class'])
for name,group in result:
    #loop that will print out each group and their members
    print("\nGroup:")
    print(name)
    print(group)


#reading the csv file provided in the assignment
data = pd.read_csv("data.csv")
print("Statistical Description")
#describing the data
print(data.describe())

#checking for null values
print("\nChecking Null Values: ")
print(data.isnull().sum())

#filling in all null vallues with the mean
data.fillna(data.mean(), inplace=True)

#printing out the null values again to show that it was changed
print("\nChecking Null Values Again: ")
print(data.isnull().sum())

#choosing pulse and calories to aggregate
columns = ['Pulse', 'Calories']
aggregation = data[columns].agg(['min', 'max', 'count', 'mean'])
print("\nAggregated data for Pulse and Calories:")
print(aggregation)

#filtering all rows to get only rows that have between 500 and 1000 calories
cal_filter = data[(data['Calories'] >= 500) & (data['Calories'] <= 1000)]
print("\nRows where calories are between 500 and 1000:")
print(cal_filter)

#Another filter but this time it wants more than 500 calories and less than 100 pulse
cal_filter = data[(data['Calories'] > 500) & (data['Pulse'] < 100)]
print("\nRows where calories are above 500 and pulse is below 100:")
print(cal_filter)

#modified dataframe without Maxpulse
df_modified = data.drop(columns=['Maxpulse'])
print("\nModified DataFrame (without 'Maxpulse'):")
print(df_modified)

#removing maxpulse from the main data
data.drop(columns=['Maxpulse'], inplace=True)
print("\nDataFrame after deleting 'Maxpulse':")
print(data)

#Coverting calories to an int type
data['Calories'] = data['Calories'].astype(int)
print("\nData types after converting 'Calories' to int:")
print(data.dtypes)

#creating a scatter plot of duration vs calories
data.plot(kind='scatter', x='Duration', y='Calories', color='blue', title='Scatter plot of Duration vs Calories')
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()
