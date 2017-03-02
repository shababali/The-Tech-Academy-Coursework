'''Ch3: Python Basics 1'''


43.5/10

4.35*1.61

10/1.61

43.5/6.211180124223602

print 'This stuff rocks'

x = 10
print x

y = 2
print (x+y)

print (x-y)

print (x*y)

print (x/y)

# print X
'''
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print X
NameError: name 'X' is not defined
''' 

some_int_variable = 2
some_float_variable = 1.24
some_boolean_variable = True
some_string_value = "awesome text here"
print some_int_variable

print some_float_variable

print some_boolean_variable

print some_string_value





'''Ch 4: Python Basics 2'''


x=10
y=2

'''Prints x + y
to the shell - example of
a block comment in Python.'''

print(x+y)

if x == 10:
    print'x = 10'

if y == 2:
    # In the statement
    print 'x = 10'
    # Still in the statement

# Not in the statement.  Statement finished.



'''Ch5: Puppet Master: Playing the Strings'''


name = "Guido"
print name[0]
print name[3]
print name[4]
print name.upper()
print name.lower()
print name.capitalize()

date = "11/12/2013"

# Go through string and split
# where there is a '/'
date_manip = date.split('/')

# Show the outcome
print date_manip
print date_manip[0]
print date_manip[1]
print date_manip[2]
print 'Month: ' + date_manip[0]
print 'Day: ' + date_manip[1]
print 'Year: ' + date_manip[2]
print('Month: ' + date_manip[0] +
      'Day: ' + date_manip[1]
      + 'Year: ' + date_manip[2])

# Need to fix, won't produce proper result, see next attempt.

print('Month: ' + date_manip[0] +
      '. Day: ' + date_manip[1]
      + '. Year: ' + date_manip[2])



'''Ch6: Make a Statement'''


x = 5
print x == 5
print x == 4
print x < 7
print x > 7
print x !=3
print x >= 5
print x <= 5
print x > 5

# Define the variables
x = 10

# Start if statement
if x == 10:
        print 'x = 10'

# If x does not equal 10, but equals 9 run this
elif x == 9:
        print 'x = 9'

# If it's not equal to 10 or 9, run this
else:
        print 'x does not equal 9 or 10'

x = 9

if x == 10:
        print 'x = 10'

# If x does not equal 10, but equals 9 run this
elif x == 9:
        print 'x = 9'

# If it's not equal to 10 or 9, run this
else:
        print 'x does not equal 9 or 10'

x = 1

if x == 10:
        print 'x = 10'

# If x does not equal 10, but equals 9 run this
elif x == 9:
        print 'x = 9'

# If it's not equal to 10 or 9, run this
else:
        print 'x does not equal 9 or 10'



'''Ch7: Going Loopy'''


#Ctrl-C will stop a program stuck in an infinite loop.

# Start counter at 0
counter = 0

# While 'counter' is less than or equal to 5,
# run the loop
while counter < 5:
    # Show counter value
    print counter
    # Shortcut to increase counter by 1
    counter = counter + 1
    # can shortcut above to counter += 1
while counter < 5:
    print counter
    counter += 1
    
# Run loop in range 0 - 5
# Counter changes automatically in each iteration
for counter in range (0,5):
    # Show the value of counter
    print counter
    # It will iterate from 0 through 4, but will not show 5.



'''Ch8: Lists'''


# Create the list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",
                        "Me",]

# print to console
# print "Epic programmers:  " + epic_programmer_list
# the above won't work: TypeError: cannot concatenate 'str' and 'list' objects

# print to console
print "An epic programmer:  " + epic_programmer_list[0]

# print to console
print "An epic programmer:  " + epic_programmer_list[0]
print "An epic programmer:  " + epic_programmer_list[1]
print "An epic programmer:  " + epic_programmer_list[2]
print "An epic programmer:  " + epic_programmer_list[3]
print "An epic programmer:  " + epic_programmer_list[4]
print "An epic programmer:  " + epic_programmer_list[5]

epic_programmer_list.append("Ken Thompson")

