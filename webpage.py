from flask import Flask
webpage=Flask(__name__) #目前執行的模組

@webpage.route("/") #@是函式的裝飾，以此函式為基礎
def home():
    return "hello"

@webpage.route("/test") #@是函式的裝飾，以此函式為基礎
def testsd():
    return "this is test"

if __name__=="__main__": #如果以主程式執行
    webpage.run()

