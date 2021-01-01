# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:10:40 2020

@author: shima
"""

# Python as a calculator

# Division 
print(5 / 8)

# Addition
print(7 + 8)

# Subtraction
print(18 - 5)

# Multiplication
print(4 * 5)

# Exponentiation
print(4 ** 2)

# Modulo/mod (reaminder)
print(18 % 5)

# Creating a variable
saving = 5000

# Printing the variable
print(saving)

# Calculating based on variables
factor = 1.1

# formulating the result
result = saving * factor ** 5

# printing outcome
print(result)

# Create a variable desc and profitable
desc = 'compound interest'
profitable = True

# Applying customized formula
year1 = saving*factor 

# Checking the output type
print(type(year1))

# Fixing print out text
print('I started with $' + str(saving) + ' and now I have $' + str(result) + '. Awesome!')

# Defining pi_string
pi_string = '3.1415926'

# Converiting pi_string to pi_float
pi_float = float(pi_string)
print(type(pi_float))

# create a list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
         
# create a copy
areas_copy = [11.25, 18.0, 20.0, 10.75, 9.50]

# modifying the copy file
areas_copy[0] = 5.0
print(areas_copy)

# the original file is untouched
print(areas)

# create a list another list
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# create list in square meter
area = [11.25,18.0,20.0,10.75,9.50]
print(area)

# modify list area
area = ["hallway",hall,"kitchen", kit, "living room", liv,"bedroom", bed, "bathroom", bath]

# checking resuölts, contains both areas and square meters
print(area)

# creating list of list
house = [ ['hallway', hall],
        ['kitchen', kit],
['living room', liv], ["bedroom",bed],["bathroom",bath]]
print(house)

# retrieving subsets, for example the second element
print(areas[1])

# printing the last element of the list
print(areas[-1])

# retriving the fourth element in the list
print(areas[3])

# summing up subsets, kitchen and living room 
eat_sleep_area = areas[1]+ areas[-3]
print(eat_sleep_area)

# sllicing and dicing
downstairs = areas[:6]

# similarly create upstairs
upstairs = areas[6:]
print(upstairs)
print(upstairs)

# replace list elements
areas[2]= "chill zone"

# extend a list, adding poolhouse to data 
areas_1 = areas + ["poolhouse", 24.5] 

# Adding garage to the last list
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)



