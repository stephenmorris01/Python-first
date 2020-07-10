# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:17:14 2020

@author: steph
"""


# creates a list of user inputs

print("I will create a list of integers.")

list = []

n = int(input("Enter number of items : "))

print("Enter each of the ", n, " numbers. Enter one at a time, each time followed by the 'Enter' key.")
for i in range(0, n):

    item = int(input())

    list.append(item) # adding the items

print("Here is your list of ", n, " numbers!")
print(list)
    
