


import mysql.connector

import random

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="H0vhoy2zc4pz", database="eightballtest")

mycursor = mydb.cursor()
'''
mycursor.execute("show tables")
for i in mycursor:




#variable = mycursor.execute( "SELECT test FROM Confirm")
variable = mycursor.execute ("SELECT test FROM Confirm ORDER BY RAND() LIMIT 1")
for i in mycursor:
    print(i)
'''


table = ["1","2","3"]
x = random.choice(table)

print(x)

if x == "1":
    mycursor.execute("SELECT test FROM Confirm ORDER BY RAND() LIMIT 1")
elif x == "2":
    mycursor.execute("SELECT test FROM Disprove ORDER BY RAND() LIMIT 1")
elif x == "3":
    mycursor.execute("SELECT test FROM Notsure ORDER BY RAND() LIMIT 1")

print(mycursor)

