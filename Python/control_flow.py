# CONDITIONAL STATEMENTS
# BOOLEAN EXPRESSIONS
# FOR & WHILE LOOPS
# BREAK & CONTINUE
# BUILT-IN FUNCTIONS (ZIP & ENUMERATE)
# LIST COMPREHENSION

# Control Flow is the sequence in which the lines of code are executed

# IF STATEMENT

phone_balance=3
bank_balance=100

print(phone_balance, bank_balance)

if phone_balance <5:
    phone_balance += 10
    bank_balance -=10

print(phone_balance, bank_balance)

# IF, ELIF, ELSE

n=4
if n%2==0:
    print("Number " + str(n) + " is even")
else:
    print("Number " + str(n) + " is odd" )

print(n)

season="spring"
if season=="spring":
    print("plant the garden")
elif season=="fall":
    print("water the garden")
elif season=="winter":
    print("stay indoors")
else:
    print("unrecognized season")

# Indentation

#The Python Style Guide recommends using 4 spaces to indent, rather than using a tab. Whichever you use, be aware that "Python 3 disallows mixing the use of tabs and spaces for indentation."


# COMPLEX BOOLEAN EXPRESSIONS

weight=56
height=164
if 18.5 <= weight / height**2  <25:
    print('EMI is considered "normal"')

is_raining=True
is_sunny=True
if is_raining and is_sunny:
    print("is there a rainbow?")

unsubscribed=False
location="CAN"
if (not unsubscribed) and (location == "USA" or location=="CAN"):
    print("send email")

# Entire line in an if statement must evaluate to a boolean value i.e either True or False

# GOOD AND BAD EXAMPLES

# If the entire line in an if statement always evaluates to True or always evaluates to False, the core usability of if conditional statement isn't used at all.
is_cold=False
if is_cold or not is_cold:
    print("This indented code will always get run.")

# The below code will result  in always printing "wear boots" and is not a boolean expression ( the right part of if condition line)
weather="hell"
if weather== "snow" or "rain": # the right part of "or" i.e. "rain" is a string and not a boolean expression
    print("wear boots")

# instead we use the following code
if weather=="snow" or weather=="rain":
    print("Boots are required")
else:
    print("Boots not required")

# Be careful writing expressions that use logical operators
# Make sure Boolean expression are evaluated you expect them to
# Don't compare a boolean variable with "== True" OR "==False" as they themselves evaluate to True or False
is_cold=True
if is_cold==True:
    print("Weather is cold") 

# instead use the variables directly

if is_cold:
    print("Weather is cold")

# TRUTH VALUE TESTING

# Objects with truth value as False:

# Constants defined to false: "None" & "False"

# Zero of any numeric type 
# i.e. Decimal(0.0) , Complex No.(0j) , Fraction (0,1)

# Empty sequences and collections
# i.e. "" , '', (), [], {}

# Anything that isn't listed as truth value False is evaluated as True

errors=3
if errors: # evaluates to true as errors is a non zero number
    print("There are "+ str(errors) + " mistakes")
else:
    print("no mistakes here")

# in the "wear boots" example, the string on the right hand side "rain" wolud always evaluate to true as it is non empty string

if weather =="hell" or "": # "" will always evaluate to false, thus the result depends on truth value of the expression on left 'weather =="hell"'
    print("Boots not required")


# FOR LOOPS

# A for loop is used to "iterate", or do a task repeatedly, over an iterable.

# Iterable -- It is an object that can return one of its elements at a time.
# This can include sequence types such as strings, lists, or tuples, as well as non sequence types such as dictionaries and files.

# Iteration variable -- variable that represents each element in the iterable that the loop is currently processing

cities = ['new york city', 'mountain view', 'chicago', 'los angeles'] # iterable

for city in cities: # cities is the iterable and city is the loop's iteration variable
    print(city.title())

# We can also use for loop to create list & modify list

# creating list
capitalized_cities=[]
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

# range() function -- It creates iterable sequences of numbers. 

