yes = ["As I see it, YES",
       "It Is Certain",
       "Most Likely",
       "It is Decidedly so",
       "Yes",
       "All Signs Point to Yes",
       "You May Rely on it",
       "Bet your life",
       "Without a Doubt",
       "Definitely",
       "Certainly So",
       "I will say Yes"
        ]
no = ["My reply is no",
       "Dont Count on it",
       "No",
       "Very Doubtful",
       "My Senses say No",
       "I have a bad feeling about this",
       "I dont feel confident",
       "Outlook Not so Good",
       "I won't bet on it",
       "I wouldn't do it",
       "I Doubt it"
       "Negative"
        ]

tryagain = ["Ask Again Later",
       "Better not tell you now",
       "Concentrate and Ask me again",
       "Cannot predict now",
       "I'm not sure",
       "Give me a minute to decide",
       "It is unclear",
       "What does your heart tell you?",
       "I really don't know",
        "Give it it another shot",
        "not sure"
        ]

import random


def mergelist(a, b, c):
    merge = a + b + c
    return merge


def selectrandom(listname):
    draw = random.choice(listname)
    return (draw)


def showdraw(x):
    print(x)


def selectagain():
    ans3 = input("Would you like to shake again (Y/N)?:")
    if ans3 in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("")
        x = mergelist(yes, no, tryagain)
        showdraw(selectrandom(x))
        print("")
        selectagain()
    else:
        main()


def main():
    print("WELCOME TO MAGIC EIGHT BALL")
    print("")

    ans = input("Would you like to shake (Y/N)?:")
    if ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("")
        x = mergelist(yes, no, tryagain)
        showdraw(selectrandom(x))
        print("")
        selectagain()

    else:
        ans2 = input("Are you satisfied with your answer (Y/N)?:")
        if ans2 in ['y', 'Y', 'yes', 'Yes', 'YES']:
            print("")
            print("Thanks for participating")
            pass
        else:
            selectagain()

main()
