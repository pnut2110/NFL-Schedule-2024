import pandas as pd

# Read the .xlsx file
df = pd.read_excel('G:\\Python\\Logo and weekly opponents\\NFL Schedule.xlsx', header=None)

print(df.columns)