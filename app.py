import pandas as pd

#read data from CSV file intp a dataframe

# df = pd.read_csv(r"D:\pandas\Pandas\results.csv", encoding="latin1")

df = pd.read_excel(r"D:\pandas\Pandas\results.xls", engine="xlrd")



print(df)