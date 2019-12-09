import pandas as pd
#excel_file='DB.xlsx'
#data = pd.read_excel(excel_file)

def instructions():
    file=open("instruction1.txt",'r')
    print(file.read())


def player_menu():
    print ('בחר אפשרות')
    print ('1- בחירת קטגוריה והתחלת משחק \n2- צפייה בהוראות המשחק \n3- צפייה בציונים קודמים \n4- יציאה מהמערכת')
    choice=int(input())
    if (choice==1):
        choose_category()
    if (choice==2):
        instructions()  #TODO: add the instruction function to file
    if (choice==3):
        watch_grades()  #TODO: watch_grades function
    if (choice==4):
        log_off()  #TODO: log_off function


#--------------------------------------------------

def professional_menu():
    print ('בחר אפשרות')
    print ('1- הפקת דוחות \n2- צפייה בציונים של הילדים \n3- בחירת ילד וצפייה בשאלות עליהן הוא דילג \n4-  אתחול נתונים של ילד')
    print ('5- הוספת שאלה למאגר \n6- מחיקת שאלה מהמאגר \n7- צפייה בשאלה בה טעו הכי הרבה ילדים \n8- מחיקת משתמש \n 9- יציאה מהמערכת')
    choice=int(input())
    if (choice==1):
        print ('1- הפקת דו"ח אודות הורים המשתמשים במערכת \n2-הפקת דוח ילדים המשתמשים במערכת')
        report=int(input())
        if (report==1):
            parent_report() #TODO: parent report function
        elif (report==2):
            players_report() #TODO: players report
    if (choice==2):
        watch_grades() #TODO: choose a child and watch grades function
    if (choice==3):
        watch_skipped() #TODO: choose a child and watch skipped questions function
    if (choice==4):
        reset_playerdata() #TODO: choose a child and reset data
    if (choice==5):    
        add_question() #TODO:
    if (choice==6):    
        delete_question() #TODO:
    if (choice==7):   
        most_wrong() #TODO: function that shows the question most players answered wrong and change name of function
    if (choice==8):
        remove_user() #TODO:
    if (choice==9):
         log_off()  #TODO: log_off function

#professional_menu()
         
#--------------------------------------------------
    
    
def choose_category():
    print(':בחר קטגוריה למשחק')
    print('1- בית ספר')
    print('2- בית')
    print('3- מקום ציבורי')
    choice=input()
    game(choice)   #TODO: game function
    