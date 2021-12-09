from flask import Flask
webpage=Flask(__name__) #目前執行的模組

@webpage.route("/") #@是函式的裝飾，以此函式為基礎
def home():
    return "hello"

@webpage.route("/test") #@是函式的裝飾，以此函式為基礎
def testsd():
    return "this is test"
"""import webCrawler fail"""
import urllib.request   as request 
src="https://www.ptt.cc/bbs/movie/index.html"
src="https://www.ptt.cc/bbs/Gossiping/index.html" #要加cookie
#加header
header={
        "cookie" : "over18=1",#加cookie
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"    
    }

def setheader(_src, _header):
    _req= request.Request(_src, headers=_header)
    return _req

 

def getDOM(_req):
    with request.urlopen(_req) as response :
        _data= response.read().decode("utf-8") 
    import bs4
    _root = bs4.BeautifulSoup(_data, "html.parser")
    # print(root)
    # print(_root.title.string)
    return _root


#抓回上頁的連結
def getbacklink(soup):
    back_tags=soup.find("a",string="‹ 上頁")
    # print(back_tags)
    # print(back_tags["href"])
    return back_tags["href"]
def getdata(soup):
    div_tags=soup.find("div",class_="title")
    # print(div_tags)
    # print(div_tags.a.string)
    return div_tags.a.string

def getalldata(soup):
    #抓標題
    div_tags=soup.find_all("div",class_="title")
    datalist=list()
    for tag in div_tags:
        if tag.a!= None:
            # print(len(datalist))
            # datalist.append(tag.a.string)
            datalist[len(datalist):]=[tag.a.string]
            # print(tag.a.string)
    return datalist
    
def printlist(_data):
    _counter=0
    for i in _data:
        print(str(_counter)+":"+str(i))
        _counter+=1
data=list()
def getData(_src, _header):
    _req=setheader(_src, _header)   
    root=getDOM(_req)
    data.extend(getalldata(root))
    tempsrc="https://www.ptt.cc/"+ getbacklink(root)
    return tempsrc
for i in range(3):
    src=getData(src, header)
printlist(data)
def getlist():
    return data
def gettxt():
    _txt=str()
    for i in data:
        _txt+=str(i)+"<br>\n"
    return _txt
""""""
@webpage.route("/webcrawler") #@是函式的裝飾，以此函式為基礎
def webcrawler():
    
    print("webcrawler")
    # import webCrawler
    # src="https://www.ptt.cc/bbs/Gossiping/index.html" #要加cookie
    # #加header
    # header={
    #         "cookie" : "over18=1",#加cookie
    #         "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"    
    #     }
    # for i in range(3):
    #     src=webCrawler.getData(src, header)
    # return str(webCrawler.getlist())
    return str(gettxt())

if __name__=="__main__": #如果以主程式執行
    webpage.run()
