#location cleaning
import pandas as pd
url = 'https://github.com/lrchang2/4H_location/blob/master/ProgramEnrollments.csv'
df = pd.read_csv(url)

print(df)
