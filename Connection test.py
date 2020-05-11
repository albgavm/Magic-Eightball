import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="H0vhoy2zc4pz", database="eightballtest")

mycursor = mydb.cursor()
mycursor.execute("show tables")

for i in mycursor:
    print(i)