# Patrick Moore 2018-03-26
# This file contains a Python script to form part of my 2018 project for the Progamminf and Scripting Module of the H.DIP in Data Analytics
# Iris Analyser is the script used to analyse the iris data set
# Iris Data Set - (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
# Reference for the problem - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) fromt the Python Tutorial

# Section 1 - Functions - In this section of the project, the functions used to analyse the data are defined

def count():                                     # count() is a function that will count the number of rows in the data file
  with open("data/iris.csv", "r") as myfile:     # this statement opens the iris data set as an object called myfile
    counter = 0                                  # this initialises a variable that will used to store the values of the count
    for line in myfile:                          # this loop run through the rows of the file one a a time
      counter = counter + 1                      # for each pass through the loop the counter is incremented by one
    return counter                               # the counter is returned at the end with the number of rows in the data set

def sum(x):                                      # sum(x) is a function that takes an argument of 'x' and then returns the sum of the values in column 'x'
  with open("data/iris.csv", "r") as myfile:       # this statement opens the iris data set as an object called myfile                  
    sums = 0                                     # this initialises a variable that will used to store the values of the sum
    for line in myfile:                          # this loop run through the rows of the file one a a time
      rows = line.split(',')[0:5]                # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      sums = sums + float(rows[x])               # on each pass through the loop sums is incremented with the float value of the line for the column specified by 'x'
    return sums                                  # the final value of the sum is returned with the summation of all values in the specified column

def mean(x):                                     # mean(x) takes a value x and returns the mean of the column x 
  average = sum(x)/count()                       # the functions that are already declared can be used to calculate the average 
  return average

print(sum(0))
print(sum(1))
print(sum(2))
print(sum(3))

print(mean(0))
print(mean(1))
print(mean(2))
print(mean(3))


print(count())    