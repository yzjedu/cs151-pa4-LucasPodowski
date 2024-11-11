[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z38AR3-E)
<h1>CS151 PROGRAMMING ASSIGNMENT</h1>

- 🔵 **_Understand the problem and Design before Coding_** 🔵
- 🟢 **_FINAL DUE: Thursday 11/21/24 at 11:59 PM_** 🟢
- **_Programming Grade: EMRN_**

<h2>Table of contents</h2>

<!-- TOC -->
  * [`I. PROBLEM:`](#i-problem)
  * [`II. PURPOSE OF THE ASSIGNMENT`](#ii-purpose-of-the-assignment)
  * [`III. REQUIREMENTS ANALYSIS `](#iii-requirements-analysis-)
    * [Files](#files)
    * [Usability](#usability)
    * [User Options](#user-options)
  * [`IV. DESIGN`](#iv-design)
    * [Function design:](#function-design-)
  * [`V. PROGRAMMING REQUIREMENTS`](#v-programming-requirements)
    * [Testing your Program](#testing-your-program)
    * [To earn an E](#to-earn-an-e)
  * [`VII. ASSIGNMENT REMINDERS`](#vii-assignment-reminders)
  * [`VIII. What to Submit in GitHub`](#viii-what-to-submit-in-github)
<!-- TOC -->

## `I. PROBLEM:`

- You are creating a program to analyze headlines from the Australian Broadcasting Company (ABC). 
- Your program is going to read in the file chosen by the user, and then allow them to request specific types of analysis on that file. 
- The headlines included in this assignment are real headlines from this real news agency.

## `II. PURPOSE OF THE ASSIGNMENT`

The purpose of this assignment is to give you  
1. Practice with files
2. Practice with lists
3. Practice with designing functions
4. Practice with implementing functions

## `III. REQUIREMENTS ANALYSIS `

The first stage in your programming assignment is the requirements analysis stage.  
- You must understand the problem before you can try to solve it.

At the start of the program, the user will get to tell you the name of a headline file they would like to analyze. 
- You must read in this data and store it in a list before doing any analysis. 
- Your program should have excellent usability and prevention of crashing.

### Files

Included in this assignment are six potential input files, all the same format, but with different data. 
- If you write your code correctly, it will be able to read in any of the files and process it without changing any of your code. 
- Each file has 1 headline per line of the file. 
- The files are very large, which is one of the reasons we need Python to help us analyze them.

### Usability

Remember that your program should:
1. Follow good usability/HCI principles in input and output. 
   - You must go above and beyond what we were doing in the first half of the semester, now that we know how to special characters like tabs, and f strings for print formatting.
2. Protect the program against bad user input
   - It should be clear what to input, and error checking should prevent the user from crashing your program.
3. State at the start the purpose of the program.
   - Use a clear to separator, such as `------` or new line to separate the purpose from the user interaction
   
### User Options

The user can choose the following types of analyses on the file they chose to analyse at the start of the program:

1. Determine how many headlines have a particular word in it, for a single file
2. Write headlines containing a specific word to a new file.
   - User gets to choose the name of the word and the new file .
3. Determine the average number of characters per headline
4. Output the longest and shortest headline. 
   - Length is determined by number of characters.
5. Read in a new file to analyze. 
   - If the user chooses this option, it overwrites the data you had been storing 
   <br> (e.g. old file is no longer stored in program after new file is read in)

The user gets to keep choosing what they want to do until they choose to quit.

## `IV. DESIGN`

The second stage is to design your solution based on the requirements. 
- Think about how to break the problem up into different smaller problems that are easier to solve. 
- In particular, what functions do you need? 
  - Remember that functions are the tasks that the program is solving.
### Function design: 
  For this design, you need to determine the functions that you need and their algorithms. For each function you need to know:
  -  **In algorithm**
  ```
  # Purpose:  [what problem does the function solve?]
  # Name: [The proposed name of the function]
  # Parameters: [list with purpose in the same order they appear in the function header]
  # Return: [return value, it's type, and what it represents]
  # Algorithm:
  ```
  - **In Code**
  ```
  # Purpose:  [what problem does the function solve?]
  # Parameters: [list with purpose in the same order they appear in the function header]
  # Return: [return value, it's type, and what it represents]
  ```
**Don't forget main and error checking!**


## `V. PROGRAMMING REQUIREMENTS`

After your design is complete and correct, it’s time to start programming and then testing. 
- This is a great time to start practicing iterative development. 
- Instead of writing an entire program and then testing it, write part of it, test it, then write the next part. 
- That way if something is broken it will be easier to figure out why. 
- Now that you have functions, there are natural ways to build up a working program. 
  - For example, get the basic menu functionality working, where you just output what each option does. 
  - Then, add file reading. Make sure that works, then add in an analysis option, etc.

**Be careful not to overwrite the contents of your input files. Never use your input file as the name of your output file**. 
- If you accidentally do this, you can use the history functionality at the bottom of this view to revert the text file to its original data.

### Testing your Program

To make it easier to test your program, we provide a few of the expected answers. 
- The below does not include error checking, and you probably want to run it for other inputs as well.

For `2017.txt`:
```
* the word "cat" appears 34 times
* the word "pirate" appears 4 times
* the average number of words in a headline is 6
* the average number of characters in a headline are 49.5
* Shortest headline (by characters): 4
* Longest headline (by characters): 70
```


For testing files it can also be useful to test on a smaller file that you can easily check by hand against. 
- We've provided `testfile.txt` for this purpose. 
- Here you can figure out which lines should be included for whatever word you are searching for, or 
  <br> calculate what the average length should be, and compare to what your program is doing.

### To earn an E
If you are going for an E on this assignment, it should have most of the following:
1. Works correctly
2. Has good commenting
3. Uses for loops
4. Overall good code style and choices
5. Excellent usability


## `VII. ASSIGNMENT REMINDERS`

- Follow the programming assignment requirements document for comments, formatting, etc. 
- Follow the honor code guidelines outlined in the syllabus and at [here](https://www.loyola.edu/academics/computer-science/current-students/honor-code).

- Include an updated version of the intro comments. 
  - Note the new final line below about `Input files`. 
  - Be sure to note that you need input files that contains the headlines! 
```
# Programmers:  [your names here]
# Course:  CS151, [Instructors Name]
# Due Date: [date assignment is due]
# Lab Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Input Files: [description of the format of the input files you need for this program to work]
```

## `VIII. What to Submit in GitHub`

1. Completed `main.py` file
2. Completed `algorithm.md` -> Contains the algorithm of your program
2. `reflection.md` -> Reflection of the assignment


**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working by yourself?
   
***Remember to commit and push your GitHub project.***