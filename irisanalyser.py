# Patrick Moore 2018-03-26
# This file contains a Python script to form part of my 2018 project for the Progamming and Scripting Module of the H.DIP in Data Analytics
# Iris Analyser is the script used to analyse the iris data set
# Iris Data Set - (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
# Reference for the problem - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) fromt the Python Tutorial

# Section 1 - Functions - In this section of the project, the functions used to analyse the data are defined

def count(x,type):                                            # count(x,type) is a function that will count the number of rows in a particular data column, depending on the species of iris entered
  with open("data/iris.csv", "r") as myfile:                  # this statement opens the iris data set as an object called myfile
    counter = 0                                               # this initialises a variable that will used to store the values of the count
    for line in myfile:                                       # this loop runs through the rows of the file one at a time
      rows = line.split(',')[0:5]                             # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if type == 'all':                                       # if 'all' is passed as an argument, the loop will count all rows in the column
        counter = counter + 1                      
      else:                                                   # otherwise the 5th column in the dataset is checked for the species that has been passed
        if type in rows[4]:                               
          counter = counter + 1                               # this will count the number of the rows which have the entered species in them
    return counter                                            # the counter is returned at the end with the number of rows in the data column that are for the desired variety

def sum(x,type):                                              # sum(x) is a function that takes an argument of 'x' and then returns the sum of the values in column 'x' based on the secies entered as 'type'
  with open("data/iris.csv", "r") as myfile:                  # this statement opens the iris data set as an object called myfile                  
    sums = 0                                                  # this initialises a variable that will used to store the values of the sum
    for line in myfile:                                       # this loop runs through the rows of the file one at a time
      rows = line.split(',')[0:5]                             # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if type == 'all':                                       # if 'all' is passed as an argument, the loop will sum all values in the specified column
       sums = sums + float(rows[x])
      else:                                                   # otherwise the 5th column in the dataset is checked for the species that has been passed
        if type in rows[4]:                                   # this will sum the values in the rows which have the entered species in them 
          sums = sums + float(rows[x])                        # on each pass through the loop sums is incremented with the float value of the line for the column specified by 'x'
    return sums                                               # the final value of the sum is returned with the summation of all values in the specified column, with the specified species

def mean(x,type):                                             # mean(x,type) takes a value x and a variety and returns the mean of the column x depending on the iris species specified
  average = sum(x,type)/count(x,type)                         # the functions that are already declared can be used to calculate the average 
  return average

def max(x,type):                                              # max(x) is a function that takes an argument of 'x' and then returns the maximum value in column 'x' for the specified species
  with open("data/iris.csv", "r") as myfile:                  # this statement opens the iris data set as an object called myfile                   
    maximum = 0                                               # this initialises a variable that will used to store the maximum value in column 'x' as the program loops
    for line in myfile:                                       # this loops run through the rows of the file one at a time
      rows = line.split(',')[0:5]                             # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if type == 'all':                                       # if the type is set to 'all', it will check the whole column
        if float(rows[x]) > maximum:                          # on each pass through the loop the value is checked to see if it is greater than 'maximum'
          maximum = float(rows[x])                            # if it is greater than 'maximum' then 'maximum' will be set to that value
      else:                                                   # otherwise the 'type' is checked in column 4 and it will look for the maximum value for the specified 'type'
        if type in rows[4]:
          if float(rows[x]) > maximum:
            maximum = float(rows[x])
    return maximum                                            # the final value of 'maximum' is returned

def min(x,type):                                              # min(x) is a function that takes an argument of 'x' and then returns the minimum value in column 'x' for the specified iris species
  with open("data/iris.csv", "r") as myfile:                  # this statement opens the iris data set as an object called myfile                           
    minimum = max(x,type)                                     # this initialises a variable that will used to store the maximum value in column 'x' (value is initially set to the maximum so that the loop will find all the lower values)
    for line in myfile:                                       # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                             # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if type == 'all':                                       # if the type is set to 'all', it will check the whole column
        if float(rows[x]) < minimum:                          # on each pass through the loop the value is checked to see if it is less than 'minimum'
          minimum = float(rows[x])                            # if it is less than 'minimum' then 'minimum' will be set to that value
      else:                                                   # otherwise the 'type' is checked in column 4 and it will look for the minimum value for the specified 'type'
        if type in rows[4]: 
          if float(rows[x]) < minimum:
            minimum = float(rows[x])
    return minimum                                            # the final value of 'minimum' is returned

