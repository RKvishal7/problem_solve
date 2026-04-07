import pandas as pd
from jupyter_core.migrate import regex
from sympy import false
from sympy.codegen.ast import continue_, none
from torchgen.packaged.autograd.gen_python_functions import method_impl

# create a dataFrame with name, age, marks
'''data = {
    "name" :(input("student names : ").split(",")),
    "age" :(map(int,input("student age : ").split(","))),
    "mark" :(map(int,input("student marke : ").split(",")))
}
df = pd.DataFrame(data)

print("old data-> "," \n ",df,sep="")'''

#Create Series from list
'''lst = [19,3,4,69]
s = pd.Series(lst)#if you want change the index join the (, index = [your choice num or alpha]) after lst 
print(s)'''

# Convert dictionary to DataFrame == same like creating data frame
'''dictnary = {
    "name" :["vishal"],
    "age" :[19],
    "mark" :[3],
}
data = pd.DataFrame(dictnary)
print(data)'''

# display first and last rows
'''print(df.head(5))
print(df.tail(3))'''

# select column
'''print(df["age"])
print(df[["mark","age"]])'''

# select rows using iloc
'''print(df.iloc[0])#first
print(df.iloc[1])#second'''

#Select last row
'''print(df.iloc[-1])'''

#row slicing == ye iloc se hi hota hai df.iloc(start:end)
'''print(df.iloc[0:3])'''

# column slicing
'''print(df.iloc[:,0:2])'''

# shape finding
'''print(df.shape)'''

# get column name
'''print(df.columns)
print(df.rows)'''

#get data type
'''print(df["age"].dtype)
print(df["mark"].dtype)
print(df["name"].dtype)'''

# value count
'''print(df["name"].value_counts())
print(df["age"].value_counts())
print(df["mark"].value_counts())'''

#discribe numerical values
'''print(df.describe())'''

#add new column
'''df["city"] = input("enter city name :" )
print(df)
def check_result(x):
    if x >= 80:
        return "1st"
    elif x >= 60:
        return "2nd"
    elif x >= 40:
        return "3rd"
    else:
        return "fail"
df["result"] = df["mark"].apply(check_result)
print(df)'''

#update column value
'''df["mark"] = df["mark"].apply(lambda x: x+1 if x < 40 else x) #with lamda function
print(df)'''

#multply column's value
'''df["mark"] = df["mark"]*2
print(df)'''

# rename column
'''print(df.rename(columns={"mark":"Mark"}))#single column rename
print(df)
print(df.rename(columns={
    "name":"Name",
    "age":"Age",
    "mark":"Mark"
},inplace=True)) #multi column rename'''

#delete column
'''print(df.drop("age",axis=1))#single column delete
print(df.drop(["name","mark"],axis=1))#multi column delete
print(df.drop(0,axis=0))#row delete'''

#data shorting and reset index
'''print(df.sort_values(["age"],ascending=[True]).reset_index(drop=True))#single column sort
print(df.sort_values(["mark"],ascending=[False]).reset_index(drop=True))#single column sort
print(df.sort_values(["name","mark"]).reset_index(drop=True))#multi column sort '''

#set column as index
'''print(df.set_index(["age"]))#temporery change 
print(df)
print(df.set_index("age",inplace=True))#permanent change'''

###level-2

#filtering with condition
'''print(df["age"]>18)
print((df["age"]==18)& (df["mark"]>=90))#and condition
print((df["age"]==18)| (df["mark"]>=90))#or condition
print(~(df["age"]==18))#not condition
print(df[df["age"].isin([15,9])])
print(df[df["name"].str.contains("v")])
print(df[df["mark"].between([8,99])])'''

# filter null and not-null value
'''print(df.isnull())
print(df.notnull())'''

#replace value
'''print(df["name"].replace("vishal","rkv"))
'''

# apply
'''print(df["mark"].apply(lambda x : x+1 if x<80 else x))'''

