import pandas as pd
import numpy as np
import pandas as pd
import xlsxwriter
import numpy as np
import functools
import xlrd

#-----------------------------------

#Elior Function
#For Testing
Users_db=pd.read_excel('Users_db.xlsx')
User_db=pd.read_excel('123456789.xlsx')
Player_db=pd.read_excel('Player_db.xlsx')
Questions_db=pd.read_excel('Questions_db_new.xlsx')

kid_id=123456789
parent_id=999

def View_Skip(kid_id): #Get kid id and print the question from last game if skip from "User_db"
    suffix=".xlsx"
    file_name=str(kid_id)
    User=pd.read_excel(file_name+suffix)
    Row_List=[]
    for index, rows in User.iterrows():
        my_list = [rows.Q1, rows.A1,rows.Q2, rows.A2,rows.Q3, rows.A3,rows.Q4, rows.A4,rows.Q5, rows.A5]
    if "s" not in my_list:
       print("No questions were skipped")
    else:
        i=0
        while i < len(my_list):
            if my_list[i]=="s":
                print(my_list[i-1])
            i=i+1
    return

def Add_Kid(kid_id,parent_id): #Get kid id and write the parent id in "Parent" in "Player_db"
    Player_db.loc[Player_db.ID == kid_id, 'Parent'] = parent_id
    writer = pd.ExcelWriter('Player_db.xlsx', engine='xlsxwriter')
    Player_db.to_excel(writer)
    writer.save()
    return

def View_Kid(parent_id): #Get parent id and print all the kids that belong to the parent id from "Player_db"
    kids=Player_db.loc[Player_db.Parent==parent_id]
    print(kids['ID'])
    return

def Print_Login_Count(kid_id): #Get kid id and print login count from "Player_db"
    kid=Player_db.loc[Player_db.ID==kid_id]
    print(kid['Login_count'])
    return

def Example_Game(): #play game for example to Understand how to play the game
    x=1
    print("Example Game\n Choose answer 1|2|3:")
    while x<6:
      print("Quetion:",x)
      print("Answer 1")
      print("Answer 2")
      print("Answer 3")
      user_input = input("Enter answer:")
      if user_input=='1' or user_input=='2' or user_input=='3':
          print("You choose answer : ", user_input)
      else:
          print("*** Worng  answer! ***\n*** Choose Only  1 | 2 | 3 ***")
          x = x - 1
      x=x+1
    return


def Most_Mistakes():
    questions_db=pd.read_excel('Question_db_new.xlsx')
    max_mistakes=0
    for mistake in questions_db['Mistakes']:
        if mistake>max_mistakes:
            max_mistakes=mistake
    max_index=(questions_db.index[questions_db['Mistakes']==max_mistakes].tolist())[0]
    print('The question with the most mistakes is {0}'.format(questions_db.loc[max_index]['Question']))
    print('This question has been answered wrong {0} times.'.format(max_mistakes))


def Delete_User():
    id=int(input('Please enter the ID of the user to delete: '))
    # search and delete from players data base
    players=pd.read_excel('Player_db.xlsx')
    for player_id in players['ID']:
        if id==player_id:
            player_index=(players.index[players['ID']==id].tolist())[0]
            new_players=players.drop(player_index)
            new_players.to_excel("Player_db.xlsx")
            print('User deleted!')
            return
    # search and delete from users data base
    users=pd.read_excel('Users_db.xlsx')
    for user_id in users['ID']:
        if id==user_id:
            user_index=(users.index[users['ID']==id].tolist())[0]
            new_users=users.drop(user_index)
            new_users.to_excel("Users_db.xlsx")
            print('User deleted!')
            return
    # if the id wasnt found in any data base
    print('Error - ID not found')
    
def Delete_Question():
    while True:
        category=input('Please choose a category to delete from (School, Home or Public Places): ')
        if (category=='Home' or category=='School' or category=='Public Places'):
            break;
        else:
            print('Invalid category!')
    questions=pd.read_excel('Question_db_new.xlsx')
    # making an index list of questions in the category
    q_list=questions.index[questions['Category']==category].tolist()
    print('Please choose a question to delete:')
    index=1
    # printing questions in the category
    for q_index in q_list:
        print('{0}: {1}'.format(index, questions.loc[q_index]['Question']))
        index+=1
    q_to_delete=int(input())
    print ('You chose to delete the question: {0}'.format(questions.loc[q_list[q_to_delete-1]]['Question']))
    # delete question and update data base
    new_questions=questions.drop(q_list[q_to_delete-1])
    new_questions.to_excel("Question_db_new.xlsx")
    print('Question deleted!')

def Add_Question():
    while True:
        category=input('Please choose category to add a question (School, Home or Public Places): ')
        if (category=='Home' or category=='School' or category=='Public Places'):
            break;
        else:
            print('Invalid category!')
    ques=input('Please enter the question to add: ')
    print('Please enter 3 possible answers: ')
    right_answer=input('The right answer: ')
    answer2=input('Answer 2: ')
    answer3=input('Answer 3: ')
    questions=pd.read_excel('Question_db_new.xlsx')
    new_questions=questions.append({'Category':category, 'Question':ques,'Answer_A':right_answer,'Answer_B':answer2,'Answer_C':answer3,'Mistakes':0,'Right Answer':right_answer},ignore_index=True)
    new_questions.to_excel("Question_db_new.xlsx")
    print('Question added!')
    
