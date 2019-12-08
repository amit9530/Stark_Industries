import pandas as pd
excel_file='DB.xlsx'
data = pd.read_excel(excel_file)

print (data)

def choose_category():
    print(':בחר קטגוריה למשחק')
    print('1- בית ספר')
    print('2- בית')
    print('3- מקום ציבורי')
    choice=input()
    game(choice)
    
choose_category()