#create column with condition
'''df["gen"] = df["age"].apply(lambda v : "adult" if v >=18 else "teenager")
print(df)
print(df.query("gen=='adult'"))#only adult
print(df.query("gen=='teenager'"))#only teenager
print(df["gen"].value_counts())#count value'''

#unique values
'''print(df.nunique())#all data
print(df["name"].nunique())#specific column'''

#check and remove duplicates
'''print(df.duplicated())#ye row par kam karta hai
print(df.drop_duplicates())  #agr kisi column ke sabhi value kisi dusre column ke sabhi value ka same hai to usme koi ak delete ho jayega
print(df.duplicated(subset=["age"]).value_counts())# column
print(df.drop_duplicates(subset=["age"]).value_counts())#column'''

#convert datatype
'''df["age"] = df["age"].astype(int,inplace=True)
df["mark"] = df["mark"].astype(int,inplace=True)
df["age"] = pd.to_numeric(df["age"],errors="coerce")#error ko handle karne ke liye =(errors="coerce)"
df["mark"] = pd.to_numeric(df["mark"],errors="coerce")
print(df)'''

#uppercase, lowercase str and basic str opp
'''df["name"] = df["name"].str.upper()#VISHAL
df["name"] = df["name"].str.title()#Vishal
df["name"] = df["name"].str.lower()#vishal

print(df)'''

#strip and marge column
'''df["name"] = df["name"].str.strip()#remove space
df["name"] = df["name"].str.rstrip()#right space remove
df["name"] = df["name"].str.lstrip()#left space remove
df["last"] = "kumar","sharma"
df["full_name"] = df["name"]+" "+df["last"]#marging column
df["name"] = df["full_name"]
df["all"] =df["name"].str.cat(df["last"], sep=" ")#agar koi column me empty value hai uske liye hi error nhi aayega
df["all_name"] = df[["name","last"]].agg(" ".join,axis=1)# multicolumn join ke liye 
print(df)'''

#check exist value
'''print("vishal" in df["name"].values )#fast & simple
print(df["name"].isin(["kusum","vishal"]).any())#better and multi value checks
print(df["name"].str.contains("vi").any())#foe word check in value '''

#lambda function
'''df["result"] = df["mark"].apply(lambda x : "top" if x>=90 else "pass")
df["per"] = df.apply(lambda row: row["mark"]+row["age"],axis=1)
print(df)'''

### LEVEL-> 3

#find missing value , count missing value and drop row / column with missing
'''dict_data = {
    "name" : ["vishal","kishan",None],
    "age" : [12,50,20],
    "marks": [None,80,100,]
}
data = pd.DataFrame(dict_data)
print(data)'''
'''print(pd.isnull(data))#finding missing value
print(pd.isnull(data).sum())#sum missing values
print(pd.notnull(data).sum())#sum of attend value
print(data.dropna())#row remove
print(data.dropna(subset="name"))#specific row remove
print(data.dropna(how="all"))#Tabhi row delete hogi jab poori row NaN ho
print(data.dropna(thresh=3))
print(data.drop("age",axis=1))#specific row remove
print(data.drop(columns=["age","marks"]))#multi column remove'''

#fill missing value
'''print(data.fillna(0))#on all nan value
print(data["name"].fillna("benam"))#particuler column me
print(data["age"].fillna(0))
print(data["marks"].fillna(100))'''

#fill with math opp(for int)
'''print(data["age"].fillna(data["age"].mean()))
print(data["marks"].fillna(data["marks"].median()))'''

#forward and backward fill
'''print(data.ffill())#forward fill
print(data.bfill())#backword fill
print(data.ffill().bfill())#both for best for 1st and last nan value fill'''

