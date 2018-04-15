![GMIT Logo](/img/GMITLOGO.jpg)
# GMIT, H.Dip in Data Analytics, Progamming and Scripting Project 2018
## 1. Introduction
This repository contains all of the files pertaining to my 2018 project submission for the Programming and Scripting module of the GMIT H.Dip program in Data Analytics. All of the work within this repository was carried out over the course of a 5 week period in March and April 2018. This README contains the complete documentation for the project. 
### 1.1 Project Objective
The objective of this project is to carryout some research into "Fishers Iris Data Set" (this will help in the understanding of the backgroud of the data set). The next step is to use the Python programming language to write a script to summarise the data. The summary data is then to be analysed and discussed. The problem statement for the project is as follows[1]:
1. Research background information about the data set and write a summary about it.
1. Keep a list of references you used in completing the project.
1. Download the data set and write some Python code to investigate it.
1. Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.
1. Write a summary of your investigations.
1. Include supporting tables and graphics as you deem necessary.

## 2. The Iris Data Set Background
### 2.1 The Iris Data Set [2]
The Iris data set is a set of data containing information about iris flowers. The data contains 150 different data points. For each data point there are 5 pieces of information. These are [3]:
1. The sepal lenght in cms
1. The sepal width in cms
1. The petal lenght in cms
1. The petal width in cms
1. The class (Iris Setosa, Iris Verticolour or Iris Virginica)

The class represents the species of the iris flower and in the set there are 50 points for each of the 3 iris species. The data set is a multivariate data set as it involves data points with more than one measurement taken at a time [4]. It is commonly called "Fishers Iris Data Set" as it was published in the 1936 paper "_The use of multiple measurements in taxonomic problems_". It is also known as "Andersons Iris Data Set" as the data was originally collected by American botanist Edgar Anderson while working on a study of the physical differences between 3 related species of iris flower. Fisher used the data set as an example of _linear discriminate analysis_[9], and it is now commonly used as a typical test case in many statistical classification techniques (see section 2.3).

### 2.2 Edgar Anderson and Ronald Fisher
![Anderson](/img/Anderson.jpg)

Edgar Anderson was an American botanist who lived in the early part of the 20th century[5]. In the 1920s, while working as assistant professor of botany at Washington University in St. Louis his main area of research centered around the development of techniques to quantify geographical  difference in the iris versicolor. In 1929 he obtained a fellowship to study at the John Innes Horticultural Institute in Britain, where he worked with Ronald Fisher. Anderson collected the iris data set himself and in fact "_two of the three species were collected in the Gaspé Peninsula, all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus_"[6].

![Fisher](/img/Fisher.jpg)

Ronald Fisher was a contemporary of Anderson. In addition to being probably the greatest statistician ever, he invented experimental design and was a principal founder of population genetics [7]. 
In 1925, he released his book "_Statistical Methods for Research Workers_" which soon revolutionised both statistics and biology. In fact, he has been described as "_a genius who almost single-handedly created the foundations for modern statistical science_" [8].

### 2.3 The Purpose of Linear Discriminant Analysis (LDA) [9]
The purpose of LDA is to classify objects into groups based on a set of features that describe the objects. In general, an object is placed into one of a number of predetermined groups based on the outcome of some obsertvations made on that object. In order to classify items properly the following must be decided:
1. Which set of features best describes membership of each group?
1. What model should be used to seperate the groups?

Applying this description to the iris data set - the groups would be the 3 iris species (Iris Setosa, Iris Verticolour or Iris Virginica), the set of features would be the petal lenght, petal width, sepal lenght and sepal width. The linear discriminant model is one model that can be used to seperate the groups. 

Another method of classifying or grouping data points is _cluster analysis_. This method involves creating a scatter plot of data and then looking to see do any of the data points cluster together which may indicate membership of a particular group. With cluster analysis the groups are unknown at the start and would have to be determined by the analysis. The iris data set is generally not used in cluster analysis as there are only 2 groupings seen in the analysis. Futhermore it is not possible to seperate Iris Virginia from Iris Versicolour without having the species data in advance[2].

### 2.4 Popularity of the Iris set in teaching and study
While carrying out research into the iris data set it quickly became apparent that this data set is ubiquitous across the internet. Most of the sites were linked to education and training. Other uses of the data were by data analysis software companies who use the data set in their promotional material. The reasons for it's popularity are best summed up as follows [10]:

1. _Containing 150 observations, it is small but not trivial._

1. _The task it poses of discriminating between three species of Iris from measurements of their petals and sepals is simple but challenging._

1. _The data are real data, but apparently of good quality. In principle and in practice, test datasets could be synthetic and that might be necessary or useful to make a point. Nevertheless, few people object to real data._

1. _The data were used by the celebrated British statistician Ronald Fisher in 1936. (Later he was knighted and became Sir Ronald.) At least some teachers like the idea of a dataset with a link to someone so well known within the field. The data were originally published by the statistically-minded botanist Edgar S. Anderson, but that earlier origin does not diminish the association._

1. _Using a few famous datasets is one of the traditions we hand down, such as telling each new generation that Student worked for Guinness. Using a few test datasets affords some continuty in now new test methods are assessed._

