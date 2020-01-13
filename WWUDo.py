import pandas as pd
import xlsxwriter
import numpy as np
import functools
import xlrd
import unittest
from openpyxl import load_workbook
import sys


# -----------------------------------

# Elior Function

class Unit_Test(unittest.TestCase):

    def test_View_Skip(self):
        self.assertEqual(View_Skip(), 1)

    def test_Add_Kid(self):
        self.assertEqual(Add_Kid(111111111), 1)

    def test_Print_Login_Count(self):
        self.assertEqual(Print_Login_Count(), 1)

    def test_Example_Game(self):
        self.assertEqual(Example_Game(), 1)

    def test_Most_Mistakes(self):
        self.assertEqual(Most_Mistakes(), 1)

    def test_Delete_User(self):
        self.assertEqual(Delete_User(), 1)

    def test_Delete_Question(self):
        self.assertEqual(Delete_Question(), 1)

    def test_Add_Question(self):
        self.assertEqual(Add_Question(), 1)

    def test_instructions(self):
        self.assertEqual(instructions(), 1)


def View_Skip():  # Get kid id and print the question from last game if skip from "User_db"
    kid_id = input("Please enter kid id")
    suffix = ".xlsx"
    file_name = str(kid_id)
    User = pd.read_excel(file_name + suffix)
    Row_List = []
    for index, rows in User.iterrows():
        my_list = [rows.Q1, rows.A1, rows.Q2, rows.A2, rows.Q3, rows.A3, rows.Q4, rows.A4, rows.Q5, rows.A5]
    if "s" not in my_list:
        print("No questions were skipped")
    else:
        i = 0
        while i < len(my_list):
            if my_list[i] == "s":
                print(my_list[i - 1])
            i = i + 1
    return


def Add_Kid(parent_id):  # Get kid and parent id and write the parent id in "Parent" in "Player_db"
    Player_db = pd.read_excel('Player_db.xlsx')
    kid_id = input("Please enter kid id")
    Player_db.loc[Player_db.ID == kid_id, 'Parent'] = parent_id
    writer = pd.ExcelWriter('Player_db.xlsx', engine='xlsxwriter')
    Player_db.to_excel(writer)
    writer.save()
    return 1


def View_Kid():  # Get parent id and print all the kids that belong to the parent id from "Player_db"
    Player_db = pd.read_excel('Player_db.xlsx')
    parent_id = input("Please enter kid id")
    kids = Player_db.loc[Player_db.Parent == parent_id]
    print(kids['ID'])
    return 1


def Print_Login_Count():  # Get kid id and print login count from "Player_db"
    Player_db = pd.read_excel('Player_db.xlsx')
    kid_id = input("Please enter kid id")
    kid = Player_db.loc[Player_db.ID == kid_id]
    print(kid['Login_count'])
    return 1


def Example_Game():  # play game for example to Understand how to play the game
    x = 1
    print("Example Game\n Choose answer 1|2|3:")
    while x < 6:
        print("Quetion:", x)
        print("Answer 1")
        print("Answer 2")
        print("Answer 3")
        user_input = input("Enter answer:")
        if user_input == '1' or user_input == '2' or user_input == '3':
            print("You choose answer : ", user_input)
        else:
            print("*** Worng  answer! ***\n*** Choose Only  1 | 2 | 3 ***")
            x = x - 1
        x = x + 1
    return 1


# -----------------------------------
def Print_Grades(id):
    ''' function gets id of player and prints all grades from the player's data base'''
    player_db = '{0}.xlsx'.format(id)
    grades = pd.read_excel(player_db)
    print('Printing grades: ')
    for index, row in grades.iterrows():
        print('Grade: {0}, date: {1}'.format(row['Grade'], row['Date']))


def Most_Mistakes():
    ''' function searches in data base for the question with most mistakes and prints it'''
    questions_db = pd.read_excel('Question_db_new.xlsx')
    max_mistakes = 0
    for mistake in questions_db['Mistakes']:
        if mistake > max_mistakes:
            max_mistakes = mistake
    max_index = (questions_db.index[questions_db['Mistakes'] == max_mistakes].tolist())[0]
    print('The question with the most mistakes is {0}'.format(questions_db.loc[max_index]['Question']))
    print('This question has been answered wrong {0} times.'.format(max_mistakes))
    return 1


