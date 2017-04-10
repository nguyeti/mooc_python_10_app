import os, pandas as pd

df = pd.read_csv("./data/supermarkets.csv")
print(df.where(df.State == "California"))
