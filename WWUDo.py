import pandas as pd
#myData=pd.read_excel("Question_db.xlsx",encoding = "ISO-8859-1")

def instructions():
    file=open("instruction1.txt",'r')
    print(file.read())

print("Running instructions...")
instructions()
print()
print("Run has ended")