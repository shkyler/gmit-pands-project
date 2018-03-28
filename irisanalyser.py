# Patrick Moore 2018-03-26
# This file contains a Python script to form part of my 2018 project for the Progamminf and Scripting Module of the H.DIP in Data Analytics
# Iris Analyser is the script used to analyse the iris data set
# Iris Data Set - (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
# Reference for the problem - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) fromt the Python Tutorial

# Section 1 - Functions - In this section of the project, the functions used to analyse the data are defined

def count():                                   # count is a function that will count the number of rows in the data file
  with open("data/iris.csv", "r") as myfile:   # this statement opens the iris data set as an object called myfile
    counter = 0                                # this initialises a variable that will used to store the values of the count
    for line in myfile:                        # this loop run through the rows of the file one a a time
      counter = counter + 1                    # for each pass through the loop the counter is incremented by one
    return counter                             # the counter is returned at the end with the number of rows in the data set

print(count())    