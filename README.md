<<<<<<< HEAD
# cw

Local development
======

Install python3

sudo apt-get install python3

Code structure
--------------

developer.py : Class representing a Developer object
main.py : main script with interactive command line to run the sorting and add developers to the given list

Run:
---
python src/main.py

Comments
-----------------
1. The command prompt doesn't have a lot of control and checks over the user's input, therefore some working examples are the following:

Sorting:
  > sort_by filter1 filter2 filter3
    ex: sort_by name age

Adding new developer to the list:
  > add_developer name age ossprojects
    ex: add_developer Anna 27 2

Combined example:
Let's say we want to test whether the list will be order correctly given all 3 arguments. 
First, we can run
      > add_developer Amanda 21 9 - given that we need another similar name on the list
and then run
      > sort_by name age oss_projects 

That should print:
Name: Amanda, Age: 21, OSS_Projects: 8
Name: Amanda, Age: 21, OSS_Projects: 9
Name: John, Age: 29, OSS_Projects: 3
Name: Lawrence, Age: 32, OSS_Projects: 2
Name: Linda, Age: 29, OSS_Projects: 5
Name: Robert, Age: 24, OSS_Projects: 1
Name: Steven, Age: 24, OSS_Projects: 4

2. There are severals improvements that can be made regarding design, for example remove the sorting functionality outside the script class and with that in mind unit tests as well would be nice to validate the correctness of the sorting function. 

3. Import of more than one developer given a type of file (add_developers)
=======
# cw-exercise
>>>>>>> e8e989c3189ac9189e0478cfba0fcdca0ccf0bd6