def stddev(x,type):                                           # stddev(x) is a function that takes an argument of 'x' and then returns the standard deviation of the data in column 'x' for a specified iris type
  with open("data/iris.csv", "r") as myfile:                  # this statement opens the iris data set as an object called myfile
    devsq = 0                                                 # this initialises a variable that will used to store the "deviations from the mean"
    for line in myfile:                                       # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                             # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if type == 'all':                                       # if the type is set to 'all' the sum of devsq is calculated for the whole column 
        devsq = devsq + (mean(x,type) - float(rows[x]))**2    # on each pass through the loop devsq is incremented by the value of the 'deviation from the mean' squared
      else:                                                   # otherwise the 'type' is checked in column 4 and it will increment devsq for the columns with the specified iris type
        if type in rows[4]:
          devsq = devsq + (mean(x,type) - float(rows[x]))**2  
    sig = (devsq/count(x,type))**0.5                          # sig is the standard deviation calulated by getting the square root of the average of 'devsq'
    return sig                                                # this calculation for sig is returned

def datacolumn(x,type):                                       # datacolumn() is a fuction that takes an argument 'x' and then returns a list of the data in column 'x' for a specified iris species
  with open("data/iris.csv", "r") as myfile:                  # this statement opens the iris data set as an object called myfile                  
    values = []                                               # this initialises a list variable that will used to store the values of column 'x'
    for line in myfile:                                       # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]                             # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
      if type == 'all':                                       # if the type is set to 'all' - 'values' will be appended with the values of the whole column in order
        values.append(float(rows[x]))
      else:                                                   # otherwise the 'type' is checked in column 4 and it will only append 'values' with the values from the specified iris type
        if type in rows[4]:                
          values.append(float(rows[x]))               
    return values                                             # the final list of values is returned

# Section 2 - Data Summary - In this section of the project, the functions and data structures that are used to summarise the data are defined. All the data is formatted to 2 decimal places and converted to strings to improve printing

summaryall = [[' ', 'Sepal Lenght (cm)', 'Sepal Width (cm)', 'Petal Lenght (cm)','Petal Width (cm)'],                                                     # summaryall summarises the data for all species of iris into one list
              ['Sum', str(round(sum(0,'all'),2)), str(round(sum(1,'all'),2)), str(round(sum(2,'all'),2)), str(round(sum(3,'all'),2))],
              ['Max', str(round(max(0,'all'),2)), str(round(max(1,'all'),2)), str(round(max(2,'all'),2)), str(round(max(3,'all'),2))],
              ['Min', str(round(min(0,'all'),2)), str(round(min(1,'all'),2)), str(round(min(2,'all'),2)), str(round(min(3,'all'),2))],
              ['Mean', str(round(mean(0,'all'),2)), str(round(mean(1,'all'),2)), str(round(mean(2,'all'),2)), str(round(mean(3,'all'),2))],
              ['Std Dev', str(round(stddev(0,'all'),2)), str(round(stddev(1,'all'),2)), str(round(stddev(2,'all'),2)), str(round(stddev(3,'all'),2))]
             ]