# It has three integer arguments --
# ( first and third arguments are optional )
# start -- is first number of sequence ( 0 if unspecified)
# stop -- is 1 more than last number of sequence
# step -- is the difference between each number of sequence (default is 1) 

# calling range with only one argument, makes it a stop argument
print( list( range(4) ) ) # stop=4 (stop is one more than last number by definiton)

# calling range with two integers, makes them the start and stop arguments
print( list( range(2,6) ) ) # start=2, stop=6 

# calling range with three integers
print( list( range(1,10,2) ) ) # start=1, stop=10, step=2
# prints 1, 3, 5, 7, 9

for number in range(4):
    print(number)

# modifying list

for index in range( len(cities) ): # len(cities)=4
    cities[index]= cities[index].title()
print(cities)

for i in range(4):
    print("Hello")


# We can define objects with an iter() method to allow them to be used as an iterable.

############################################################################################################################

# PRACTICE QUESTION

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for number in range(5,31,5):
    print(number)

# save each name in username with all lowercase letters and underscore instead of space
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for index in range( len(names) ):
    usernames.append( names[index].lower().replace(" ","_")  ) 
print(usernames)

# Modifying the same names list instead of creating new list

# incorrect method
for name in names:
    name = name.lower().replace(" ", "_")
    # this will assign the changed value to the iterating variable name but not assign it to the names list as no such command is given. It just extracts and changes value of tbe iterating variable
print(names)

# The printed output for the names list will look exactly like it did in the first line. 
# During each iteration, the name variable is set to a string taken from the list. Then the assignment statement creates a new string (name.lower().replace(" ", "_")) and changes the name variable to that string. 
# It doesn't modify the contents of the names list at all. To modify the list you must operate on the list itself, using range, as you saw earlier.

# correct method
for index in range( len(names) ):
    names[index]= names[index].lower().replace(" ","_")

print(names)

############################################################################################################################

# BUILDING DICTIONARIES

# finding the frequency of words in the list
book_title = ['great','expectations','the','adventures','of','sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin' ]

word_counter ={} # declaring dictionary 

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word]+=1

print(word_counter)

# OR
word_counter2={}
for word in book_title:
    word_counter2[word]= word_counter2.get(word,0) +1
print(word_counter2)


# ITERATING THROUGH DICTIONARIES WITH FOR LOOP

# "for n in some_dict" will only give keys of dictionary
cast={
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards":"Cosmo Kramer"
}

for key in cast:
    print(key)

# .items() method --  returns tuples of key and values pairs of a dictionary
print( cast.items() )

for key, value in cast.items():
    print("Actor:{}    Role:{}".format(key,value) ) # prints both keys and values


# WHILE LOOOPS

# For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. 

# This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a while loop. 

# sum() -- returns sum of elements in a list

card_deck =[4,11,8,5,13,2,8,10]
hand=[]

while sum(hand) <=17:
    hand.append(card_deck.pop() )
    print( sum(hand) )
print(hand) 

# the indented body of the loop should modify at least one variable in the test expression/ condition, else the loop will execute infinitely.


# FOR LOOPS VS WHILE LOOPS

# for loops are ideal when number of iterations is known to be finite

# iterable collections like list, set, tuple, dictionary 

# iterating through loop for definite no. of times with range() functiom

# while loops are ideal when the iterations need to continue until a conditiom is met

# comparison operator, loops based on receiving specific user input


# BREAK, CONTINUE

# break -- terminates the loop 

# cargo loading
# here manifest is list of cargo to be loaded with each cargo represented by a tuple with name and weight
# total weight should not exceed 100
manifest = [ ("bananas",1), ("mattresses",24), ("dog kennels",42), ("machine", 120), ("cheeses",5) ]

weight=0
items=[] # items to be loaded

for cargo in manifest:
    if weight >=100:
        break
    else:
        items.append(cargo[0])
        weight +=cargo[1]

print(weight) # weight exceeds 100
print(items)

# instead
weight=0
items=[]
for cargo in manifest:
    if  weight + cargo[1] >=100:
        break
    else:
        items.append(cargo[0])
        weight +=cargo[1]