def Delete_User():
    ''' function deletes user from player db and users db'''
    id = int(input('Please enter the ID of the user to delete: '))
    # search and delete from players data base
    players = pd.read_excel('Player_db.xlsx')
    for player_id in players['ID']:
        if id == player_id:
            player_index = (players.index[players['ID'] == id].tolist())[0]
            new_players = players.drop(player_index)
            new_players.to_excel("Player_db.xlsx")
    # search and delete from users data base
    users = pd.read_excel('Users_db.xlsx')
    for user_id in users['ID']:
        if id == user_id:
            user_index = (users.index[users['ID'] == id].tolist())[0]
            new_users = users.drop(user_index)
            new_users.to_excel("Users_db.xlsx")
            print('User deleted!')
            return
    # if the id wasnt found in any data base
    print('Error - ID not found')
    return 1


def Delete_Question():
    ''' function print all questions in the relevant category , and deletes the question the user chose'''
    while True:
        category = input('Please choose a category to delete from (School, Home or Public Places): ')
        if (category == 'Home' or category == 'School' or category == 'Public Places'):
            break;
        else:
            print('Invalid category!')
    questions = pd.read_excel('Question_db_new.xlsx')
    # making an index list of questions in the category
    q_list = questions.index[questions['Category'] == category].tolist()
    print('Please choose a question to delete:')
    index = 1
    # printing questions in the category
    for q_index in q_list:
        print('{0}: {1}'.format(index, questions.loc[q_index]['Question']))
        index += 1
    q_to_delete = int(input())
    print('You chose to delete the question: {0}'.format(questions.loc[q_list[q_to_delete - 1]]['Question']))
    # delete question and update data base
    new_questions = questions.drop(q_list[q_to_delete - 1])
    new_questions.to_excel("Question_db_new.xlsx")
    print('Question deleted!')
    return 1


def Add_Question():
    ''' function adds question according to the category the user chose'''
    while True:
        category = input('Please choose category to add a question (School, Home or Public Places): ')
        if (category == 'Home' or category == 'School' or category == 'Public Places'):
            break;
        else:
            print('Invalid category!')
    ques = input('Please enter the question to add: ')
    print('Please enter 3 possible answers: ')
    right_answer = input('The right answer: ')
    answer2 = input('Answer 2: ')
    answer3 = input('Answer 3: ')
    questions = pd.read_excel('Question_db_new.xlsx')
    new_questions = questions.append(
        {'Category': category, 'Question': ques, 'Answer_A': right_answer, 'Answer_B': answer2, 'Answer_C': answer3,
         'Mistakes': 0, 'Right Answer': right_answer}, ignore_index=True)
    new_questions.to_excel("Question_db_new.xlsx")
    print('Question added!')
    return 1


def Reset_Player():
    ''' function deletes player's grades and last game data'''
    id = int(input('Please enter ID of the child to reset data: '))
    players = pd.read_excel('Player_db.xlsx')
    if not (id in players.ID.values):
        print('ID not found')
        return
    # reset data in players data base
    index = players.index[players['ID'] == id].tolist()[0]
    players.at[index, 'Login_count'] = 0
    players.at[index, ('Last_Login', 'Q1', 'A1', 'Q2', 'A2', 'Q3', 'A3', 'Q4', 'A4', 'Q5', 'A5', 'Last grade')] = "NaN"
    players.to_excel('Player_db.xlsx')
    id_db = '{0}.xlsx'.format(id)
    # create an empty data frame and overrite player's data base
    empty_db = pd.DataFrame(columns=['Date', 'Grade'])
    empty_db.to_excel(id_db)
    print('Players data was Reset')
    return 1


# -----------------------------------


def login_report(id):
    """Print the player last login times"""
    playerDB = pd.read_excel('Player_db.xlsx')
    index = 0
    for kid in playerDB['ID']:
        if int(kid) == int(id):
            print("The player last login was at:", playerDB['Last_Login'][index])
        index += 1


