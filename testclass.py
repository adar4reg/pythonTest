

class IO:
    # def __init__(self) -> None:
    #     pass
    # def __init__(self):
    #     self.x=1
    def __init__(self,name):
        self.name=name
        self.file=None
    supportedSrcs=["console","file"]
    def open(self):
        self.file=open(self.name, mode="r+", encoding="utf-8")
    def read(self):
        return self.file.read()
    def close(self):
        return self.file.close()    
    def check(src):
        if src not in IO.supportedSrcs:
            print("not support")
        else:
            print("read from ", src)

#使用
print(IO.supportedSrcs)
IO.check("file")
IO.check("internet")

# iIO= IO()
# print(iIO.x)
# print(iIO.supportedSrcs)
iIO= IO("tmp.txt")
print(iIO.name)
iIO.open()
print(iIO.read())


class Name:
    def __init__(self,fname, lname):
        self.first=fname
        self.last=lname
        self.name=self.first+" "+self.last
    def show(self):
        print("First="+n1.first)
        print("Last="+n1.last)
        print("NAME="+n1.name)
    def get(self):
        return n1.name   
n1=Name("terry","yang")
print(n1.name)
n1.show()    
print(n1.get())