import pandas as pd

data = {
    "Name": ["Adnan","zaid","Aliya"],
    "Age" : [10,20,30],
    "City" : ["nagput","mumbai","delhi"]
}

df = pd.DataFrame(data)

print(df)

# df.to_csv("output.csv",index=False)

df.to_excel("output.xlsx", index= False)