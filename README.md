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
1. The sepal length in cms
1. The sepal width in cms
1. The petal length in cms
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

1. _Using a few famous datasets is one of the traditions we hand down, such as telling each new generation that Student (William Sealy Gosset) worked for Guinness. Using a few test datasets affords some continuty in now new test methods are assessed._

## 3. The Iris Analyser
The Iris Analyser is a piece of software written in the Python [11] programming language which can be used to carry out analysis of the iris data set. The entire program was written as part of this project. This section of the README will look first at the code in the analyser and then explain how to run the program and use it analyse the iris data set.
### 3.1 Description of the code in irisanalyser.py
The irisanalyser.py script has over 300 lines of code in it, so to make it easier to read it has been split into four main sections using comments in the code. These will be explained one at a time.
#### 3.1.1 - Section 1 - Basic Statistical Functions
In this section of the code, some functions that are used to calculate some basic statistics about the data are defined. While it is possible to use some of the built in functions in the numpy library, it was decided that it might be more challenging to try to create some of these functions from scratch as part of this research and learning exercise. These functions are as follows:

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

_**printsummary(data)**_ is a function that takes one of the four data summaries as an argument and prints it to the colsole in a neatly formatted grid[13].

#### 3.1.3 - Section 3 - Graphics
In this section of the code, the functions for creating graphical plots of the data are defined. The matplotlib library [14] is used here. Functions are included for creating three different graph types. These are the scatter plot, the histogram and the normal distribtion. These functions are described below:

_**scatter(x,y,type):**_ This is a function that takes 3 arguments(x is an int,y is an int, type is a string). 'type' is representative of the species. Depending on the type entered, this function will create a scatter plot by calling the datacolumn() function for the columns specified by 'x' and 'y'.[15]

_**histogram(y,type):**_ This is a function that takes 2 arguments(y is an int, type is a string). 'type' is representative of the species. Depending on the type entered, this function will create a histogram plot by calling the datacolumn() function for the column specified by 'y'. [16]

_**normdist(x,type):**_ This is a function that takes 2 arguments(x is an int, type is a string). 'type' is representative of the species. Depending on the type entered, this function will create a normal distribution curve by calling the datacolumn() function for the column specified by 'x'. [17]

#### 3.1.4 - Section 4 - User Interface
The user interface is the part of the software that the user will interact with. It will asks questions of the user in order to get the required details. It will then use these user inputs to create the outputs required and return them to the user. There are 3 main parts to the user interface:

_**The Splash Screen**_ When the program is first run this is what is printed to the terminal. It serves as a home screen. From here the user can decide to either analyse data, see the help file or quit the program.

_**help():**_ This is a very simple function that prints out a list of commands that can be accepted by the program, ordered by the various screens in the program. It can only be run from the splash screen and once it is run it will automatically start up a new analysis session.

_**session():**_ THis is a function used to manage an analysis sesssion. It asks the user for the information that is used to decide what outputs are required. Note that all user inputs are controlled by using a while loop. If the user tries to enter invalid data - the while loop will keep asking until a valid input is entered(this lesson was learned when programming a Rock, Paper Scissors game [18]). Once the program has returned the data or graph as specified by the user, the session() function will ask if more analysis is required. From here the user can either quit the program or start another session.

### 3.2 Instructions for using the Iris Analyser
#### 3.2.1 Cloning the repository
You can clone the following repository from Github by typing the following command:

```git clone https://github.com/shkyler/gmit-pands-project```

In order for the program to run successfully, the iris data set must be stored in a file named 'iris.csv' with the columns arranged in the order as described in Section 2.1 of this README file. This .csv file must be stored in a directory called 'data', and this 'data' folder must be located in the same directory as the 'irisanalyser.py' script.

The program can be ran from any terminal window by using the 'cd' command to move into the same directory as the 'irisanalyser.py' script and running the following command:

```python3 irisanalyser.py```

**Note that the splash screen and data summaries are quite wide and in order for them to render correctly in the terminal, the terminal window should be full screen**   

#### 3.2.2 Using the Iris Analyser
Once the script has been down loaded and ran in a terminal window, you should see the following screen:
![Splash](/img/splash.png)

Type 'no' to quit the program, 'yes' to progress, or 'help' to get some assistance regarding the commands used at various stages in the program. Note, that if the 'help' command is entered the program will automatically start once the help instructions have been printed. The help file looks like this:
![Help](/img/help.png)

The program then asks whether the user would like a data summary or graphical summary. If a data summary is required 'data' should be entered. The program will then ask the user which species they require a data summary for. 'all', 'setosa', 'versicolor' or 'virginica' can be entered. The data summary for 'all' can be seen below:
![allsumm](/img/allsumm.png)

Note that the program now asks whether or not more analysis is required, the user can type 'yes' to do more analysis or 'no' to quit the program.

If the user types 'yes', they will then be asked do they want a data summary or graphical analysis. Typing 'graph' will open the graphical summary module.

There are 3 options in this module 'scat', 'hist' or 'norm'. Typing 'scat' will allow the user to bring up a scatter plot of 2 columns of the data. Typing 'hist' can be used for a histogram of one column of the data and typing 'norm' can be used to plot a normal distribution curve using data from one column of the data.