## 3. The Iris Analyser
The Iris Analyser id a piece of software written in the Python [11] programming language which can be used to carry out analysis of the iris data set. The entire program was written as part of this project. This section of the README will look first at the code in the analyser and then explain how to run the program and use it analyse the iris data set.
### 3.1 Description of the code in irisanalyser.py
The irisanalyser.py script has over 300 lines of code in it, so to make it easier to read it has been split into four main sections using comments in the code. These will be explained one at a time.
#### 3.1.1 - Section 1 - Basic Statistical Functions
In this section of the code, some functions that are used to calculate some basic statistics about the data are defined. While it is possible to use some of the built in functions in the numpy library, it was decided that it might be more challenging to try to create some of these functions from scrath as part of this research and learning exercise. These functions are as follows:

_**count(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). It will then go through the data set looking at the column indexed by 'x'. The 'type' refers to the class of iris that is to be analysed. If type is 'all' it will look at the whole data set, otherwise one of the 3 iris species can be passed and it will only consider that particular species. The function will return a 'count' f the required data as specified by the arguments passed.

_**sum(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). It will then go through the data set looking at the column indexed by 'x'. The 'type' refers to the class of iris that is to be analysed. If type is 'all' it will look at the whole data set, otherwise one of the 3 iris species can be passed and it will only consider that particular species. The function will return a 'sum' of the required data as specified by the arguments passed.

_**mean(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). As before, 'x' refers to the data column index and 'type' refers to the species. It then calls the sum() and count() functions and uses them to calulate the mean of the data as specified by the arguments passed.

_**max(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). It will then go through the data set looking at the column indexed by 'x'. The 'type' refers to the class of iris that is to be analysed. If type is 'all' it will look at the whole data set, otherwise one of the 3 iris species can be passed and it will only consider that particular species. The function will return the maximum value of the required data as specified by the arguments passed.

_**min(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). It will then go through the data set looking at the column indexed by 'x'. The 'type' refers to the class of iris that is to be analysed. If type is 'all' it will look at the whole data set, otherwise one of the 3 iris species can be passed and it will only consider that particular species. The function will return the minimum value of the required data as specified by the arguments passed. (note that this function calls the max() function to use as the initial value of the minimum - if 0 is used, none of the data values in the data set will be below it, so it will erroneously return 0 as the minimum)

_**stddev(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). It will then go through the data set looking at the column indexed by 'x'. The 'type' refers to the class of iris that is to be analysed. If type is 'all' it will look at the whole data set, otherwise one of the 3 iris species can be passed and it will only consider that particular species. The function will return the standard deviation[12] of the required data as specified by the arguments passed. The algorithm was designed around the definitions on the wikipedia page.

_**datacolumn(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). It will then go through the data set looking at the column indexed by 'x'. The 'type' refers to the class of iris that is to be analysed. If type is 'all' it will look at the whole data set, otherwise one of the 3 iris species can be passed and it will only consider that particular species. The function will return an array containing the data values from the species and data column specified by the arguments - this function is useful for graphical analysis of the data.

#### 3.1.2 - Section 2 - Data Summary
In this section of the code, the functions from Section 1 are used to define some data summaries of each data column. Four data summaries are defined as follows:

_**summaryall**_ is an array which contains the sum, maximum value, minimum value, mean and standard deviation for each of the four columns in the data set. It summarises data for all 150 data points in the data set.

_**summarysetosa**_ is an array which contains the sum, maximum value, minimum value, mean and standard deviation for each of the four columns in the data set. It summarises data for the 50 Iris-setosa data points in the data set.

_**summaryversicolor**_ is an array which contains the sum, maximum value, minimum value, mean and standard deviation for each of the four columns in the data set. It summarises data for the 50 Iris-versicolor data points in the data set.

_**summaryvirginica**_ is an array which contains the sum, maximum value, minimum value, mean and standard deviation for each of the four columns in the data set. It summarises data for the 50 Iris-virginica data points in the data set.

_**printsummary(data0**_ is a function that takes one of the four data summaries as an argument and prints it to the colsole in a neat formatted grid[13].

### 3.2 How to use it

## 4. Analysis of the Iris Data Set
### 4.1 Results
### 4.2 Discussion

## References
1. [1] Dr. Ian McLoughlin. GMIT. Instructions: Project 2018 (_https://learnonline.gmit.ie/mod/url/view.php?id=199458_)
1. [2] Wikipedia. Iris flower data set (_https://en.wikipedia.org/wiki/Iris_flower_data_set_)
1. [3] UC Irvine Machine Learning Repository. Iris plants database. )(_http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names_)
1. [4] Wikipedia. Multivariate statistics (_https://en.wikipedia.org/wiki/Multivariate_statistics_)
1. [5] Wikipedia. Edgar Anderson (_https://en.wikipedia.org/wiki/Edgar_Anderson_)
1. [6] Edgar Anderson (1935). "_The irises of the Gaspé Peninsula_"
1. [7] Famous Scientists. Ronald Fisher. (_https://www.famousscientists.org/ronald-fisher_)
1. [8] Anders Hald (1998). (_A History of Mathematical Statistics._)
1. [9] Linear Discriminate Analysis (LDA).(_http://people.revoledu.com/kardi/tutorial/LDA/LDA.htm_l)
1. [10] Stack Exchange. "What aspects of the “Iris” data set make it so successful as an example/teaching/test data set" (_https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching_)
1. [11] Python Software Foundation. Welcome to Python. (_https://www.python.org/_)
1. [12] Wikipedia. Standard Deviation (_https://en.wikipedia.org/wiki/Standard_deviation_)
1. [13] Stack Overflow. Create nice column output in python. (_https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python_)

