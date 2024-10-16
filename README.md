# Project1_Morales
Repository for Project 1 TOC fa24
Project 1 Readme Team Morales
Version 1 9/11/24
A single copy of this template should be filled out and submitted with each project submission, regardless of the number of students on the team. It should have the name readme_”teamname”
Also change the title of this template to “Project x Readme Team xxx”
1
Team Name: Morales
2
Team members names and netids: Nicolas Morales (nmorale2)
3
Overall project attempted, with sub-projects: 2-SAT Solver
4
Overall success of the project: Great! Saw that all cases were within a few milliseconds of each other, regardless of input length, meaning polynomial time was achieved.
5
Approximately total time (in hours) to complete: 3 hours
6
Link to github repository: https://github.com/nmorale2/Project1_Morales 
7
List of included files (if you have many files of a certain type, such as test files of different sizes, list just the folder): (Add more rows as necessary). Add more rows as necessary.

File/folder Name
File Contents and Use
Code Files
2SATSolver_Morales.py
Main code file. Implements a 2-SAT solver using Tarjan’s algorithm to find strongly connected components (SCCs) and checks for satisfiability.
Test Files
2SAT.cnf.csv
kSAT.cnf.csv
Bunch of test cases. Obtained from Project 1 Files in Canvas
Output Files
output_Morales.txt
Contains the outputs of the program when tested with 2SAT.cnf.csv
Plots (as needed)
plot_results_Morales.py
execution_time_plot.png
Gives the time it took to solve each block in the input file.
Resulting plot



8
Programming languages used, and associated libraries: Python, csv package, collections package, sys package, subprocess package, time package, matplotlib.plt package
9
Key data structures (for each sub-project): Directed graph in order to use Tarjan’s algorithm
10
General operation of code (for each subproject): Finds SCCs using Tarjan’s algorithm, adds implications based on the clauses, then solves the 2-SAT problem using the implication graph and Tarjan’s algorithm. Provides a boolean assignment for satisfiable problems.
11
What test cases you used/added, why you used them, what did they tell you about the correctness of your code.
I used the 2SAT.cnf.csv file because it was a) readily available, and b) it gave lots of cases. I checked by hand a few test cases to make sure my code was working properly, comparing the two results.
12
How you managed the code development: Looked online for how to implement a 2SAT solver, then implemented Tarjan’s algorithm, and accompanying functions. Hardest part was putting everything together in order to make the whole thing work.
13
Detailed discussion of results: Shown below is an example output of two blocks, followed by their inputs.
Time taken for block 0: 0.0554 seconds
Time taken for block 1: 0.0539 seconds

-4,4,0,
1,2,0,

As expected, the length of time is really short, meaning that the SAT solver is really efficient.
14
How team was organized: I worked alone
15
What you might do differently if you did the project again: I would try to use a different method of solving the 2SAT instead of Tarjan’s algorithm.
16
Any additional material: N/A


