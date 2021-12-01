print("hello")

"""
x=2**3
print(x)
x=2^2
print(x)
x=4/3
print(x)
x+=1
print(x)

print(x)
x="1234567890"
x=x*2
print(x)
print(x[0:9])
print(x[5:])
print(x[:100])

x=[1,2,3,4,5,6]
print(x)
x[3:]=""
print(x)

x=[1,2,3,4,5,6]
print(x)
x[3:]=[]
print(x)

print(x[1])
x=(11,12,13,14,15,16)
print(x[3])

print(x[3:])
"""


"""
x=[[1,2,3],[4,5,6]]
print(x[0][2])

#集合可以運算比較
x={1,2,3,4,5,6}
y={1,3,5,7,9}
z=x&y
print(z)
z=x|y
print(z)
z=x-y
print(z)
z=x^y
print(z)
z=x-y
print(1 in z)

x = list("hello")
print (x)
x =  set ("hello")
print(x)

x =  "1234"
print("h" in x)

x =  {"a":1,"b":3,"c":5,"d":7,"d":9}
print("" in x)
print(x["d"] )
del x["d"]
print(x )

Dic= {x: x*2 for x in  [3,4,5]} 
print(Dic )
"""

"""
if 2>1: 
    print("xs1")
    print("xs2")
    print("xs3")    
elif True: 
    print("elif")
else: 
    print(Dic )
"""

"""
n=1
while n<3: 
    n+=1
    #continue
    break
    print("1xs1")
    print("1xs2")
    print("1xs3")
    
else:
    print("1xs4")
    print("1xs5")


def hello(msg, msg1):
    print(msg+msg1)

hello("HELLO","AAAA")


def add(msg=1, msg1=2):
    result = msg +msg1
    return result

print(add("HELLO","add"))

print(add())

def unlimitedPara(*para):
    result=""
    for i in para:
        result += "--"+i
    return result

print(unlimitedPara("HELLO","add","1","2"))

def avg(*para):
    result=0
    for i in para:
        result+= i
    result= result/ len(para)
    print(para.__len__)
    return result


print(avg(1,2,3,4,5));

"""
"""
import sys
print(sys.platform)
print(sys.maxsize)
tmpfile = open("tmp.txt","w", encoding="utf-8")
tmpfile.write("123\n")
tmpfile.writelines("789\n")
tmpfile.write("456\n")
tmpfile.writelines("789\r")
#tmpfile.writelines("見鬼123\r\n")
tmpfile.close()
#with open("C:\\temp\\tmp.txt", mode="w", encoding="utf-8") as tmpfile:
with open("tmp.txt", mode="r+", encoding="utf-8") as tmpfile:
    print("x3")
    print (tmpfile.readline())
    print (tmpfile.readline())
    for i in tmpfile:
        print ("*"+ i)
with open("tmp.txt", mode="r+", encoding="utf-8") as tmpfile:
    print("x2")
    tmpdata=tmpfile.readlines()
    for i in tmpdata:
        print ("*"+ i)

with open("tmp.txt", mode="r+", encoding="utf-8") as tmpfile:
    print("x1")
    tmpdata=tmpfile.read()
    print (tmpdata)

with open("tmp.json", mode="w", encoding="utf-8") as tmpfile:
    tmpfile.write("{")
    for i in range(5):
        tmpfile.write("\"i"+str(i)+"\":\""+str(i)+"\",")
    tmpfile.write("\"abc\":\"123\"}")   
print("json")
import json
with open("tmp.json", mode="r+", encoding="utf-8") as tmpfile:
    tmpdata=json.load(tmpfile)
print (tmpdata)
tmpdata["i1"]="new"
tmpdata["new"]="new"
print (tmpdata)
with open("tmp.json", mode="w", encoding="utf-8") as tmpfile:
     json.dump(tmpdata, tmpfile)

with open("tmp.json", mode="r+", encoding="utf-8") as tmpfile:
    tmpdata=json.load(tmpfile)
print (tmpdata)
"""

# import urllib.request   as request 
# import json
# src="https://wic.heo.taipei/OpenData/API/Sewer/Get?stationNo=&loginId=sewer01&dataKey=BD3E513A"
# with request.urlopen(src) as response :


# def readStation(result):
#     for i in result:
#         print (i["stationName"]) 

"""
    tmpdata=json.load(response)
    readStation(tmpdata["data"])
"""

"""
    data= response.read().decode("utf-8") 
with open("tmp.json", mode="w", encoding="utf-8") as tmpfile:
    tmpfile.write(data)
with open("tmp.json", mode="r+", encoding="utf-8") as tmpfile:
    tmpdata=json.load(tmpfile)
    readStation(tmpdata["data"])
"""
#import sys
# sys.path.append("C:\\temp\\PythonWorkspace\\TestProject\\")


import testclass as test
tc=test.IO("console")
tc.check()
test.IO.check("console")
# tc.check("console")

#import就會執行裡面的主程式
#print(test.IO.supportedSrcs)

#變數型態
#數字、文字、布林
# 有順序可動的列表List
# [3,4,5]
# ["hello","word"]

# 有順序不可動的列表Tuple
# (3,4,5)
# ("hello","word")


# 無順序的集合Set
# {3,4,5}
# {"hello","word"}

# key pair 字典 Dictionart
# { "蘋果":"apple", 資料:data}

#變數宣告
#變數不可用數字開頭


