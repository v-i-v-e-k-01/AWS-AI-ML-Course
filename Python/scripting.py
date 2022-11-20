# # Python Script -- It is just Python code/program

# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!

#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/

# <3, Juno
# """
# print(snake_string * how_many_snakes)

# # Taking variable value as input from user 

# # input('message') function -- Displays 'message' in the terminal and takes input from user as a string data type by default

# name =input("Enter a name:")
# print("Hello ", name.title())

# # default input has data type string
# num = input("Enter a number:")
# print( type(num) )

# # integer as input  with int() function
# number = int ( input("Enter a number:") )
# number+=12
# print( type(number) )

# # float as input with float() function
# num_2= float( input("Enter a decimal:") )
# print( type(num_2) )

# # eval() function -- evaluates a string as a line of Python
# x = eval(input('Enter an expression: '))
# print(x)

# num=30
# x= eval('num + 42')
# print(x)

# # taking input names list, assignments remaining for each student list and grades for each student list and printing the same within a predefined message template for each student
# names = input("Enter names separated by commas: ").split(",") 
# print(names)

# assignments= input("Enter assignments counts separated by commas:").split(",") 

# grades= input("Enter grades separated by commas:").split(",") 

# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# for name, assign, grade in zip(names,assignments,grades):
#     print(message.format(name,assign,grade, int(grade)+ int(assign)*2 ))


# ERRORS AND EXCEPTIONS

# # Syntax errors -- due to Python syntax violation
# msg='Welcome
# print(msg)

# # Exceptions --  occur when unexpected things happen during execution of program

# x= int("ten")
# x+=20
# print(x)

# print(non_existant_variable)


# #  TRY STATEMENT

# # code inside "try" block is executed first
# # if Python runs into any exceptions while running the "try" block code, it skips the rest of "try" block and executes the "except" block

# try:
#     x=int( input("Enter a number: ") )
# except: # catches all types of exception 
#     print('That\'s not a valid number!')

# print("Attempted Input") 

# # inputs to practice -- ten, four , 4, 7 etc

# # eg. if input 10 -- try block executes successfully and skips the except block
# # if input ten -- executes except block as soon as "ten" is processed i.e. after input() function is processed

# # To keep code running until user inputs a valid number 
# # we use infinite while loop and break it after the try block

# while True:
#     try:
#         x=int ( input("Enter a number: ") ) # invalid inputs 
#         # are processed until this line and then execute 
#         # except block
#         break # if try block executes without exception  
#         # until this line, the loop breaks here
#     except:
#         print( "That\'s not a valid number") 

# print( type (x) )

# # "else" block with try, except block

# # If Python doesn't run into any exception while executing try block, it executes "else" block after "try" block .

# while True:
#     try:
#         x=int ( input("Enter a number:") )
#         # here if we write "break" keyword, the loop will  
#         # after the complete execution of "try" block and 
#         # "else" block will not get executed
#     except: 
#         print("That\'s not a valid number")
#     else:
#         print("Number input successful with no exeption")
#         break

# print( type(x) )


# # "finally" block with "try", "except", and/or "else" block

# # "finally" block is executed after the "try", "except", "else" block

# # "finally" block executes irrespective of exception occurence, return/break/continue statement, or an error in any of the "try", "except", "else" block.

# while True:
#     try:
#         x= int( input("Enter a number: ") )
#     except:
#         print("That\'s not a valid number")
#         continue
#     else:        
#         print("Number input successful with no exeption")
#         break
#     finally:# executed after above code irrespective of the 
#             # above code result
#         print("all blocks complete here")

# print( type(x) )


# # Specific exception handling

# while True:
#     try:
#         x= int( input("Enter a number:") )
#         # undeclared_variable
#         break
#     except (ValueError, NameError): 
#         print("Name or Value Error")
#     except KeyboardInterrupt:
#         print("\n Keyboard Interrupt")
#     finally:
#         print("Attempted Input")

# print( type(x) )

# # inputs to try -- ten, (insert a undeclared variable in try block), enter "Ctrl + C" in terminal, 4 

# # see exception list in python documentation for all exceptions 

# # accessing original error message along with exception handling

# try:
#     x=int( input("Enter 1st number:") )
#     y=int( input("Enter 2nd number:") )
#     z=x/y
# except ZeroDivisionError as e:
#    print("Original Error Message, ZeroDivisionError: {}".format(e))

# print(z)

# # displaying original error message for any exception

# try:
#     x=int( input("Enter a number:") )
# except Exception as e:
#    print("Exception occurred: {}".format(e))

# print( type(x) )


# # READING AND WRITING FILES

# # Files -- strings of characters that encode some information

# # The characters of file are interpreted by various programs used to run/interact with them and display the output by processing/interpreting the characters

# # In Python, the raw characters of files are displayed rather than processed output


# # Reading Files

# # To read file , first they are opened and stored in a variable

# # open() function -- opens a file

# # file path is given in parenthesis along with optional parameters

# # optional parameters specify the mode in which we open the file (default mode -- 'r' )
# # 'r' -- read only 
# # 'w' -- write only  (overwrites the file contents) 
# # 'a' -- append only (adds/appends data to file)
# f = open('demo/demo_file.txt','r')

