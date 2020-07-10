# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:28:00 2020

@author: steph
"""


# prints the current time
from time import gmtime, strftime

t = strftime("%m/%d/%Y %H:%M:%S local") # current local time
g = strftime("%m/%d/%Y %H:%M:%S GMT", gmtime()) # current GMT time

print (t)
print (g)
