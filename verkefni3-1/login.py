import sqlite3

def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        with sqlite3.connect("Quiz.db") as db:
            cursor=db.cursor()
        find_user = ("SELECT * FROM user Where username = ? and password = ?")
        cursor.execute(find_user,[(username),(password)])
        results=cursor.fetchall()

        if results:
            for x in results:
                print("Welcome "+x[2])
            #return("Exit")
            break

        else:
            print("Username or/and password not recognised")
            again = input("Try again? (y/n): ")
            if again.lower() =="n":
                print("Goodbye")
                #return("Exit")
                break

def newUser():
    found=0
    with sqlite3.connect("Quiz.db") as db:
        cursor = db.cursor()
    while found == 0:
        username = input("Username: ")
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username Taken")
        else:
            found=1
    firstname = input("First name: ")
    surname = input("Surname: ")
    password = input("Password: ")
    password1 = input("Password: ")
    while password !=password1:
        print("Password didn't match")
        password = input("Password: ")
        password1 = input("Password: ")
    insertData = '''INSERT INTO user(username,firstname,surname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(username),(firstname),(surname),(password)])
    db.commit()


def menu():
    while True:
        print("Welcome")
        menu = ('''
        1 - Create user
        2 - Login
        3 - Exit
        ''')

        userChoice = input(menu)

        if userChoice=="1":
            newUser()
        elif userChoice=="2":
            login()
        elif userChoice=="3":
            print("See ya ;)")
            break
        else:
            print("1, 2 or 3 it's not hard")

menu()