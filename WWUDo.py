import pandas as pd
excel_file='DB.xlsx'
data = pd.read_excel(excel_file)

print (data)

def menu_player():
    print ('בחר אפשרות')
    print ('1- בחירת קטגוריה והתחלת משחק /n 2- צפייה בהוראות המשחק /n 3- צפייה בציונים קודמים /n 4- יציאה מהמערכת')
    choice=int(input())
    
    switch (choice) {
            case 1: choose_category();
            case 2: 
            case 3:
            case 4:
            }
        


def choose_category():
    print(':בחר קטגוריה למשחק')
    print('1- בית ספר')
    print('2- בית')
    print('3- מקום ציבורי')
    choice=input()
    game(choice)
    
choose_category()