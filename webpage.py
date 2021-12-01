from flask import Flask
webpage=Flask(__name__) #目前執行的模組

@webpage.route("/") #@是函式的裝飾，以此函式為基礎
def home():
    return "hello"

@webpage.route("/test") #@是函式的裝飾，以此函式為基礎
def testsd():
    return "this is test"

@webpage.route("/webcrawler") #@是函式的裝飾，以此函式為基礎
def webcrawler():
    print("webcrawler")
    import webCrawler
    # src="https://www.ptt.cc/bbs/Gossiping/index.html" #要加cookie
    # #加header
    # header={
    #         "cookie" : "over18=1",#加cookie
    #         "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"    
    #     }
    # for i in range(3):
    #     src=webCrawler.getData(src, header)
    # return str(webCrawler.getlist())
    return str(webCrawler.gettxt())

if __name__=="__main__": #如果以主程式執行
    webpage.run()
