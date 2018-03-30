# Patrick Moore 2018-03-26
# This file contains a Python script to form part of my 2018 project for the Progamming and Scripting Module of the H.DIP in Data Analytics
# Iris Analyser is the script used to analyse the iris data set
# Iris Data Set - (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
# Reference for the problem - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) fromt the Python Tutorial

# Section 1 - Functions - In this section of the project, the functions used to analyse the data are defined

def count():                                     # count() is a function that will count the number of rows in the data file
  with open("data/iris.csv", "r") as myfile:     # this statement opens the iris data set as an object called myfile
    counter = 0                                  # this initialises a variable that will used to store the values of the count
    for line in myfile:                          # this loop run through the rows of the file one at a time
      counter = counter + 1                      # for each pass through the loop the counter is incremented by one
    return counter                               # the counter is returned at the end with the number of rows in the data set

def sum(x):                                      # sum(x) is a function that takes an argument of 'x' and then returns the sum of the values in column 'x'
  with open("data/iris.csv", "r") as myfile:     # this statement opens the iris data set as an object called myfile                  
    sums = 0                                     # this initialises a variable that will used to store the values of the sum
    for line in myfile:                          # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      sums = sums + float(rows[x])               # on each pass through the loop sums is incremented with the float value of the line for the column specified by 'x'
    return sums                                  # the final value of the sum is returned with the summation of all values in the specified column

def mean(x):                                     # mean(x) takes a value x and returns the mean of the column x 
  average = sum(x)/count()                       # the functions that are already declared can be used to calculate the average 
  return average

def max(x):                                       # max(x) is a function that takes an argument of 'x' and then returns the maximum value in column 'x'
  with open("data/iris.csv", "r") as myfile:      # this statement opens the iris data set as an object called myfile                   
    maximum = 0                                   # this initialises a variable that will used to store the maximum value in column 'x'
    for line in myfile:                           # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                 # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if float(rows[x]) > maximum:                # on each pass through the loop the value is checked to see if it is greater than 'maximum'
        maximum = float(rows[x])                  # if it is greater than 'maximum' then 'maximum' will be set to that value
    return maximum                                # the final value of 'maximum' is returned

def min(x):                                       # min(x) is a function that takes an argument of 'x' and then returns the minimum value in column 'x'
  with open("data/iris.csv", "r") as myfile:      # this statement opens the iris data set as an object called myfile                           
    minimum = 10                                  # this initialises a variable that will used to store the maximum value in column 'x' (value can't be 0 to start otherwise it will not change in the for loop)
    for line in myfile:                           # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                 # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if float(rows[x]) < minimum:                # on each pass through the loop the value is checked to see if it is less than 'minimum'
        minimum = float(rows[x])                  # if it is less than 'minimum' then 'minimum' will be set to that value
    return minimum                                # the final value of 'minimum' is returned

def stddev(x):                                    # stddev(x) is a function that takes an argument of 'x' and then returns the standard deviation of the data in column 'x'
  with open("data/iris.csv", "r") as myfile:      # this statement opens the iris data set as an object called myfile
    devsq = 0                                     # this initialises a variable that will used to store the "deviations from the mean"
    for line in myfile:                           # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                 # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      devsq = devsq + (mean(x) - float(rows[x]))**2 # on each pass through the loop devsq is incremented by the value of the 'deviation from the mean' squared
    sig = (devsq/count())**0.5                    # sig is the standard deviation calulated by getting the square root of the average of 'devsq'
    return sig                                    # this calculation for sig is returned

# Section 2 - Data Summary - In this section of the project, the functions are used to summarise the data
summary = [['Statistic', 'Sepal Lenght (cm)', 'Sepal Width (cm)', 'Petal Lenght (cm)','Petal Width'],
           ['Sum', round(sum(0),2),round(sum(1),2), round(sum(2),2), round(sum(3),2)],
           ['Max', round(max(0),2), round(max(1),2), round(max(2),2), round(max(3),2)],
           ['Min', round(min(0),2), round(min(1),2), round(min(2),2), round(min(3),2)],
           ['Mean', round(mean(0),2), round(mean(1),2), round(mean(2),2), round(mean(3),2)],
           ['Std Dev', round(stddev(0),2), round(stddev(1),2), round(stddev(2),2), round(stddev(3),2)]
          ]

# Section 3 - Graphics - In this section of the project, some graphics will created

# Section 4 - User Interface - In this section of the project a user interface will be created
print(round(stddev(0),2))
print(round(stddev(1),2))
print(round(stddev(2),2))
print(round(stddev(3),2))
print(summary)