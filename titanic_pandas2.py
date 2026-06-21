import pandas as pd

df=pd.read_csv("titanic.csv")

#age analysis
print(len(df[df["Age"]>60]))

print(len(df[(df["Age"]<12) & (df["Survived"]==1)]))

print(df.groupby("Pclass")["Age"].mean())

#gender and class analysis

print(len(df[(df["Sex"]=="female") & (df["Pclass"]==1)]))

print(len(df[(df["Sex"]=="male") & (df["Pclass"]==3) & (df["Survived"]==1)]))

print(df.groupby("Pclass")["Fare"].mean())

#highest fare amongst survivors
#method one
print(df[df["Survived"]==1]["Fare"].max())
#method two
print(df.loc[df["Survived"]==1,"Fare"].max())
#method three
print(df.groupby("Survived")["Fare"].max()[1])

"""def farecatagory(fare):
    if fare < 20:
        return "low"
    elif fare <= 50:
        return "medium"
    else:
        return "high"
    
df["farecatagory"]=df["Fare"].apply(farecatagory)

print(df)"""

df["farecatagory"]=df["Fare"].apply(lambda x:"low" if x<20 else "medium" if x<=50 else "high")
print(df)

print(df["farecatagory"].value_counts())

#replaceing passenger names
df.loc[0:4,"Name"]="Test passenger"
print(df.head())

df.loc[10:15,"Fare"]=999
print(df.loc[10:15,["Fare"]])

#creating a new fare per person
df["fareppers"]=df["Fare"]/(df["Siblings/Spouses Aboard"] + 1)
print(df["fareppers"])

#grouping and agregation
print(df.groupby("Sex")[["Fare","Age"]].mean())

print(df.groupby(["Sex","Pclass"])["Fare"].mean())

print(df[df["Survived"]==1].groupby("Pclass")["Survived"].count())

print(df.groupby(["Pclass","Sex"])["Age"].max())

#sorting and text operations

sorterdf=df.sort_values(by=["Pclass","Fare"],ascending=[True,False])
print(sorterdf.head(20))

df["namelower"]=df["Name"].str.lower()
print(df.head())

df["surname"]=df["Name"].str.split(" ").str[-1]
print(df)

df["gender"]=df["Sex"].apply(lambda x:"m" if x=="male" else "f")
print(df)

print(df["surname"].nunique())