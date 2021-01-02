# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:06:49 2020

@author: shima
"""

# Importing numpy
import numpy as np

# create list height
height = [180, 215, 210, 210, 188, 176, 209, 200]

# Creating np_height
np_height = np.array(height)

# Checking the type of the file
print(type(np_height))

# Create a mumpy array from height 
np_height_in = np.array(np_height)
print(np_height_in)

# Convert the height from inch to m
np_height_m = np_height_in*0.0254
print(np_height_m)

# Create a weight list
weight =  [70, 65, 80, 91, 68, 76, 79, 82]
np_weight = np.array(weight)

# Calculating BMI: BMI = weight(kg)/(np_height_m**2)
bmi = np_weight/(np_height_m**2)

# Create the light array
light = bmi<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Print subarray index 3-6
print(weight[2:5])

# Check numpy array type: 'numpy.ndarray' is one dementional
print(type(bmi))

# Creating 2D array of the previous one
bmi_2d = ([np_weight/(np_height_m**2)],
          [np_weight/(np_height_m**2)])

# Checking the type : class 'tuple'
print(type(bmi_2d))

# Checking the dimentions of the array
print(bmi_2d)

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print(np_baseball)
# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 2th row of np_baseball
print(np_baseball[1,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Calculating the mean value
print(np.mean(np_baseball))

# What is the median value
print(np.median(np_baseball))

# What is the average value of the first column
avg = np.mean(np_baseball[:,0])

# Print the results
print("Average:" + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))

# Creating position and height files
positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights = np.array(heights)
np_positions = np.array(positions)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