print(weight) # weight <=100
print(items)
 

# continue -- skips one iteration of the loop

fruit=["orange","strawberry","apple"]
foods=["strawberry","apple","humus","toast"]

fruit_count=0
for food in foods:
    if food not in fruit:
        print("Not a fruit")
        continue
    fruit_count+=1
    print("found a fruit")

print("Total fruit: "+ str(fruit_count) )

# in cargo example we can add lower weight elements after machine which can fit under limit 100
weight=0
items=[]
for cargo in manifest:
    if weight + cargo[1] >=100:
        continue
    else:
        items.append(cargo[0])
        weight +=cargo[1]

print(weight) 
print(items)


############################################################################################################################

# PRACTICE QUESTION

# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker=""
for headline in headlines:
    news_ticker=news_ticker+ headline + " "
    if len(news_ticker) >=140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

############################################################################################################################

# ZIP, ENUMERATE

# zip() -- returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables
items=['bananas','mattresses','dog kennels','machine','cheeses']
weights=[15,34,42,120,5]

print( list( zip(items, weights) ) )

# looping 
for cargo in zip(items, weights):
    print(cargo[0], cargo[1])

# unpacking with zip() function
 
some_list=[ ('a',1),('b',2),('c',3),('d',4) ]

letters, numbers = zip(*some_list) # returns two tuples 
print(letters)
print(numbers)

# iterating lists with returning index with values

items=['bananas','mattresses','dog kennels','machine','cheeses']

for i, item in zip(range(len(items)),items):
    print(i,item)

# enumerate() function -- returns an iterator of tuples containing indices and values of a list.   

for i, item in enumerate(items):
    print(i,item)

############################################################################################################################

# PRACTICE QUESTION

#Use zip() to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.

data=((0,1,2), (3,4,5), (6,7,8), (9,10,11))

data_transpose=tuple( zip(*data) )

print(data_transpose)

############################################################################################################################

# LIST COMPREHENSION

#eg. 1
cities = ['new york city', 'mountain view', 'chicago', 'los angeles'] 

capitalized=[city.title() for city in cities]

#eg. 2
# squares=[]
# for x in range(9):
#     squares.append(x**2)

squares=[x**2 for x in range(9)]
print(squares)

# conditionals in list comprehension

# "if" condition are put after the iterable

squares2=[x**2 for x in range(9) if x%2==0]
print(squares2)

# If there is "if" and "else" statement, they are put at beginning after the expression (here expression is "x**2")

squares3= [x**2 if x%2==0 else x+3 for x in range(9)]
print(squares3)

############################################################################################################################

# PRACTICE QUESTION

# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names= [ name.lower().split()[0] for name in names ]
print(first_names)

############################################################################################################################

# OVERALL PRACTICE QUESTIONS

# Q1 (A)
# Create a dictionary that includes the count of Oscar nominations for each director in the nominations list
nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
 
nom_count_dict = {}

for year in nominated:
    for name in nominated[year]:
        nom_count_dict[name]= nom_count_dict.get(name, 0)+1
        
print("nom_count_dict = {}\n".format(nom_count_dict))


# Q1 (B)
# Create a dictionary with the count of Oscar wins for each director in the winners list

win_count_dict = {}

for year, winner_list in winners.items():
    for winner in winner_list:
        win_count_dict[winner]=win_count_dict.get(winner,0)+1


print("win_count_dict = {}".format(win_count_dict))

# Q2
# Provide a list with the name(s) of the director(s) with the most Oscar wins. We are asking for a list because there could be more than 1 director tied for the most Oscar wins

most_win_director = []
# Add your code here
win_count_dict = {}

for year, winner_list in winners.items():
    for winner in winner_list:
        win_count_dict[winner]=win_count_dict.get(winner,0)+1

highest_count = 0

for key, value in win_count_dict.items():
    if value > highest_count:
        highest_count = value
        most_win_director.clear()
        most_win_director.append(key)
    elif value == highest_count:
        most_win_director.append(key)
    else:
        continue

print("most_win_director = {}".format(most_win_director))