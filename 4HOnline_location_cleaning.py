#location cleaning
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/Lucy/Desktop/ProgramEnrollments.csv")
#change 'nan' to string "None"
df=df.where((pd.notnull(df)), "None") 

#functions
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def containsCommas(inputString):
    return any(char=="," for char in inputString)
def hasHashtags(inputString):
    return any(char=="#" for char in inputString)

#psuedo dictionary
dict={'Adams': ['Camp Point','Mendon','Quincy', 'Hull'], 'Bond': ['Greenville', 'Kinmundy', 'Champaign', 'Sorento']}
road=pd.read_csv("/Users/Lucy/Desktop/RoadTypes.csv")
roads=road.to_dict()

#sort 'Program: Location' into PEARS attributes
for index, location in enumerate(df['Program: Location']):
    if hasNumbers(location)==True:
        df.loc[index,'Program Address'] = location
        #print(df['Program Address'][index]==location)
    if hasNumbers(location)==False:
        if df['Group Enrollment Form: County'][index] in dict:
            if df['Program: Location'][index] in dict.get(df["Group Enrollment Form: County"][index]):
                df.loc[index,'Program City'] = location
            else:
                df.loc[index,'Program Name'] = location

#clean 'Program Address' for consistency
#splits location in "address", "city" and "name" (not in that order)
split_addresses=[]
split_addresses_index=[]
for index, address in enumerate(df['Program Address']):
    if containsCommas(address) == True:
        split_addresses_index.append(index)
        split_addresses.append(address.split(','))

#
for i, x in enumerate(a):
    if hasNumbers(x[0]) == True:
        df.loc[b[i],'Program Address']= a[i][0]
        df.loc[b[i],'Program City']= a[i][1]
    else:
        df.loc[b[i],'Program Address']= a[i][1]
        if len(a[i]) > 2: 
            df.loc[b[i],'Program City']= a[i][2]
