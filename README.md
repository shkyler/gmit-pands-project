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
The Iris data set is a set of data containing information about iris flowers. The data contains 150 diferent data points. For each data point there are 5 pieces of information. These are [3]:
1. The sepal lenght in cms
1. The sepal width in cms
1. The petal lenght in cms
1. The petal width in cms
1. The class (Iris Setosa, Iris Verticolour or Iris Virginica)

The class represents the species of the iris flower and in the set there are 50 points for each of the 3 iris species. The data set is a multivariate data set as it involves data with more than one measurement taken at a time [4]. It is commonly called "Fishers Iris Data Set" as it was published in the 1936 paper "_The use of multiple measurements in taxonomic problems_". It is also known as "Andersons Iris Data Set" as the data was originally collected by American botanist Edgar Anderson while working on a study of the physical differences between 3 related species of iris flower. Fisher used the data set as an example of _linear discriminate analysis_[9], and it is now commonly used as a typical test case in many statistical classification techniques (see section 2.3).

### 2.2 Edgar Anderson and Ronald Fisher
![Anderson](/img/Anderson.jpg)

Edgar Anderson was an American botanist who lived in the early part of the 20th century[5]. In the 1920s, while working as assistant professor of botany at Washington University in St. Louis his main area of research centered around the development of techniques to quantify geographical  difference in the iris versicolor. In 1929 he obtained a fellowship to study at the John Innes Horticultural Institute in Britain, where he worked with Ronald Fisher. Anderson collected the iris data set himself and in fact "_two of the three species were collected in the Gaspé Peninsula, all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus_"[6].

![Fisher](/img/Fisher.jpg)

Ronald Fisher was a contemporary of Anderson. In addition to being the greatest statistician ever, he invented experimental design and was a principal founder of population genetics [7]. 
In 1925, he released his book "_Statistical Methods for Research Workers_" which soon revolutionise both statistics and biology. In fact, he has been described as "_a genius who almost single-handedly created the foundations for modern statistical science_" [8].

### 2.3 The Purpose of Linear Discriminant Analysis (LDA) [9]
The purpose of LDA is to classify objects into groups based on a set of features that describe the objects. In general, an object is placed into one of a number of predetermined groups based on the outcome of some obsertvations made on that object. In order to classify items properly the following must be decided:
1. Which set of features best describes membership of each group?
1. What model should be used to seperate the groups?

Applying this description to the iris data set - the groups would be the 3 iris species (Iris Setosa, Iris Verticolour or Iris Virginica), the set of features would be the petal lenght, petal width, sepal lenght and sepal width. The linear discriminant model is one model that can be used to seperate the groups. 

Another method of classifying or grouping data points is _cluster analysis_. This method involves creating a scatter plot of data and then looking to see do any of the data points cluster together which may indicate membership of a particular group. With cluster analysis the groups are unknown at the start and would have to be determined by the analysis. The iris data set is generally not used in cluster analysis as there are only 2 groupings seen in the analysis. Futhermore it is not possible to seperate Iris Virginia from Iris Versicolour without having the species data in advance[2].

### 2.4 Popularity of the Iris set in Teaching and Study

## 3. My Code
### 3.1 What it does
### 3.2 How to use it
### 3.3 Results obtained from the analysis with some graphics if possible
### 3.4 Discussion of the results

## References
1. [1] Dr. Ian McLoughlin. GMIT. Instructions: Project 2018 (_https://learnonline.gmit.ie/mod/url/view.php?id=199458_)
1. [2] Wikipedia. Iris flower data set (_https://en.wikipedia.org/wiki/Iris_flower_data_set_)
1. [3] UC Irvine Machine Learning Repository. Iris plants database. )(_http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names_)
1. [4] Wikipedia. Multivariate statistics (_https://en.wikipedia.org/wiki/Multivariate_statistics_)
1. [5] Wikipedia. Edgar Anderson (_https://en.wikipedia.org/wiki/Edgar_Anderson_)
1. [6] Edgar Anderson (1935). "_The irises of the Gaspé Peninsula_"
1. [7] Famous Scietists. Ronald Fisher. (_https://www.famousscientists.org/ronald-fisher_)
1. [8] Anders Hald (1998). (_A History of Mathematical Statistics._)
1. [9] Linear Discriminate Analysis (LDA).(_http://people.revoledu.com/kardi/tutorial/LDA/LDA.htm_l)

