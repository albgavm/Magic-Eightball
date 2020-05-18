


import mysql.connector
import inquirer

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


table = ["1","2","3"]
x = random.choice(table)


if x == "1":
    mycursor.execute("SELECT test FROM Confirm ORDER BY RAND() LIMIT 1")
elif x == "2":
    mycursor.execute("SELECT test FROM Disprove ORDER BY RAND() LIMIT 1")
elif x == "3":
    mycursor.execute("SELECT test FROM Notsure ORDER BY RAND() LIMIT 1")

rows = mycursor.fetchall()    # get all selected rows, as Barmar mentioned
for r in rows:
    print(r)
'''


addquestion = input("would you like to add a text selection panel?")

questions = [
    inquirer.List('size',
                  message="would you like to add a text selection panel?",
                  choices=['Shake', 'Edit', 'Exit'],
                  ),
]


