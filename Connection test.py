


import mysql.connector
from Magic Eight Ball import selectrandom



mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="H0vhoy2zc4pz", database="eightballtest")

mycursor = mydb.cursor()
'''
mycursor.execute("show tables")
for i in mycursor:
    print(i)

'''



#variable = mycursor.execute( "SELECT test FROM Confirm")
variable = mycursor.execute ("SELECT * FROM Confirm
    ORDER BY RAND()
    LIMIT 1;")

for i in mycursor:
    print(i)



