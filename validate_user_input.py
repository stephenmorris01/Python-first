# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:17:14 2020

@author: steph
"""


# prints user-input characters

while True:
    userWord = input("Please enter a word ")
    try:
        val = int(num)
        print("Input is an integer number.")
        break;
    except ValueError:
        try:
            float(num)
            print("Input is a float number.")
            break;
        except ValueError:
            print("You said", userWord)
    