def Print_Last_Mistake(id):
    """Print the last game mistakes"""
    playerDB = pd.read_excel('Player_db.xlsx')
    question = pd.read_excel('Question_db_new.xlsx')
    index = 0
    QandA = []
    for kid in playerDB['ID']:
        # QandA=[('Q1','A1'),('Q2','A2'),('Q3','A3'),('Q4','A4'),('Q5','A5')]
        if int(kid) == int(id):
            for n in range(1, 6):
                a = 'A' + str(n)
                q = 'Q' + str(n)
                QandA.append((playerDB[q][index], playerDB[a][index]))
        index += 1
    for index in range(0, len(QandA)):
        i = 0
        for q in question['Question']:
            if str(q) == str(QandA[index][0]):
                if not (question['Right Answer'][i] == QandA[index][1]):
                    if QandA[index][1] == 's':
                        print("Question:\n{0}\nwas skipped.\nThe correct answer is:\n{1}".format(QandA[index][0],
                                                                                                 question[
                                                                                                     'Right Answer'][
                                                                                                     i]))
                    else:
                        print("The question:\n{0}\nis incorrect.\nYour answer:\n{1}\nThe correct answer is:\n{2}"
                              .format(QandA[index][0], QandA[index][1], question['Right Answer'][i]))
                    print()
                break
            i += 1


def Print_Last_Grade(id):
    playerDB = pd.read_excel('Player_db.xlsx')
    index = 0
    for kid in playerDB['ID']:
        if int(kid) == int(id):
            print(playerDB['Last grade'][index])
        index += 1


def View_All(user_type):
    """View all the user type"""
    # Need to change to the right file path
    UsersDB = pd.read_excel('Users_db.xlsx')
    index = 0
    for user in UsersDB['ID']:
        types = UsersDB['User type'][index]
        if (types == user_type):
            print(user)
        index = index + 1


def instructions():
    file = open("instruction1.txt", 'r')
    print(file.read())
    return 1


def Choose_Category(id):
    print('Choose game category')
    print('1- School')
    print('2- Home')
    print('3- Public places')
    print('4- Random questions')
    choice = input()
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print('Wrong input, try again')
        print('1- School')
        print('2- Home')
        print('3- Public places')
        print('4- Random questions')
        choice = input()
    game(choice, id)  # TODO: game function - AMIT


def Print_Last_Game(id):
    Player_db = pd.read_excel('Player_db.xlsx', "Sheet1")
    flag = True
    for Id in Player_db['ID']:
        if id == Id:
            flag = False
    if not flag:
        if Player_db[id]['Q1'] == None:
            print("The player didnt play yet")
        else:
            print("question 1: ", Player_db[id]['Q1'])
            if Player_db[id]['A1'] == 's':
                print("the player skipped the question")
            else:
                print("answer 1: ", Player_db[id]['A1'])
            print("question 2: ", Player_db[id]['Q2'])
            if Player_db[id]['A2'] == 's':
                print("the player skipped the question")
            else:
                print("answer 2: ", Player_db[id]['A2'])
            print("question 3: ", Player_db[id]['Q3'])
            if Player_db[id]['A3'] == 's':
                print("the player skipped the question")
            else:
                print("answer 3: ", Player_db[id]['A3'])
            print("question 4: ", Player_db[id]['Q4'])
            if Player_db[id]['A4'] == 's':
                print("the player skipped the question")
            else:
                print("answer 4: ", Player_db[id]['A4'])
            print("question 5: ", Player_db[id]['Q5'])
            if Player_db[id]['A5'] == 's':
                print("the player skipped the question")
            else:
                print("answer 5: ", Player_db[id]['A5'])


def Player_Menu(id):
    print("Choose an option: ")
    print('1- Play game \n2- Show game instructions \n3- Show grades')
    print('4- Show last played game \n5- Show last game skipped question \n6- Show the latest grade')
    print('7- Exit to login screen')

    choice = int(input())
    if (choice == 1):
        Choose_Category(id)
    if (choice == 2):
        instructions()
    if (choice == 3):
        Print_Grades(id)
    if (choice == 4):
        Print_Last_Game(id)  # TODO:  Print_Last_Game - AMIT
    if (choice == 5):
        View_Skip()
    if (choice == 6):
        Print_Last_Grade()  # TODO: Print_Last_Grade - OREN
    if (choice == 7):
        Login_And_SignIn()
    Player_Menu(id)

# --------------------------------------------------