# Add this line to show the appended programmer in the console
print "An epic programmer:  " + epic_programmer_list[6]

# Looping through each item in epic_programmer_list
for programmer in epic_programmer_list:
    # Print the programmers' name to console
    print programmer

for programmer in epic_programmer_list:
    print "An epic programmer:  " + programmer

# Create list of numbers
number_list = [1,2,3,4,5]

# Loop each number in number_list
for x in number_list:
    # Print each number to the power of 2
    print x**2

# Create list of numbers
number_list = [1,2,3,4,5]
empty_number_list = []

# Loop each number in number_list
for x in number_list:
    # Append each number to the power of 2
    # to the empty_number list
    empty_number_list.append(x**2)
    print empty_number_list

# Print final list having entered each number in number_list
print empty_number_list



'''Ch9: Writing a Dictionary'''


dictionary_name = {'item_1':1,'item_2':2, 'item_3':3}
print dictionary_name['item_1']

epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds' : 'lt@gmail.com',}

print epic_programmer_dict
print epic_programmer_dict['Tim Berners-Lee']

# Adds a different email address
epic_programmer_dict['Tim Berners-Lee'] = 'tim@gmail.com'
print 'New email for Tim:' + epic_programmer_dict['Tim Berners-Lee']

# Add Larry Page and his email to the dictionary
epic_programmer_dict['Larry Page'] = 'lp@gmail.com'

print epic_programmer_dict

epic_programmer_dict['Sergey Brin'] = 'sb@gmail.com'
epic_programmer_dict['Me'] = 'sa@gmail.com'
epic_programmer_dict['Dan Tower'] = 'dt@gmail.com'

print epic_programmer_dict

# If you want to delete an item in the dictionary use method del.
# del epic_programmer_dict['Sergey Brin'] - as an example.

del epic_programmer_dict['Sergey Brin']
print epic_programmer_dict



'''Ch10: Learn to Function'''


#Example: Outline of a function
# def someFunction(< input variables >):
#    < Do stuff here with input variables >
#    return < some value>

def letsAdd(x,y):
    addition = x + y
    return addition

print letsAdd(3,5)

def letsAdd(x,y):
    addition = x + y
    someValue = 10
    return addition

#print someValue will not work, the variable is not defined
# out of the scope of this function.
'''  File "<pyshell#5>", line 1, in <module>
       print someValue
   NameError: name 'someValue' is not defined'''

someValue = 5
print letsAdd(3,5)
print someValue

# Make function called subtraction
def subtraction(x,y):
    # Make subtract variable equal to x - y
    subtract = x - y

    # Return subtract variable
    return subtract

print subtraction(10,4)

def moreSubtraction(x,y,z):
    # Make subtract variable equal to x - y - z
    subtract = x - y - z

    # Return subtract variable
    return subtract

print moreSubtraction(40,3,11)

def multiplication(x,y):
    multiply = x * y

    return multiply

print multiplication(5,6)

def division(x,y):
    divide = x / y

    return divide

print division(39,3)

# Division results in rounding of integers to the nearest whole number.
# For division to return decimal numbers use
# divide = float(x)/float(y)

length = len("How epic are built-in functions, huh?")
print length

length = len("How epic was Trump's domination on Super Tuesday?")
print length

x = 23
print str(x)

x = 2.32
print str(x)

y = float(40)/float(7)
print y

#returns integer
yInt = int(y)
print yInt

#rounds to the next whole number but does not return integer.
print round(y)

#rounds to the next whole number - returns integer.
print int(round(y))



'''Ch11: Importing Modules'''


import math

print math.sqrt(16)

from math import sqrt, exp

print sqrt(16)
print exp(2)

# exp() calculates 'e' to the power of something.  
# 'e' is a constant of approx 2.71828


# You can create python modules by saving scripts into a new pyfile and calling
# the file.
'''Script Example: named - smallMathsModule.py'''
# Import the function randint from the Python random module
from random import randint

def multiplyBy5(x):
    return 5*x

def add5(x):
    return x+5