summarysetosa = [[' ', 'Sepal Lenght (cm)', 'Sepal Width (cm)', 'Petal Lenght (cm)','Petal Width (cm)'],                                                     # summarysetosa summarises the data for iris-setosa into one list
                ['Sum', str(round(sum(0,'setosa'),2)), str(round(sum(1,'setosa'),2)), str(round(sum(2,'setosa'),2)), str(round(sum(3,'setosa'),2))],
                ['Max', str(round(max(0,'setosa'),2)), str(round(max(1,'setosa'),2)), str(round(max(2,'setosa'),2)), str(round(max(3,'setosa'),2))],
                ['Min', str(round(min(0,'setosa'),2)), str(round(min(1,'setosa'),2)), str(round(min(2,'setosa'),2)), str(round(min(3,'setosa'),2))],
                ['Mean', str(round(mean(0,'setosa'),2)), str(round(mean(1,'setosa'),2)), str(round(mean(2,'setosa'),2)), str(round(mean(3,'setosa'),2))],
                ['Std Dev', str(round(stddev(0,'setosa'),2)), str(round(stddev(1,'setosa'),2)), str(round(stddev(2,'setosa'),2)), str(round(stddev(3,'setosa'),2))]
                ]

summaryversicolor = [[' ', 'Sepal Lenght (cm)', 'Sepal Width (cm)', 'Petal Lenght (cm)','Petal Width (cm)'],                                                     # summaryversicolor summarises the data for iris-versicolor into one list
                    ['Sum', str(round(sum(0,'versicolor'),2)), str(round(sum(1,'versicolor'),2)), str(round(sum(2,'versicolor'),2)), str(round(sum(3,'versicolor'),2))],
                    ['Max', str(round(max(0,'versicolor'),2)), str(round(max(1,'versicolor'),2)), str(round(max(2,'versicolor'),2)), str(round(max(3,'versicolor'),2))],
                    ['Min', str(round(min(0,'versicolor'),2)), str(round(min(1,'versicolor'),2)), str(round(min(2,'versicolor'),2)), str(round(min(3,'versicolor'),2))],
                    ['Mean', str(round(mean(0,'versicolor'),2)), str(round(mean(1,'versicolor'),2)), str(round(mean(2,'versicolor'),2)), str(round(mean(3,'versicolor'),2))],
                    ['Std Dev', str(round(stddev(0,'versicolor'),2)), str(round(stddev(1,'versicolor'),2)), str(round(stddev(2,'versicolor'),2)), str(round(stddev(3,'versicolor'),2))]
                    ]

summaryvirginica = [[' ', 'Sepal Lenght (cm)', 'Sepal Width (cm)', 'Petal Lenght (cm)','Petal Width (cm)'],                                                     # summaryvirginica summarises the data for iris-virginica into one list
                    ['Sum', str(round(sum(0,'virginica'),2)), str(round(sum(1,'virginica'),2)), str(round(sum(2,'virginica'),2)), str(round(sum(3,'virginica'),2))],
                    ['Max', str(round(max(0,'virginica'),2)), str(round(max(1,'virginica'),2)), str(round(max(2,'virginica'),2)), str(round(max(3,'virginica'),2))],
                    ['Min', str(round(min(0,'virginica'),2)), str(round(min(1,'virginica'),2)), str(round(min(2,'virginica'),2)), str(round(min(3,'virginica'),2))],
                    ['Mean', str(round(mean(0,'virginica'),2)), str(round(mean(1,'virginica'),2)), str(round(mean(2,'virginica'),2)), str(round(mean(3,'virginica'),2))],
                    ['Std Dev', str(round(stddev(0,'virginica'),2)), str(round(stddev(1,'virginica'),2)), str(round(stddev(2,'virginica'),2)), str(round(stddev(3,'virginica'),2))]
                    ]

def printsummary(data):                                       # I researched how to format the out put here https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python 
  colwidth = 18                                               # 'printsummary' takes a list as an argument  
  for row in data:                                            # it loops through each row in the list   
    print("".join(cell.ljust(colwidth) for cell in row))      # it prints each item in the row, left justified and formatted to the column width specified

#printsummary(summaryall)
#printsummary(summarysetosa)
#printsummary(summaryversicolor)
#printsummary(summaryvirginica)      
#import numpy as np
#print(np.matrix(summary))

# Section 3 - Graphics - In this section of the project, some graphics functions will created

