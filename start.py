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
     json.dumps(tmpdata, tmpfile)

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

# #send mail
# import email.message 

# #建立訊息物件 
# msg= email.message.EmailMessage() 

# #訊息物件基本設定 
# msg["From"] ="adar4tmp@gmail.com"
# # msg["To"] ="2100786@systexsoftware.com.tw, terryyang@systexsoftware.com.tw, "
# msg["To"] ="adar4job@gmail.com, adar4reg@gmail.com"
# msg["Cc"] ="adar4tmp@gmail.com"
# msg["Subject"] ="發信測試"
# msg.set_content("EMAIL訊息內容") 

# #加入HTML內容 
# # msg.add_alternative("<h3>HTML內容</h3>", subtype="html") 
# import smtplib 
# #連線smtp 
# Server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 

# #發送 
# Server.login("adar4tmp@gmail.com", "superwind") 
# print(Server.send_message(msg) )
# Server.close() 

 


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

def printIterable(_iterable):
    for x in _iterable:
        print(x)
# #iterable
# iterable= (1,2,3) #Tuple
# printIterable(iterable);
# iterable={3,4,5} #set
# printIterable(iterable);
# iterable=["c","b", "a"] #list
# printIterable(iterable);
# iterable={ "蘋果":"apple", "資料":"data"} #dic
# printIterable(iterable);

# #Generator
# def my_generator():
#     print("new value is generated!1")
#     yield 5
#     print("new value is generated!2")
#     yield 10
#     for x in range(1, 10):
#         print("new value is generated!"+str(x))
#         yield x

# def even_generator():
#     x=0
#     while True:
#         x+=2
#         print("new value is generated!"+str(x))
#         yield x
# # iterable= my_generator()
# iterable= even_generator()
# # printIterable(iterable)

# print(iterable.__next__())
# print(next(iterable))

# #callback
# def test(arg,data):
#     arg(data)
# def handle(data): 
#     print(data)
# test(handle,100)


##裝飾器
# def testDecorator(_callback): 
#     def  innerfun(): 
# #處理邏輯 
#         print("innerfun")
#         _callback(3) 
#     return innerfun 
# @testDecorator
# def decoratedfun(data): 
# #處理邏輯 
#     print("decoratedfun", data)
# decoratedfun() 



##裝飾器工廠
def testFactory(base):
    print("testFactory")
    def testDecorator(_callback): 
        def  innerfun(): 
    #處理邏輯 
            print("innerfun")
            result=base*3
            _callback(result) 
        return innerfun 
    return testDecorator 

@testFactory(3)
def decoratedfun(data): 
    print("decoratedfun", data)

decoratedfun() 


@testFactory(3)
def decoratedCfun(data): 
    print("裝飾器功能", data)
