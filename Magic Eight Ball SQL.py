import mysql.connector
import random

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="H0vhoy2zc4pz", database="eightballtest")



# select random column #MUST FIX does not work
def selectrandom():
    # just SELECT RANDOM TABLE AND SELECT RANDOM CHOICE
    tablelist = (1, 2, 3)
    randchoice = random.choice(tablelist)
    mycursor = mydb.cursor()
    if randchoice == 1:
        mycursor.execute("SELECT test FROM Confirm ORDER BY RAND() LIMIT 1")
    elif randchoice == 2:
        mycursor.execute("SELECT test FROM Disprove ORDER BY RAND() LIMIT 1")
    elif randchoice == 3:
        mycursor.execute("SELECT test FROM Notsure ORDER BY RAND() LIMIT 1")

    draw = mycursor.fetchall()

    for text in draw:
        return (text)


# showdraw
def showdraw(show):
    print(show)


# ask to selectagain
def selectagain():
    ans3 = input("Would you like to shake again (Y/N)?:")
    if ans3 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("")
        showdraw(selectrandom())
        print("")
        selectagain()
    else:
        main()


# adds a line in a yes,no or tryagain table
def addline():
    addquestion = input("would you like to add a text selection panel?")
    if addquestion in ['y', 'Y', 'yes', 'Yes', 'YES']:
        ans = input("where would you like to add a text? (Yes, No or Tryagain tables?)")
        mycursor = mydb.cursor()

        if ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
            yesinput = input("Enter text do you want to add as Yes table")
            mycursor.execute("INSERT INTO Confirn VALUES (?)", (yesinput))  # need to check if it populates the table
            print("yes statement successfully added")

        elif ans in ['n', 'N', 'no', 'No', 'NO']:
            noinput = input("Enter text do you want to add as No table")
            mycursor.execute("INSERT INTO Disprove VALUES (?)", (noinput))
            print("no statement successfully added")

        elif ans in ['tryagain', 'Tryagain', 'try again', 'Try again', 'Try Again', 'TRY AGAIN']:
            tryagaininput = input("Enter text do you want to add as Tryagain table")
            mycursor.execute("INSERT INTO Notsure VALUES (?)", (tryagaininput))
            print("no-statement successfully added")

        else:
            selectagain()


# def main() need to change first draw from the database
def main():
    print("WELCOME TO MAGIC EIGHT BALL")
    print("")
    ans = input("Would you like to shake (Y/N)?:")

    # main draw function
    if ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("")
        showdraw(selectrandom())
        print("")
        selectagain()

    # need to edit and add edit database
    else:
        ans2 = input("Are you satisfied with your answer (Y/N)?:")
        if ans2 in ['y', 'Y', 'yes', 'Yes', 'YES']:
            print("")
            print("Thanks for participating")
            pass
        else:
            selectagain()

main()