# # read() method -- reads text contained in file and returns it as string
# file_data = f.read() # file "f" is read

# # close() method -- closes a file, frees up resources used by it
# f.close()

# print( file_data )

# # files should be closed. open files has limit acc to operating system

# files=[]
# for i in  range(5000):
#     files.append( open('demo/demo_file.txt','r') )
#     print(i)

# # for i in range(5000):
# #     files[i].close()


# # Writing files

# # 'w' parameter in open function to write a file

# # in 'w' parameter anything contained in file will be deleted

# # 'w' parameter allows to create a new file of the name given in open() function, if the file isn't present in directory

# file_2=open('non_existent_file.txt','w')
# file_2.write("Hello")
# file_2.close()

# # .write() method -- used to write to the file

# f=open('demo/demo_file.txt','w')

# f.write("This is the changed demo_file")

# f.close()

# # see the demo_file.txt contents after execution of the above commands


# # With Keyword

# # allows opening files, perform operations and automatically closes files after the indented code is executed

# with open('demo/demo_file.txt','r') as f: # i.e. f=open('demo/demo_file.txt','r')
#     file_data = f.read()
#     # file 'f' closes here but file_data variable remains

# print(file_data)


# # Calling .read() method with an integer

# # no parameters in .read() method reads complete file

# # integer argument/parameter -- reads file characters upto that count,  outputs them, and keeps the 'window' at that position ready to read on

# with open('demo/demo_2.txt','r') as f:
#     print( f.read(4) )
#     print( f.read(12) )
#     print( f.readline() ) # reads full/ remaining line
#     print( f.read() )# reads remaining data of file


# # looping lines 

# # syntax -- for line in file_name:

# demo_2_lines=[]
# with open('demo/demo_2.txt','r') as f:
#     for line in f:
#         demo_2_lines.append( line.strip() ) # as each line has a newline character attached, .strip() removes it

# print(demo_2_lines)


# IMPORTING LOCAL SCRIPTS

# Imported script is stored as a module object

import demo.demo_script as demo_script # imports demo_script.py
# demo_script.py is executed here before print(4)
print(4)

# access variables of imported script
print(demo_script.num)

# access function from imported script
scores=[4,5,8,7,9]
print("Mean: ",demo_script.mean(scores) )
print("Scores incremented:",demo_script.add_five(scores))

# adding alias for imported string
import demo.demo_script as d
print( "Mean Score again:",  d.mean(scores)  )


# in-built __name__ variable

print(__name__) # the script executed gets __name__ variable value as"__main__"
print(d.__name__) # the script imported gets __name__value as "imported_script_name"


# Standard Library Modules
# https://docs.python.org/3/library/index.html

# math module
import math

print(math.factorial(4))

# learn python modules
# https://pymotw.com/3/

# Suggsted Modules: 

# csv: very convenient for reading and writing csv files

# collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple

# random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items

# string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).

# re: pattern-matching in strings via regular expressions

# math: some standard mathematical functions

# os: interacting with operating systems

# os.path: submodule of os for manipulating path names

# sys: work directly with the Python interpreter

# json: good for reading and writing json files (good for web work)


# TECHNIQUES FOR IMPORTING MODULES

import math

import math as m

# Importing individual function or class

# syntax: from module_name import object_name

from collections import defaultdict, namedtuple

defaultdict()
namedtuple

from collections import defaultdict as dfdt

dfdt()

# importing complete module and use the function directly

# not recommended in code -- creates confusion
from math import *

print( factorial(7) )


# MODULES, PACKAGES AND NAMES

# Package -- Module that contains sub-modules

#sub_modules accessed using . notation

import os.path  # here os is package and path is sub-module

print( os.path.isdir('C:/Users/Home/Desktop/Courses/AI & ML Course/Python') )

# THIRD-PARTY LIBRARIES

# Installing third party package
# type "pip install package_name" in cmd as admin

# after installation, the packages can be imported same as standard library packages

# requirements.txt file is standard convention to specify required packages

# eg. (foll. data present as text in requirements.txt)
# beautifulsoup4==4.5.1
# bs4==0.0.1
# pytz==2016.7
# requests==2.11.1

# to install all of a project's dependencies at once type the foll, command in cmd as admin:
# pip install -r requirements.txt

# Popular third-party libraries

# IPython - A better interactive Python interpreter
# requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
# Flask - a lightweight framework for making web applications and APIs.
# Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
# Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
# pytest - extends Python's builtin assertions and unittest module.
# PyYAML - For reading and writing YAML files.
# NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
# pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
# Matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
# ggplot - Another 2D plotting library, based on R's ggplot2 library.
# Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
# pyglet - A cross-platform application framework intended for game development.
# Pygame - A set of Python modules designed for writing games.
# pytz - World Timezone Definitions for Python


# IPython -- alternative to default python interpreter in cmd 

# to start ipython type -- ipython , in cmd

# ? -- gives info about object without need of seeing documentation 
# eg. len?

# ! to execute system shell commands


# Simplified Python Documentation -- https://docs.python.org/3/tutorial/