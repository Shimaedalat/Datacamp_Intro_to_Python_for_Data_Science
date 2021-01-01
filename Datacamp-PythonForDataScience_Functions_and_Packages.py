# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:24:05 2020

@author: shima
"""

# Creating new variables
var1 = [1, 2, 3, 4]
var2 = True

# Checking the variable types
print(type(var1))
print(type(var2))

# Checking the length of var1
print(len(var1))

# Converting var2 type to integer 
out2 = int(var2)
print(type(out2))

# Creating two different lists
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Pasting together 
full = first + second

# Sort full in descending order : 
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# String methods
room = "poolhouse"

# Applying upper()
room_up = room.upper()
print(room_up)

# Counting an element in a string
print(room.count("o"))

# List methods
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Finding the index of an specific element
print(areas.index(20.0))

# Checking how often a number appears in a list
print(areas.count(15))

# Using append to add elements to a list
areas.append(24.5)
areas.append(15.45)
print(areas)

# Reveersing the  order of elements in a list
areas.reverse()
print(areas)

# Defining radius
r = 0.43

# Importing the math package
import math

# Calculating C
C = 2*math.pi*r

# Calculatinf A
A = math.pi*r*r

# Checking the results
print("Circumference: " + str(C))
print("Area: " + str(A))
 