def Parent_Menu(id):
    print("Choose an option: ")
    print('1- Add kid \n2- View kid\n3- Show grades ')
    print("4- Show the kid's login count \n5- Show last game skipped question \n6- Play example game")
    print("7- Show kid's last game \n8- Show the kid's last game mistake \n9- Show the kid's last loggin date")
    print('10- Exit to login screen')

    choice = int(input())
    if (choice == 1):
        Add_Kid(id)
    if (choice == 2):
        View_Kid()
    if (choice == 3):
        Id = int(input('Please enter child ID: '))
        Print_Grades(Id)
    if (choice == 4):
        Print_Login_Count()
    if (choice == 5):
        View_Skip()
    if (choice == 6):
        Example_Game()
    if (choice == 7):
        Id = int(input('Please enter child ID: '))
        Print_Last_Game(id)  # TODO: Print_Last_Game - Amit
    if (choice == 8):
        Print_Last_Mistake()
    if (choice == 9):
        login_report()
    if (choice == 10):
        Login_And_SignIn()
    Parent_Menu(id)


# --------------------------------------------------


def Professional_Menu(id):
    print('Choose an option: ')
    print(
        '1- Reports\n2- Watch childs grades\n3- Watch childs last games skipped questions\n4- Reset players data\n5- Add a question\n6- Delete a question')
    print('7- Watch the most mistaken question\n8- Delete a user\258741359n9- Exit to login screen')
    choice = int(input())
    if (choice == 1):
        print('1- Players report/n2- Parent report')
        report = int(input())
        if (report == 1):
            View_All(1)  # TODO: oren
        elif (report == 2):
            View_All(2)  # TODO: oren
    if (choice == 2):
        ID = input('Please enter childs ID: ')
        Print_Grades(ID)
    if (choice == 3):
        ID = input('Please enter childs ID: ')
        View_Skip(ID)
    if (choice == 4):
        Reset_Player()
    if (choice == 5):
        Add_Question()
    if (choice == 6):
        Delete_Question()
    if (choice == 7):
        Delete_Question()
    if (choice == 8):
        Delete_User()
    if (choice == 9):
        Login_And_SignIn()
    Professional_Menu(id)


# --------------------------------------------------


# login and sign-in function
def Login_And_SignIn():
    write = load_workbook(filename='Users_db.xlsx')
    sheet = write.active
    Users_db = pd.read_excel('Users_db.xlsx', "Sheet1")

    print("Welcome...")
    welcome = input("Do you have an account? y/n: ")

    if welcome == "n" or welcome == "N":
        count = 0
        for i in Users_db['ID']:
            count += 1
        count += 1
        while True:
            username = int(input("Enter a username: "))
            flag = False
            for Id in Users_db['ID']:
                if username == Id:
                    flag = True
            if not flag:
                IdCell = sheet.cell(row=count + 1, column=1)
                IdCell.value = username
                password = int(input("Enter a password: "))
                PasswordCell = sheet.cell(row=count + 1, column=2)
                PasswordCell.value = password
                print("Type 1 for Player")
                print("Type 2 for Parent")
                print("Type 3 for Professional")
                usertype = int(input("Enter the user type: "))
                while usertype != 1 and usertype != 2 and usertype != 3:
                    usertype = int(input("Wrong input, try again: "))
                TypeCell = sheet.cell(row=count + 1, column=3)
                TypeCell.value = usertype
                break
            print("ID already exist")
        write.save(filename='Users_db.xlsx')
        if usertype == 1:
            print("Welcome to the Player Menu")
            Player_Menu(username)
        elif usertype == 2:
            print("Welcome to the Parent Menu")
            Parent_Menu(username)
        elif usertype == 3:
            print("Welcome to the Professional Menu")
            Professional_Menu(username)

    elif welcome == "y" or welcome == "Y":
        while True:
            username = int(input("Enter a username: "))
            i = 0;
            for row in sheet.rows:
                i = i + 1;
                for cell in row:
                    if cell.value == username:
                        line = i
            flag = True
            for Id in Users_db['ID']:
                if username == Id:
                    flag = False
            if not flag:
                while True:
                    password = int(input("Enter a password: "))
                    flag = False
                    if password != Users_db['Password'][line - 2]:
                        flag = True
                    if not flag:
                        if Users_db['Type'][line - 2] == 1:
                            print("Welcome to the Player Menu")
                            Player_Menu(username)
                        elif Users_db['Type'][line - 2] == 2:
                            print("Welcome to the Parent Menu")
                            Parent_Menu(username)
                        elif Users_db['Type'][line - 2] == 3:
                            print("Welcome to the Professional Menu")
                            Professional_Menu(username)
                    print("Wrong password, try again")
                break
            print("ID not exist in the system")


Login_And_SignIn()





