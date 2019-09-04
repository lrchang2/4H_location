#location cleaning
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/Lucy/Desktop/ProgramEnrollments.csv")
df=df.where((pd.notnull(df)), "None") #change 'nan' to string "None"

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def containsCommas(inputString):
    return any(char=="," for char in inputString)

#psuedo dictionary
dict={'Adams': ['Camp Point','Mendon','Quincy', 'Hull'], 'Bond': ['Greenville', 'Kinmundy', 'Champaign', 'Sorento']}