def randomAdd(x):
# Get a random integer between 0 and 10
    y = randint (0,10)
    return x+y


# In new file, Import our module - smallMathsModule

import smallMathsModule

print smallMathsModule.add5(4)

print smallMathsModule.randomAdd(7)

print smallMathsModule.multiplyBy5(2)



'''Ch12: Make a Program'''


# Our epic programmer dict from before
epic_programmer_dict = {
    'Tim Berners-Lee'  : 'tbl@gmail.com',
    'Guido van Rossum'  : 'gvr@gmail.com',
    'Linus Torvalds'  : 'lt@gmail.com',
    'Larry Page'  : 'lp@gmail.com',
    'Sergey Brin'  : 'sb@gmail.com',
    }

print epic_programmer_dict

# Our epic programmer dict from before
epic_programmer_dict = {
    'Tim Berners-Lee'  : ['tbl@gmail.com', 111],
    'Guido van Rossum'  : ['gvr@gmail.com', 222],
    'Linus Torvalds'  : ['lt@gmail.com', 333],
    'Larry Page'  : ['lp@gmail.com', 444],
    'Sergey Brin'  : ['sb@gmail.com', 555],
    }

print epic_programmer_dict

print epic_programmer_dict['Tim Berners-Lee']

print epic_programmer_dict['Tim Berners-Lee'][1]

programmer = epic_programmer_dict['Tim Berners-Lee']
print programmer[1]

# Let user enter name through Python raw_input() function.

personsName = raw_input('Please enter a name:  ')
print personsName

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if
    # there are no errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print personsInfo

except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

# Our epic programmer dict from before
epic_programmer_dict_1 = {
    'tim berners-lee'  : ['tbl@gmail.com', 111],
    'guido van rossum'  : ['gvr@gmail.com', 222],
    'linus torvalds'  : ['lt@gmail.com', 333],
    'larry page'  : ['lp@gmail.com', 444],
    'sergey brin'  : ['sb@gmail.com', 555],
    }

print epic_programmer_dict_1

personsName = raw_input('Please enter a name:  ').lower()
print personsName

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if
    # there are no errors then it runs
    personsInfo = epic_programmer_dict_1[personsName]
    print personsInfo

except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if
    # there are no errors then it runs
    personsInfo = epic_programmer_dict_1[personsName]
    print 'Name:  ' + personsName.title()
    print 'Email:  ' + personsInfo[0]
    print 'Number:  ' + str(personsInfo[1])

except:
    # If there are errors then this code gets run.
    print 'No information found for that name'

# Our epic programmer dict from before
epic_programmer_dict_2 = {
    'tim berners-lee'  : ['tbl@gmail.com', 111],
    'guido van rossum'  : ['gvr@gmail.com', 222],
    'linus torvalds'  : ['lt@gmail.com', 333],
    'larry page'  : ['lp@gmail.com', 444],
    'sergey brin'  : ['sb@gmail.com', 555],
    }

def searchPeople(personsName):
    # Looks up the name in the epic dictionary
    try:
        # Tries the following lines of texts,
        # and if there aren't any errors
        # then it runs
        personsInfo = epic_programmer_dict_2[personsName]
        print 'Name:  ' + personsName.title()
        print 'Email:  ' + personsInfo[0]
        print 'Number:  ' + str(personsInfo[1])
    except:
        # If there are errors, then this code gets run.
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    # Asks user to input persons name
    personsName = raw_input('Please enter a name:  ').lower()

    # Run our new function searchPeople with what was typed in
    searchPeople(personsName)
    userWantsMore = False

    # See if user wants to search again
    searchAgain = raw_input('Search again? (y/n)')

    # Look at what they reply and act accordingly
    if searchAgain == 'y':
        # userWantsMore stays as true so loop repeats
        userWantsMore = True
    elif searchAgain == 'n':
        # userWantsMore turns to False to stop loop
        userWantsMore = False

    else:
        # user inputs an invalid response, so we quit anyway
        print "I don't understand what you mean, quitting"
        userWantsMore = False




