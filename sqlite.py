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

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:127.0.0.1' 
server = 'localhost' 
database = 'xfilm.db' 
username = 'myusername' 
password = 'mypassword' 
# cnxn = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};SERVER='+server+';DATABASE='+database+';Trusted_connection=yes')
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


