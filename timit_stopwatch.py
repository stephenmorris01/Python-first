# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:10:17 2020

@author: steph
"""


# simple stopwatch

# use timeit

from time import strftime
import timeit

print ("start time", strftime("%m/%d/%Y %H:%M:%S local"))
start = timeit.timeit()
n = 2+2
print("2 + 2 is", n)
end = timeit.timeit()
print ("This took", end - start, "seconds")
print ("end time", strftime("%m/%d/%Y %H:%M:%S local"))
