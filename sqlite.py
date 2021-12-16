import sqlite3
def showdata(_data):
    for i in _data:
        print(i)
        for j in i:
            print(j)
conn = sqlite3.connect(":memory:") #在記憶體中建立sqlite DB

# conn = sqlite3.connect('../../../sqlite/film.db')
conn = sqlite3.connect('c:\\temp\\sqlite\\film.db')
print ("Opened database successfully")

cursor=conn.execute('select * from film;')

resultlist= cursor.fetchall()

# cursor.execute('')
showdata(cursor)

cursor.close()
conn.close()
print ("resultlist")
# showdata(resultlist)
# for i in resultlist:
#     print(i)
#     for j in i:
#         print(j)

import pyodbc #很白癡，直接用python sqlite3連即可
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:127.0.0.1' 
server = 'localhost' 
database = 'film.db' 
database = 'C:\\temp\\sqlite\\film.db' 
username = 'myusername' 
password = 'mypassword' 
DSN='film' 
# Trusted_connection=yes  #Windows 驗證的資料來源提供者，不是使用者識別碼和密碼資訊。
# connectstr='DRIVER={SQLite3 ODBC Driver};SERVER='+server+';DATABASE='+database+';Trusted_connection=yes'
# connectstr="DRIVER={SQLite3 ODBC Driver};DSN="+DSN+";server="+server+";Trusted_connection=yes"
connectstr='DRIVER={SQLite3 ODBC Driver};DATABASE='+database  #OK，很白癡，直接用python連即可
cnxn = pyodbc.connect(connectstr)
# cursor = cnxn.cursor()

print (cnxn.execute('select name from sqlite_master where type=\'table\' order by name; '))
# resultset=cnxn.execute('select * from film;')
# print ("successfully")
resultset=cnxn.execute('select name from sqlite_master where type=\'table\' order by name; ')
# resultset=cnxn.execute('select * from film;')
for i in resultset:
    print(i)
    for j in i:
        print(j)