def scatter(x,y,type):                                                              # scatter is a function that uses matplotlib to create a scatter plot of the data, x and y are list vlaues to be plotted on the x and y axes, type is the species of iris
  import matplotlib.pyplot as plt                                                   # this statement imports the matplotlib library (REF: https://matplotlib.org/2.2.2/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter)
  columnnames = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']      # this is a list of the data column names in the order they appear in the data set
  if type == 'setosa':                                                              # if type is 'setosa' it will plot the corresponding x and y values by calling the datacolumn() function for the 'setosa' items
    plt.scatter(datacolumn(x,'setosa'),datacolumn(y,'setosa'), c='red')
  elif type == 'versicolor':                                                        # if type is 'versicolor' it will plot the corresponding x and y values by calling the datacolumn() function for the 'versicolor' items
    plt.scatter(datacolumn(x,'versicolor'),datacolumn(y,'versicolor'), c='blue')
  elif type == 'virginica':                                                         # if type is 'virginica' it will plot the corresponding x and y values by calling the datacolumn() function for the 'virginica' items
    plt.scatter(datacolumn(x,'virginica'),datacolumn(y,'virginica'), c='green')
  elif type == 'all':                                                               # if type is 'all' it will plot the corresponding x and y values by calling the datacolumn() function for all items - each set will be coloured differently
    plt.scatter(datacolumn(x,'setosa'),datacolumn(y,'setosa'), c='red')
    plt.scatter(datacolumn(x,'versicolor'),datacolumn(y,'versicolor'), c='blue')
    plt.scatter(datacolumn(x,'virginica'),datacolumn(y,'virginica'), c='green')
  elif type == 'allsame':
    plt.scatter(datacolumn(x,'setosa'),datacolumn(y,'setosa'), c='blue')            # if type is 'all' it will plot the corresponding x and y values by calling the datacolumn() function for all items - each set will be coloured the same (blue)
    plt.scatter(datacolumn(x,'versicolor'),datacolumn(y,'versicolor'), c='blue')
    plt.scatter(datacolumn(x,'virginica'),datacolumn(y,'virginica'), c='blue')  
  plt.title(columnnames[y] + ' vs. ' + columnnames[x])                              # title will be given by looking up the 'columnnames' list
  plt.ylim([0,10])                                                                  # both x any y axes set in the range 0 to 10
  plt.xlim([0,10])
  plt.xlabel(columnnames[x])                                                        # x and y axis labels given by looking up the 'columnnames' list
  plt.ylabel(columnnames[y])
  plt.grid(True)                                                                    # this command puts a grid on the background of the plot area
  plt.show()                                                                        # this command shows the plot

scatter(2,3,'versicolor')

# Section 4 - User Interface - In this section of the project a user interface will be created
#print(round(stddev(0),2))
#print(round(stddev(1),2))
#print(round(stddev(2),2))
#print(round(stddev(3),2))
#print(summary)

#print(count(0,'all'))
#print(count(0,'setosa'))
#print(count(0,'versicolor'))
#print(count(0,'virginica'))

#print(round(sum(0,'setosa'),2))
#print(round(sum(0,'versicolor'),2))
#print(round(sum(0,'virginica'),2))
#print(round(sum(0,'all'),2))

#print(round(mean(0,'setosa'),2))
#print(round(mean(0,'versicolor'),2))
#print(round(mean(0,'virginica'),2))
#print(round(mean(0,'all'),2))

#print(round(max(0,'setosa'),2))
#print(round(max(0,'versicolor'),2))
#print(round(max(0,'virginica'),2))
#print(round(max(0,'all'),2))

#print(round(min(0,'setosa'),2))
#print(round(min(0,'versicolor'),2))
#print(round(min(0,'virginica'),2))
#print(round(min(0,'all'),2))

#print(round(stddev(0,'setosa'),2))
#print(round(stddev(0,'versicolor'),2))
#print(round(stddev(0,'virginica'),2))
#print(round(stddev(0,'all'),2))