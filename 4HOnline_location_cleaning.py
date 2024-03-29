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

#populate columns with split address values
for split_index, split_list in enumerate(split_addresses):
    if hasNumbers(split_list[0]) == True:
        df.loc[split_addresses_index[split_index],'Program Address']= split_addresses[split_index][0]
        df.loc[split_addresses_index[split_index],'Program City']= split_addresses[split_index][1]
    else:
        df.loc[split_addresses_index[split_index],'Program Address']= split_addresses[split_index][1]
        if len(split_addresses[split_index]) > 2: 
            df.loc[split_addresses_index[split_index],'Program City']= split_addresses[split_index][2]
          
#put location names put into Program Address into Program Name
for index, location in enumerate(df["Program Address"]):
    if hasHashtag(location)==True: 
        if df["Program Address"][index] not in roads:
            df.loc[index,'Program Name'] = location
            df.loc[index,'Program Address'] = "None"
            