def Reset_Player():
    id=int(input('Please enter ID of the child to reset data: '))
    players=pd.read_excel('Player_db.xlsx')
    if not(id in players.ID.values):
        print('ID not found')
        return
    # reset data in players data base
    index=players.index[players['ID']==id].tolist()[0]
    players.at[index, 'Login_count']=0
    players.at[index, ('Last_Login','Q1','A1','Q2','A2','Q3','A3','Q4','A4','Q5','A5','Last grade')]="NaN"
    players.to_excel('Player_db.xlsx')
    id_db='{0}.xlsx'.format(id)
    # create an empty data frame and overrite player's data base
    empty_db=pd.DataFrame(columns=['Date','Grade'])
    empty_db.to_excel(id_db)
    print ('Players data was Reset')
    
    
Reset_Player()
    
#-----------------------------------


def login_report(id):
    """Print the player last login times"""
    playerDB = pd.read_excel('C:\\Users\\xxore\\Documents\\Project GitHub\\Player_db.xlsx')
    index = 0 
    for kid in playerDB['ID']:
        if int(kid)==int(id):
            print("The player last login was at:",playerDB['Last_Login'][index])
        index+=1

def Print_Last_Mistake(id):
    """Print the last game mistakes"""
    playerDB = pd.read_excel('C:\\Users\\xxore\\Documents\\Project GitHub\\Player_db.xlsx')
    question = pd.read_excel('C:\\Users\\xxore\\Documents\\Project GitHub\\Question_db_new.xlsx')
    index = 0
    QandA=[]
    for kid in playerDB['ID']:
        #QandA=[('Q1','A1'),('Q2','A2'),('Q3','A3'),('Q4','A4'),('Q5','A5')]
        if int(kid) == int(id):
            for n in range(1,6):
                a='A'+str(n)
                q='Q'+str(n)
                QandA.append((playerDB[q][index],playerDB[a][index]))
        index+=1
    for index in range(0,len(QandA)):
        i=0
        for q in question['Question']: 
            if str(q) == str(QandA[index][0]):
                if not (question['Right Answer'][i] == QandA[index][1]):
                    if QandA[index][1] == 's':
                        print("Question:\n{0}\nwas skipped.\nThe correct answer is:\n{1}".format(QandA[index][0],question['Right Answer'][i]))
                    else:
                        print("The question:\n{0}\nis incorrect.\nYour answer:\n{1}\nThe correct answer is:\n{2}"
                              .format(QandA[index][0],QandA[index][1],question['Right Answer'][i]))
                    print()
                break
            i+=1
    

def instructions():
    file = open("instruction1.txt", 'r')
    print(file.read())


def player_menu():
    print('בחר אפשרות')
    print('1- בחירת קטגוריה והתחלת משחק \n2- צפייה בהוראות המשחק \n3- צפייה בציונים קודמים \n4- יציאה מהמערכת')
    choice = int(input())
    if (choice == 1):
        choose_category()
    if (choice == 2):
        instructions()  # TODO: add the instruction function to file
    if (choice == 3):
        watch_grades()  # TODO: watch_grades function
    if (choice == 4):
        log_off()  # TODO: log_off function


# --------------------------------------------------


def parent_menu(id):
    print("בחר אפשרות")
    print('1- צפייה בציונים קודמים \n2- צפייה בילדים רשומים\n3- צפייה בדוח התחברות ')
    print('4- צפייה בשאלות ממשחק אחרון \n5- התחל משחק לדוגמא \n6- יציאה')
    choice = int(inpt())
    if (choice == 1):
        watch_grades()  # TODO: choose a child and watch grades function
    if (choice == 2):
        players_report()  # TODO: players report
    if (choice == 3):
        login_report(id)
    if (choice == 4):
        watch_last_game()  # TODO: show last played game, errors and skipped questions
    if (choice == 5):
        exampale_game()  # TODO: make an exampale game without saving grades
    if (choice == 6):
        log_off()  # TODO: log_off function


# --------------------------------------------------


def professional_menu():
    print('בחר אפשרות')
    print(
        '1- הפקת דוחות \n2- צפייה בציונים של הילדים \n3- בחירת ילד וצפייה בשאלות עליהן הוא דילג \n4-  אתחול נתונים של ילד')
    print(
        '5- הוספת שאלה למאגר \n6- מחיקת שאלה מהמאגר \n7- צפייה בשאלה בה טעו הכי הרבה ילדים \n8- מחיקת משתמש \n 9- יציאה מהמערכת')
    choice = int(input())
    if (choice == 1):
        print('1- הפקת דו"ח אודות הורים המשתמשים במערכת \n2-הפקת דוח ילדים המשתמשים במערכת')
        report = int(input())
        if (report == 1):
            parent_report()  # TODO: parent report function
        elif (report == 2):
            players_report()  # TODO: players report
    if (choice == 2):
        watch_grades()  # TODO: choose a child and watch grades function
    if (choice == 3):
        watch_skipped()  # TODO: choose a child and watch skipped questions function
    if (choice == 4):
        reset_playerdata()  # TODO: choose a child and reset data
    if (choice == 5):
        add_question()  # TODO:
    if (choice == 6):
        delete_question()  # TODO:
    if (choice == 7):
        most_wrong()  # TODO: function that shows the question most players answered wrong and change name of function
    if (choice == 8):
        remove_user()  # TODO:
    if (choice == 9):
        log_off()  # TODO: log_off function


# professional_menu()

# --------------------------------------------------


def choose_category():
    print(':בחר קטגוריה למשחק')
    print('1- בית ספר')
    print('2- בית')
    print('3- מקום ציבורי')
    choice = input()
    game(choice)  # TODO: game function
