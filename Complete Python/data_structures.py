# DATA STRUCTURES

# -- are Containers of data, contains different data types and even other data structures/containers

# LISTS AND MEMBERSHIP OPERATORS

# Lists

# A data type for mutable ordered sequences of elements

# Lists can contain any mix and match of the data types you have seen so far

# declared with square brackets []

random_list=[147, 34.25, 'a string', True ]

print(random_list[2])


months=['January','February','March','April','May','June','July','August','September','October','November','December']

print(months[0])# first element has index 0
print(months[1])

#can retrieve last element of list by following method
print( months[ len(months)-1 ]  )

# OR

print(months[-1]) # last element has index -1
print(months[-2]) # second last element has index -2
print(months[-12])

#print(months[18]) 
# gives error as Index out of range

# Slicing Lists

# using indexes

quarter_3= months[6:9] # index 6 to 9 i.e. [6,9) including lower bound [6] and excluding upper bound [9] -- months[6]=July
print(quarter_3) 

# slicing at beginning
print(months[:4]) # prints until month[3]=April, months[4] is excluded

#slicing at end
print(months[9:]) # months[9]=October

# negative indexes work in slicing
print(months[-10:-8]) 
print(months[:-4])
print(months[-4:] )

#string & list both support len(), indexing and  slicing , & membership operators 
greeting="Hello World"
print( len(greeting) ) # len()
print ( greeting[0] ) # indexing
print( greeting[2:10] ) # slicing [2,10) 



# Membership Operators

# two operators:
# in -- evaluates whether object on left side is included in object on right side

# not in -- evaluates whether object on left is not included in object on right side

greeting="Hello there"
print( 'her' in greeting , 'her' not in greeting)
print('Sunday' in months, 'Sunday' not in months)


# lists contain other data types while strings contain characters


# MUTABILITY AND ORDER


# Mutability

# is a term for whether an object can be modified after its creation.

# lists -- mutable , strings -- immutable

my_list=[1,2,3,4,5]
my_list[0]='one'
print(my_list)

greeting = "Hello"
print(greeting)
# greeting[3]='i' 
# gives error as strings can't be modified

# instead you will need to create complete new string 
# eg.
greeting="Gello"
print(greeting)

# Important feature of Mutability

# Mutable objects when assigned to another object, and then value of the mutable object is changed, the value of the other object also changes

# eg. (as lists are mutable)
scores=['A','B','C','D','E']
grades=scores
print(scores)
print(grades)

scores[2]='F'
print(scores)
print(grades) # grades[2] value is also changed automatically to 'F' 

# eg. (strings are immutable)
name="Jim"
student=name
print(name)
print(student)

name="Not Jim"
print(name)
print(student)


# Order

# term for whether the order of elements in an object matters, and whether this can be used to access elements

# both lists and strings are ordered

############################################################################################################################

# PRACTICE QUESTION

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003', 'March 29, 2006', 'August 1, 2008', 'July 22, 2009', 'July 11, 2010', 'November 13, 2012', 'March 20, 2015', 'March 9, 2016']
                                  
# TODO: Modify this line so it prints the last three elements of the list

print(eclipse_dates[-3:])

############################################################################################################################


# LIST METHODS

# len() method -- returns no. of elements in list

# max() method -- returns greatest element, depends on data types in list
# if numbers in list - largest number
batch_sizes=[15,45,89,34,35]
print(max(batch_sizes))

# if strings in list - last element when arranged alphabetically
python_varieties=['Burmese','African','Reticulated','Angolan']
print(max(python_varieties))

# if multiple data types in list - max() method gives error
# max( [ 42, 78, 'Hello', 'World'] )

# max() method is based on greater than Comparison Operator (i.e. > )

# min() method -- returns smallest element in list

# sorted() method -- sorts list elements from smallest to largest leaving original list unchanged
size=[15,6,89,34,65,35]
print(sorted(size))
print(size)

# to sort list elements from largest to smallest use reverse=True as a second parameter in sorted() method
print( sorted( size, reverse=True) )


# .join() method -- takes list of strings as argument and returns a string with separator string (specified by user) joining consecutive elements

# .join() gives error if data type other than string are present in list

names=['Garcia',"O'Kelly",'Davis']
print("-".join(names)) # "-" is the separator string here

nautical_directions= "\n".join( ['fore','aft','starboard','port'] ) # "\n" is the separator string in 'fore' & 'aft' and so on
print(nautical_directions)

# .append() method -- adds an element to the end of the list

python_varieties.append('Blood')
print(python_varieties)


# TUPLES

# data type for Immutable ordered sequences of elements (like strings)
# declared within round brackets (optional)
# tuples are immutable, thus the elements cant be modified including sorting them along with adding / removing items.

AngkorWat=(13.4125, 103.866667)

print(type(AngkorWat))

print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

# parenthesis are optional

dimensions = 52,40,100
length,width,height=dimensions # assign tuple element values to 3 different variables, called tuple unpacking

print("The dimensions are: {}x{}x{}".format(length,width,height))


# SETS

# Data type for immutable, unordered collections of unique elements

# declared using curly brackets {}

set_example = { 'hello', 'world', 45, True }

print(type(set_example))

countries_list= ['Angola','Maldives','India','United States','India','Denmark','Russia','Japan','Japan']

country_set=set(countries_list) # converting list to set
print(country_set)
print( len(country_set) )

# Sets support membership operators like lists

print("India" in country_set)
print("India" not in country_set)

# .add() method -- to add elements to list

country_set.add('Ghana')
print( len(country_set))

# pop() method -- used to remove last element like in list but as sets are unordered, there's no fixed last element to remove thus random element gets removed

print(country_set.pop())
print( country_set )
# union, intersection and difference of sets can be performed


# DICTIONARIES AND IDENTITY OPERATORS

# Dictionaries

# Data type for mutable , ordered objects with unique key:value pairs

# declared using foll. syntax --  dictionary_name={key:value, key:value ...}
elements={ 'hydrogen':1, 'helium':2, 'carbon':3 }
# dictionary values can be any data type but keys should be immutable data type (strings, integer, tuple )

# It's not  necessary for every key in a dictionary to have the same data type
random_dict = {"abc": 1, 5: "hello"}

#look up dictionary values using dictionary_name['key']
print(elements['carbon'])

# add values in dictionary
elements['lithium']= 3
print(elements)

# membership operators supported by dictionaries
print("carbon" in elements)
print("3" in elements)

print("1" not in elements)

# .get('key') method -- used to get values from dictionaries but returns None or a default value when not found
print(elements.get('dilithium'))
print( elements.get('kryptonite', 'There\'s no such element!') )


# Identity Operators

# is -- evaluates if both sides have same identity
# is not -- evaluates if both sides have different identities

x=elements.get('halogen') # stores None value in x
null = x is None 
print(null)

not_null=x is not None
print(not_null)

# Difference between == and  'is' operator

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a==b)
print(a==c)
print(a is b)
print(a is c)


# COMPOUND DATA STRUCTURES

# We can store dictionaries as values inside dictionaries

elements ={
    'hydrogen': {   'number':1,
                    'weight':1.00794,
                    'symbol':'H'},
    'helium':{  'number': 2,
                'weight':4.002602,
                'symbol':'He'}
}

print(elements['helium']['weight'])
