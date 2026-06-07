import pandas as pd

df=pd.read_csv("titanic.csv")

print(df.head())
print(df.tail())

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())
print(df[["Name","Age"]])

#spesefic row
print(df.iloc[0:5])

#counting things
print(df["Sex"].value_counts())
print(df["Survived"].value_counts())

#filter data
print(df[df["Sex"]=="female"])
print(df[df["Survived"]==1])
print(len(df[df["Age"]<=18]))

#finding avg 
print(df["Age"].mean())

#sorting values
print(df.sort_values("Age",ascending=False))
print(df.sort_values("Fare",ascending=False))

#missing data
print(df.isnull().sum())

#fill missing age
df["Age"]=df["Age"].fillna(df["Age"].mean())

#grouping data, survival by gender
print(df.groupby("Sex")["Survived"].mean())

#avg age by gender
print(df.groupby("Sex")["Age"].mean())

#creating new columns
df["Age group"]="adult"
df["Age group"]=df["Age"].apply(lambda age:"child" if age<18 else "adult")
print(df["Age group"].value_counts())

print(df[(df["Age group"]=="child") & (df["Survived"]==1)])