#detect and remove outlier(for int/float)
'''data = {
    "A" : [10, 12, 14, 16, 18, 200]
}
df = pd.DataFrame(data)
df = df.sort_values(by="A").reset_index(drop=True)
print(df)
Q1 = df["A"].quantile(0.25)
Q3 = df["A"].quantile(0.75)
iqr = Q3 - Q1
lower ,upper = Q1 - 1.5*iqr , Q3 + 1.5*iqr
outlier = df[(df["A"]>upper)|(df["A"]<lower)]
print(outlier)
df_clean= df[(df["A"]>=lower)&(df["A"]<=upper)]#removing outlier
print("your clean data -->>>","\n",df_clean,sep="")'''

#Normizing and Standardize column
'''df = pd.DataFrame(
    {
        "a": [10,20,30,40]
    }
)
q1 = df["a"].quantile(0.25)
q3 = df["a"].quantile(0.75)
iqr = q3 - q1
lower,upper = q1 - 1.5*iqr , q3 + 1.5*iqr
outlier = df[(df["a"]>upper)|(df["a"]<lower)]
print(outlier)
df = df[(df["a"]>=lower)&(df["a"]<=upper)]
print((df["a"]-df["a"].min())/(df["a"].max()-df["a"].min()))#if no any outlier in data , if outlier hai data me to 1st outlier ko clean karo fir normalize karo
print((df["a"]-df["a"].mean())/(df["a"].std()))# standardize column (V.V.I for ML)
'''

#remove special characters
'''df = pd.DataFrame({
    "name":["vishal@","kishan#","kumar1342"]
})
df["clean_num"] =df["name"].str.replace(r"[^a-zA-Z0-9]","",regex = True)#num and letter
df["all_clean"] = df["name"].str.replace(r"[^a-zA-Z]","",regex = True)#only letter
print(df["name"].str.replace(r"\d+$","",regex = True))# its only num removing 
print(df)'''

#convert data
'''data = pd.DataFrame({
    "name":input("enter names ->> ").split(","),
    "age":input("enter age ->> ").split(","),
    "city":input("enter city ->> ").split(","),
    "DOB":input("enter DOB (%d/%m/%Y) ->> ").split(",")
})
print(data)
data["age"] = data["age"].astype(int)#isme agar koi numerical value na ho to error dega
data["age"] = pd.to_numeric(data["age"], errors="coerce")#isme agar numarical value nhi hai to uske jagah par nan aayega magar error se bach jayaga
data["DOB"] = pd.to_datetime(data["DOB"], format="%d/%m/%Y", errors="coerce")#str to datetime
print(data)
data["city"] = data["city"].astype("category")#category convert(optimization)
print(data)
nlist = data["name"].tolist()#dataframe to list
print(nlist)'''

#extract day, month and year
'''dates = pd.DataFrame({
    "date" : ["15/03/2007","13/11/2005","23/08/2011"]
})
print(dates["date"].dtypes)
dates["date"] = pd.to_datetime(dates["date"])
dates["day"] = dates["date"].dt.day
dates["month"] = dates["date"].dt.month
dates["year"] = dates["date"].dt.year
print(dates)'''

#filter, sort and group by date
'''df = pd.DataFrame({
    "date": ["2024-01-10", "2024-01-15", "2024-02-10", "2024-02-20"],
    "sales": [100, 200, 150, 300]
})
df["date"] = pd.to_datetime(df["date"])#filtring
df_jan = df[df["date"].dt.month == 1]
df_jan = df_jan.sort_values(by="date")#sorting
grouped = df_jan.groupby("date")["sales"].sum()  #grouping
groupdi = df_jan.groupby(lambda a: df.loc[a,"date"].month) #grouping with lambda
print(grouped)
print(groupdi)'''

### LEVEL ->> 4

#group by  gender mean mark
'''df = pd.DataFrame({
    "name": ["a","b","c","d"],
    "gen": ["M","F","F","M"],
    "mark":[89,38,90,28]
})
print(df.groupby("gen")["mark"].mean())
print(df.groupby("gen", as_index=False)["marks"].mean())#this better and clean 
'''

