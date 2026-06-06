import pandas as pd

dataset={"cars":["bmw","volvo","ferrari"],
         "prouduction":[10,30,18]}

df=pd.DataFrame(dataset,index=["day1","day2","day3"])

print(df)

#series

num=[2,1,3,4,2,5]

disp=pd.Series(num,index=["a","b","c","d","e","f"])
print(disp)

disp1=pd.Series(dataset)
print(disp1)

#locate row
print(df.loc["day1"])
print(df.loc[["day1","day2"]])

print(pd.options.display.max_rows)

#remove rows with empty cells
empty=df.dropna(inplace=True)

#replace empty cells
df.fillna(100,inplace=True)
#creating a new dataframe column
df["sales"]=[30,12,42]
df.insert(loc=3,column="profit",value=[10,35,27])
print(df)
print(df["cars"])

print(df["sales"].max())
print(type(df["sales"]))
print(df["sales"].shape)

print(df.info())
print(df.describe())