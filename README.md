# IT 2750 - Scripting Fundamentals for Cybersecurity
## Lab 2 - Exploring Python Basics and Password Security

### 🗒  Description
This repository contains the Python script for Lab 2 of the course IT 2750 - Scripting Fundamentals for Cybersecurity. There are four problems in this lab.

This lab will reinforce your scripting skills while also delving into the intricacies of password complexity calculations. Problem 1 introduces basic arithmetic operations, Problem 2 extends this to interactive user input, Problem 3 focuses on string operations, and Problem 4 delves into password complexity calculations. This hands-on experience not only enhances your scripting abilities but also provides valuable insights into the mathematics behind password security, making it an essential exercise in cybersecurity fundamentals.

#### Problem 1 - Performing Operations on Numeric Variables
Problem 1 is designed to reinforce fundamental scripting skills and arithmetic operations in Python. In this problem, students are instructed to define two variables, `num1` and `num2`, and set their values to 42 and 11, respectively. They are then guided through a series of arithmetic operations, including addition, subtraction, multiplication, division, squaring, and modulo, and instructed to print the results to the screen for each operation. This problem serves as an introductory exercise to Python's basic arithmetic capabilities and encourages students to practice performing calculations within a script.

#### Problem 2 - Performing Operations on Numeric Variables Using Input
Problem 2 reinforces basic arithmetic operations in Python. In this problem, students are instructed to create two variables, `num1` and `num2`, and use the `input` function to interactively gather numerical values from the user for these variables. After obtaining the user's input, students are guided through a series of arithmetic operations, including addition, subtraction, multiplication, division, squaring, and modulo, and instructed to print the results to the screen for each operation. This problem serves as a hands-on exercise that allows students to perform calculations based on user input and practice their Python scripting skills.

#### Problem 3 - Operating with String Variables
Problem 3 requires students to create two variables, `string1` and `string2`, and use the `input` function to interactively gather string values from the user for these variables. After obtaining the user's input, students are guided through various tasks. They are asked to concatenate `string1` and `string2` and print the result, replicate `string1` five times using the replication operator, and display the sum of the lengths of `string1` and `string2`. This problem serves as a hands-on exercise to practice string operations and length calculations in Python.

#### Problem 4 - Determining Password Complexity
Problem 4 tasks students with using a pre-written Python function called `calculate_search_space` that calculates the total possible combinations of a password based on user-defined parameters such as password length, usage of uppercase characters, lowercase characters, and numbers. The lab starts by obtaining the desired password length from the user and then prompting them with three questions to determine their password requirements. After gathering these inputs, the `calculate_search_space` function is utilized to compute the search space of possible password combinations. Subsequently, students calculate the theoretical number of days it would take for a slow computer to crack the password, displaying the result. This lab serves as an interactive exercise to explore password security and the mathematics behind password search space.

### 📝  Requirements
This lab requires you to write code that adheres to the following requirements:

#### Problem 1
In Problem 1, you will edit the script template to perform the following tasks:

- Part A: Defines two variables, `num1` and `num2`, and sets the value of `num1` to 42 and the value of `num2` to 11.
- Part B: Adds `num1` and `num2` and prints the result to the screen.
- Part C: Subtracts `num2` from `num1` and prints the result to the screen.
- Part D: Multiplies `num1` and `num2` and prints the result to the screen.
- Part E: Divides `num1` by `num2` and prints the result to the screen.
- Part F: Prints the sum of `num1` squared and `num2` squared.
- Part G: Prints the result of `num1` modulo `num2`.

#### Problem 2
In Problem 2, you will edit the script template to perform the following tasks:

- Part A: Creates two variables, `num1` and `num2`, by taking user input for their values.
- Part B: Adds `num1` and `num2` and prints the result to the screen.
- Part C: Subtracts `num2` from `num1` and prints the result to the screen.
- Part D: Multiplies `num1` and `num2` and prints the result to the screen.
- Part E: Divides `num1` by `num2` and prints the result to the screen.
- Part F: Prints the sum of `num1` squared and `num2` squared.
- Part G: Prints the result of `num1` modulo `num2`.

#### Problem 3
In Problem 3, you will edit the script template to perform the following tasks:

- Part A: Creates two variables, `string1` and `string2`, by taking user input for their values.
- Part B: Concatenates `string1` and `string2` and prints the result to the screen.
- Part C: Replicates `string1` five times using the replication operator and displays the output.
- Part D: Displays the sum of the length of `string1` and the length of `string2`.

#### Problem 4
In Problem 4, you will edit the script template to perform the following tasks:

- Part A: Obtains the desired password length from the user.
- Part B: Asks the user whether they want to use UPPERCASE characters, lowercase characters, and numbers and saves the values into variables `uppercase`, `lowercase`, and `numbers`.
- Part C: Calculates the password search space using the `calculate_search_space` function and displays it to the user.
- Part D: Calculates and displays the number of days it would take for a theoretical computer to crack the password in the worst-case scenario.

#### Additional Requirements
In order to receive credit for this lab, you must replace `YOUR_NAME_HERE` with your name and `YOUR_EMAIL_HERE` with your Tri-C email address in the code file headers for all script files in the template. Students who do not perform this action will receive a zero score.

### 🚀  Usage
To run the script, execute the script file with Python. Each part of the lab problem is commented, and you should replace the placeholder text with your own information. From the code directory of this lab, you can run the various problems using the following commands:

- Problem 1: `python lab2_problem1.py`
- Problem 2: `python lab2_problem2.py`
- Problem 3: `python lab2_problem3.py`
- Problem 4: `python lab2_problem4.py`

### 🎯  Testing
The problems in this lab are tested using code that can be found in the corresponding `tests_*.py` file for each problem. You can use these tests to check if your code runs properly and to specifications. You can run these tests on your local machine by setting your working directory to the problem folder and running `pytest` with the `tests_*.py` file for the problem. From the code directory of this lab, you can run tests using the following commands:

- Problem 1: `pytest tests_lab2_problem1.py`
- Problem 2: `pytest tests_lab2_problem2.py`
- Problem 3: `pytest tests_lab2_problem3.py`
- Problem 4: `pytest tests_lab2_problem4.py`

### 🏆  Grading
This lab is worth 40 points in total using the following breakdown by problem:

- Problem 1 is worth 10 points
- Problem 2 is worth 10 points
- Problem 3 is worth 10 points
- Problem 4 is worth 10 points

You are awarded these points if all assertions in the test file pass successfully for a problem. There is no partial credit for lab problems.

### 💻  Academic Integrity and Copyright
This lab was created by the course professor (Matthew Crowley) and he asserts copyright over all material. You are not permitted to share the labs, tests, or solutions with anyone without express written consent. Breaches of this assertion may result in both academic and legal sanctions.