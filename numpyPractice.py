# Week 4: NumPy Array
# This topic is about learning to work with Numerical Python (NumPy), one of the most popular libraries in Python.
# It makes it very easy to work with multi-dimensional numerical arrays and matrices with lending support for many mathematical functions.
#
# Please follow the following project to explore how NumPy would be useful in numerical data analysis.
#
# Project: Auto Fuel Efficiency
# In this project we try to use all what we have learned so far, and mainly the numpy arrays to look into auto fuel
# efficiency and the factors that may contribute to that. Let's import our datafile mpg.csv, which contains fuel economy data for 398 cars. Here are the variables included in the dataset.

# mpg: miles per gallon
# cylinders: # of cylinders
# displacement: engine displacement in liters
# horsepower: engine horsepower
# weight: vehicle weight
# acceleration
# model_year: year manufactured
# origin: 1: North America; 2: Europe; 3: Asia and others
# name: name of the car including make and model
# As for the first step, read open the file in a variable and read it as a csv file and load it into a list variable using the csv library.
# Checkout the first few items in the list. What does that look like?


# from google.colab import files
# uploaded = files.upload()


# 1. First you should download the mpg.csv dataset from the above link to your computer. Then use the LEFT sidebar menue on this page
# (Files --> Upload) to upload the scv to your colab session. You would have to do this every time you close your colab session.
# After you uploaded the csv to your colab seccion, use this code to import the csv file into a list
import csv

csvfile=open('mpg.csv') # open the file into a variable
mpg = list(csv.reader(csvfile)) # read the file as csv and then transfer it to a list
mpg[:3] # check out the first three items in our list.

# 2. We do not need the column headings as the first item. Lets move the headings to another variable.



# 3. Try transforming the mpg dataset to NumPy array. What happens?

#Fix the issue by moving the name column to another list.
# You may do this any way you can and print out both the names and the mpg datasets.
# Can you do it with list comprehension?



# 4. Try transforming the mpg dataset to NumPy array. What happens?

# To fix the issue, replace the '?' values with None which represents missing values in Python.
# Try again for transforing the mpg dataset to numpy array. Make sure the array items are of float format.



# 5. To make your data analysis easier, you may chose to read each column in a separate one dimensional array, and give them their heading names.



# 6. Calculate the average mpg for cars based on their number of cylendars.
# It means the average mpg for cars with 3, 4, 5, and other number of cylendars.

# Next, change the code to a function and use that function to calculate average mpg for each model_year.



#7. Create a new column that includes only the make (manufacturer) of each car, like 'ford', 'chevy' and like that.
# Use the previous function and this new column to calculate the average mpg for each manufacturer.



# 8. Count the number of cars in the dataset for each manufacturer.



# 9. Calculate the correlation beween mpg and other variables, like displacement, horsepower, wight and others.
# What are the most and least influential variables on auto fuel economy?


# 10. Use matplotlib library to plot average mpg for each manufacturer.

# Next, change your code to a function that plots average mpg for every variable it is given.
# Use the function to plot average mpg for each origin.