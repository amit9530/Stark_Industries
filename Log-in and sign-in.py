# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:54:33 2019

@author: Amit
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

UsersList=pd.read_excel("D:\\Project\\UsersList.xlsx", "Sheet1")
print(UsersList)


print("Welcome...")
welcome= input("Do you have an acount? y/n: ")

if welcome=="n" or welcome=="N":
    username  = input("Enter a username:")
    for iterator in UsersList['id']:
        if iterator==username:
            username  = input("ID already exist, enter a new one: ")
        #else:
            #UsersList['id']=username
    
