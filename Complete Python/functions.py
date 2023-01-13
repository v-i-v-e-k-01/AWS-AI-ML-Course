# DEFINING FUNCTIONS

# function definition starts with "def" keyword

# syntax

# def function_name(argument1,argument2,argument3..):
#   ###########################
#   # instructions  to execute
#   ###########################
#   return return_value  # not necessary to return 


def cylinder_volume(height,radius):
    pi=3.14159
    return pi*height*radius**2

cylinder_volume(10,3) # calling function

print( cylinder_volume(10,3) )

# variable declared inside function have local scope i.e. they aren't accessible outside function 

# DEFAULT ARGUMENTS

def cylinder_volume2(height, radius=5):
    pi=3.14159
    return height*pi*radius**2

print( cylinder_volume2(10) ) # similar to cylinder_volume2(10,5)

# overwriting default value
print( cylinder_volume2(10,7) )

# passing arguments by position
print( cylinder_volume(14, 8) )
# passing arguments by name
print( cylinder_volume(height=14, radius=8) )


# VARIABLE SCOPE

# The parts of the program that a variable can be referred, or used, from

# Local Scope Of Variable
def word_count(document, search_term):
    words = document.split() # local scope
    answer=0 # local scope
    for word in words:
        if word == search_term:
            answer+=1
    return answer

def nearest_square(limit):
    answer=0 # local scope
    while (answer+1) ** 2 <limit:
        answer+=1
    return answer**2

# print(answer) -- gives error as answer variable is defined inside function and has local scope

# Global Scope Of Variable
answer2=10

def show_answer():
    print(answer2)

show_answer() # global variable can be accessed without passing them as argument
print(answer2)

# global variable can be accessed inside function
# global variable cannot be modified inside function

answer2=10
# def  answer_change():
#     answer2=answer2**4 # Gives UnboundLocalError
#     print(answer2)

# answer_change()
# print(answer2) 

# instead pass the global variable as an argument to the function and modify it in local scope
def answer_change(arg):
    arg=arg ** 4
    print(arg)

answer_change(answer2)# value changes locally inside function
print(answer2) # global value of global variable doesnt change

#  It is best to define variables in the smallest scope they will be needed in.

############################################################################################################################

# PRACTICE QUESTION

# What is the result of the below code

# egg_count = 0

# def buy_eggs():
#     egg_count += 12

# buy_eggs()

# answer -- UnboundLocalError 

#  This causes an UnboundLocalError, since Python doesn't allow functions to modify variables that are outside the function's scope. 
# A better way would be to pass the variable as an argument and reassign it outside the function. 

egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)

print(egg_count)

############################################################################################################################

# DOCUMENTATION

# Docstring -- A type of comment used to explain the purpose of a function and how it should be used

# Docstrings are enclosed in triple quotes

# Single line Docstrings -- for simple functions

def population_density(population, land_area):
    """Calculate the population density of an area.
    """
    return population/land_area

print(  population_density(45,12) )


# Multiline Docstrings

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic. If you pass in values in terms of square km or square miles the function will return density in those units.

    OUTPUT:
    population_density: population/land_area. The population density of a particular area.
    """
    return population/land_area

# Every part of Docstring is optional


# LAMBDA EXPRESSIONS

# Expression used to create an anonymous function i.e. function without a name which aren't needed later in the code

# declared using "lambda" keyword, followed by arguments and a colon, after which code to be executed is written which is returned as result

# syntax:
# var_to_store_result = lambda input_var1, input_var2.. : code_here

# simple function
# def double(x):
#     return x*2

# lambda expression
double = lambda x: x*2

double(4) # calling lambda expression/function

print ( double(4) ) 

# eg 2
multiply_answer= lambda x,y: x*y

print( multiply_answer(8,7) )


# map() function -- Function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. 

# syntax 
# map(function_name, arguments iterable of the function)

numbers=[
            [34,63,88,71,29], # argument for 1st execution
            [90,78,51,27,45], # argument for 2nd execution
            [63,37,85,46,22], #   .
            [51,22,34,11,18]  #   .
        ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list( map(mean, numbers) )
# "mean" is the function and "numbers" is the arguments iterable

print(averages)


# filter() function -- Function that takes a function and an iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True

# syntax
# filter(function_name, arguments iterable)

cities=['New York City','Los Angeles','Chicago','Mountain View','Denver','Boston']

def is_short(name):
    return len(name)<10 # returns True/ False

short_cities= list( filter(is_short, cities) )

print(short_cities)