#group by city count
'''df = pd.DataFrame({
    "name": ["a","b","c","d"],
    "city":["bihar","chennai","bihar","sitamarhi"]
})
print(df.groupby("city")["city"].value_counts())'''

# group multi columns and max, min mark per group
'''df = pd.DataFrame({
    "name":["a","b","c","d"],
    "age":[18,18,19,28],
    "gen":["M","F","M","M"],
    "city":["bihar","chennai","bihar","sitamarhi"],
    "mark": [80, 70, 90, 60]
})
print(df.groupby(["gen","city"])["mark"].mean())#muti group
print(df.groupby(["gen","city"])["mark"].max())#group with max mark
print(df.groupby(["gen","city"])["mark"].min())#group with min mark
'''
#group eith sum off salary and multiple aggregation and rename it's columns
'''emp = pd.DataFrame({
    "name":["a","b","c","d"],
    "gen":["M","F","M","F"],
    "salary":[100,70,80,90]
})
agg = (emp.groupby(["gen"])["salary"].sum())#it's also call aggregation
m_agg = (emp.groupby(["gen"])["salary"].agg(["sum","count","min","max"]))#multiple aggregation
print("old agg->>","\n",m_agg,sep="")
m_agg = m_agg.rename(columns ={
    "sum":"add",
    "count":"ginti",
    "min":"kam",
    "max":"jyada"
})
print("new agg ->>","\n",m_agg,sep="")#renamed
m_agg.columns = ["jor","ginti","kam","add"]#also renaming
print(m_agg)'''

#group filtering with condition and with custom function
'''df = pd.DataFrame({
    "dept": ["A","A","B","B","B"],
    "salary": [30,30,30,40,50]
})
print(df.groupby("dept").filter(lambda x: x["salary"].mean() >= 30 or x["salary"].mean()>=40))
print(df.groupby("dept").filter(lambda x: x["salary"].sum() >= 100 and x["salary"].min()>=50))#multi function
'''

#opp with data
'''student = pd.DataFrame({
    "name": ["a","b","c","d","e"],
    "loc":["chennai","bihar","sitamarhi","bihar","sitamarhi"],
    "marks":[89,77,90,72,88,]
})
print((student.groupby("loc").filter(lambda x: x["marks"].max() >= 85).reset_index()).rename(columns={"loc":"city","marks":"Top_mark"}))
'''

#value ranking
'''df = pd.DataFrame({
    "marks": [100, 90, 90, 80]
})
df["find"]=df["marks"].rank(ascending=False)#besic
print(df)
print(df["marks"].rank(method = "dense"))
print(df["marks"].rank(method = "min"))
print(df["marks"].rank(method = "max"))
print(df["marks"].rank(method = "first"))'''

#frequency count
'''df = pd.DataFrame({
    "name": ["a","b","c","d","e"],
    "gen":["M","F","M","F","M"],
})
print(df["name"].value_counts())
print((df.groupby("gen")["gen"].value_counts()))
print((df.groupby("gen")["gen"].size()))
print((df.groupby("gen")["gen"].count()))'''

#Transform
'''data = pd.DataFrame({
    "name": ["a","b","c","d","e"],
    "gen":["M","F","M","F","M"],
    "marks":[89,38,90,28,74]
})
data["mean_mark"]= data.groupby("gen")["marks"].transform("mean")# with transform
print(data.groupby("gen")["marks"].mean())#with aggregation
data["diff"] = data["marks"] - data.groupby("gen")["marks"].transform("mean")#opp with transform
data["norm"] = data["marks"] / data.groupby("gen")["marks"].transform("max")# opps with transform
print(data["diff"],"\n",data["norm"],sep="")'''


# compare group values
'''df = pd.DataFrame({
    "team":["a","b","c","d","e"],
    "score":[10,20,60,40,50]
})
df["above_mean"] = df["score"] < df.groupby("team")["score"].transform("mean")#compare with transform
df["sum"]=df["score"] == df.groupby("team")["score"].rank(ascending=False)#compare with function
print(df)'''

