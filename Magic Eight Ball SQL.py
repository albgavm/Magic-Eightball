import inquirer
import mysql.connector
import random

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="H0vhoy2zc4pz", database="eightballtest")


def selectrandom():
    #select random table from SQL then select random row
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


def showdraw(show):
    print(show)

def selectagain():
    #ask to selectagain
    ans3 = input("Would you like to shake again (Y/N)?:")
    if ans3 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("")
        showdraw(selectrandom())
        print("")
        selectagain()
    else:
        main()

def editselection():
    #edits the messages
    pass

def deleteselection():
    #deletes the messages
    pass

def viewselection():
    #views the messages
    pass


# adds a line in a yes,no or tryagain table
def addselection():

    questions = [
        inquirer.List('size',
                      message="would you like to add a text selection panel?",
                      choices=['Yes Text', 'No Text', 'Try Again Text'],
                      ),
    ]
    addquestion = inquirer.prompt(questions)


    if addquestion in ['y', 'Y', 'yes', 'Yes', 'YES']:
        ans = input("where would you like to add a text? (Yes, No or Tryagain tables?)")
        mycursor = mydb.cursor()

        if ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
            yesinput = input("Enter text do you want to add as Yes table")
            mycursor.execute("INSERT INTO Confirm VALUES (?)", (yesinput))  # need to check if it populates the table
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
#make whole table of selection

def main():

    print("")
    print("WELCOME TO MAGIC EIGHT BALL")
    print("choose to shake, or edit current messages")
    print("")

    start = input("press enter to continue")

    if start == "":

        questions = [
            inquirer.List('mainmenu',
                          message="Main Menu",
                          choices=['Shake', 'Edit', 'Exit'],
                          carousel=True,
                          ),
        ]
        ans = inquirer.prompt(questions)

        # main shake function
        if ans["mainmenu"] =='Shake':
            print("")
            showdraw(selectrandom())
            print("")
            selectagain()

        #edit menu
        if ans["mainmenu"] =='Edit':
            editquestions = [
                inquirer.List('edit',
                              message="Choose Edit Options",
                              choices=['Show', 'Add', 'Delete', 'Edit selection', 'Back to Main'],
                              carousel=True,
                              ),
            ]
            ansedit = inquirer.prompt(editquestions)

            if ansedit["edit"] =='Show':
                viewselection()

            elif ansedit["edit"] == 'Add':
                addselection()

            elif ansedit["edit"] == 'Delete':
                deleteselection()

            elif ansedit["edit"] == 'Edit Selection':
                editselection()

            elif ansedit["edit"] == 'Back to Main':
                main()


        else:
            #must edit to inquirer
            ans2 = input("Are you sure you want to exit (Y/N)?:")
            if ans2 in ['y', 'Y', 'yes', 'Yes', 'YES']:
                print("")
                print("Thanks for participating")
                pass
            else:
                main()

main()

