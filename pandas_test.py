import pandas as pd

# dataSeries = pd.Series([313,413432,4234,424,232], index=["a","b","c","d","e"])
# dataSeries = pd.Series(["笨蛋","kitty","python","中文"], index=[1,3,5,6])
# print(dataSeries)
# print(dataSeries[1])
# # print(dataSeries["1"])
# print(dataSeries.dtype)
# print(dataSeries.size)
# print(dataSeries.index)

# # print(dataSeries.nlargest(3))
# print(dataSeries.str.cat(sep=",") )

# dataDF = pd.DataFrame({"name": ["mary","tom","terry"], "salary": [100, 200, 300]}, index=["a","b","c"])  
#dataDF = pd.DataFrame({"name": ["mary","tom","terry"], "salary": ["aa","bb","cc"]}, index=["a","b","c"])  

# print(dataDF)
# print(dataDF.shape)
# print(dataDF.index)
# print(dataDF.size)
# dataDF["cost"]= [10, 15,20]
# print("原始資料",dataDF.iloc[1])
# print("分隔資料",dataDF.iloc[1], sep="\n")
# temp=dataDF.iloc[1]
# dataDF["nickname"]= pd.Series(["笨蛋","python","中文"] ,index=["a","b","c"])
# print("原始資料",dataDF.loc["a"])
# print("分隔資料",dataDF.loc["a"], sep="\n")
# print(dataDF)

# print("原始資料",dataDF["name"])
# temp=dataDF["name"]
# temp= temp.str.cat(sep="-")
# print("連結資料",temp)
# dataDF["cp"]= dataDF["salary"]/dataDF["cost"]
# print(dataDF)

# dataSeries=pd.Series([313,413432,4234,232])
# condition=[False,True,True,False]
# print(condition)
# fiData=dataSeries[condition]
# print(fiData)

# condition=dataSeries >500
# print(condition)
# fiData=dataSeries[condition]
# print(fiData)
# dataSeries = pd.Series(["笨蛋","kitty","python","中文"])
# condition=dataSeries.str.contains("t")
# print(condition)
# fiData=dataSeries[condition]
# print(fiData)


dataDF = pd.DataFrame({"name": ["mary","tom","terry"], "salary": [100, 200, 300]}, index=["a","b","c"]) 
dataDF["cost"]= [10, 15,20]
# print(dataDF)
# condition=[False,True,True]
# print(condition)
# print(dataDF[condition])

# condition=dataDF["salary"]  >150
# print(condition)
# print(dataDF[condition])

data=pd.read_csv("googleplaystore.csv") #把CSV取出為dataFrame
print("數量",data.shape)
print("欄位",data.columns)
print("\n======\n",data["Rating"].mean())

condition =data["Rating"] <=5   #將不合理資料排除
data = data[condition]
print(data.shape)
print("\n======\n",data["Rating"].mean())
# print(data["Installs"])

import sys
temp= data["Installs"].str.replace("[,+]","").replace("Free","")
with open("tmp.txt", mode="w", encoding="utf-8") as tmpfile:
    tmpfile.write(str(temp))

# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
#data["Installs"]=pd.to_numeric(data["Installs"].str.replace("+","").replace("Free","").replace(",",""))
data["Installs"]=pd.to_numeric(temp)
# 
print(data["Installs"].shape)
condition =data["Installs"] > 10000000
print(data[condition].shape)

keyword = input("輸入關鍵字")
condition =data["App"].str.contains(keyword)
print(data[condition].shape)
print(data[condition]["App"])