For the columns, typing 'seplen' will select the 'Sepal Length', 'sepwid' will select 'Sepal Width', 'petlen' will select 'Petal Length' and 'petwid' will select 'Petal Width'.

Once a the graph type and columns have been selected, the program will ask for an iris species. 'setosa' will return 'Iris-setosa' data plotted in red, 'versicolor' will return 'Iris-versicolor' data plotted in blue and 'virginica' will return 'Iris-virginica' data plotted in green. 'all' will return all species on the same axis plotted in their respective colours. 'allsame' returns data for the entire data set plotted as one series in blue.

The commands for a scatter plot of Sepal Width vs. Sepal Lenght for all 3 species in seperate colours is shown below:
![scatcommands](/img/scatcommands.png)

The resulting graph would look like this:
![scatgraph](/img/scatgraph.png)

Note that once the chart window is closed down, the program will ask the user if they would like to do more analysis. As before type 'yes' to continue or 'no' to quit.

## 4. Analysis of the Iris Data Set
### 4.1 Analysis of the Data Set
In this section of the project, the iris data set will be analysed using the irisanalyser.py software. The iris data set was originally collected by Edgar Anderson while studying the morphologic differences between the 3 iris species in the the data set. This analysis will focus on this and use this iris try to determine if it would be possible to classify any iris flower by species based on the the lengths and widths of the petals and sepals alone.

#### 4.1.1 Mixed Species Histograms
This initial analysis of the will create a mixed species histogram for each of the four data columns in the data set. This aims to determine the following:

1. Is there a obvious grouping for each species?
1. Are the groupings for each species distinct and well defined?
1. Do the groupings for each species overlap?

**_Sepal Length Mixed Species Histogram_**

The mixed species hisogram for the sepal length is shown below:

![histseplen](/img/histseplen.png)

As can be see from above there is not an obvious grouping for each of the 3 species. The setosa sepals are generally longer, the versicolor somewhere in the middle and the viriginca flowers generally have longer sepal lengths, however there is a lot of overlap between the species, particualrly between the versicolor and virginca species. It would make it dificult to determine an exact species based on the sepal lengths of the flowers.

**_Sepal Width Mixed Species Histogram_**

The mixed species hisogram for the sepal width is shown below:

![histsepwid](/img/histsepwid.png)

As can be see from above there is not an obvious grouping for each of the 3 species. The setosa sepals are generally wider, but there is a lot of overlap between the species, particualrly between the versicolor and virginca species. It would make it dificult to determine an exact species based on the sepal widths of the flowers.

**_Petal Length Mixed Species Histogram_**

The mixed species hisogram for the petal length is shown below:

![histpetlen](/img/histpetlen.png)

As can be see from above there is definitely some distinction of the petal lenths between the 3 species. The setosa petals are shorter and do not overlap with the other two species of iris. There is a small amount of overlap between the versicolor and virginica species - however the petal lenth is definitely a useful charactersitic in the classification of the flower types.

**_Petal Width Mixed Species Histogram_**

The mixed species hisogram for the petal width is shown below:

![histpetwid](/img/histpetwid.png)

As can be see from above there is definitely some distinction of the petal widths between the 3 species. The setosa petals are narrower and do not overlap with the other two species of iris. There is a small amount of overlap between the versicolor and virginica species - however the petal width is definitely a useful charactersitic in the classification of the flower types.

Based on the four histograms, the sepal lenghts and widths are not very useful in determining the class of a particular flower species. The petal lenghts and widths are much more distinct and therefore useful in the classification process. This can be corrobrated by some analysis of the data carried out by the UCI machine learning repository [19]. 

This analysis calculates a 'class correlation co-efficient' for each of the 4 characterisitics. They list the results as follows:
* Sepal Length - 0.7826
* Sepal Width - -0.4194
* Petal Length - 0.9490 (high!)
* Petal Width - 0.9565 (high!)

The class correlation co-efficient describes how stongly units in the same group resemble each other [20]. The higher the value, the more related to each other items in the group are.

Based on the the initial analyses and coupled with the data from the UCI, the sepal lengths and widths can be ignored for further analysis. The remainder of the analysis will focus on the petal lengths and widths.

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
1. [12] Wikipedia. Standard Deviation. (_https://en.wikipedia.org/wiki/Standard_deviation_)
1. [13] Stack Overflow. Create nice column output in python. (_https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python_)
1. [14] Matplotlib. (_https://matplotlib.org/_)
1. [15] Matplotlib. matplotlib.pyplot.scatter.(_https://matplotlib.org/2.2.2/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter_)
1. [16] Matplotlib. matplotlib.pyplot.hist (_https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html_)
1. [17] Stack Overflow. python pylab plot normal distribution.(_https://stackoverflow.com/questions/10138085/python-pylab-plot-normal-distribution_)
1. [18] Practice Python. Rock Paper Scissors. (_https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html_)
1. [19] UC Irvine Machine Learning Repository. Data Set Description. (_http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names_)
1. [20] Wikipedia. Intraclass correlation. (_https://en.wikipedia.org/wiki/Intraclass_correlation_)

