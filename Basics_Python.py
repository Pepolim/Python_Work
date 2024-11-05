# comments
"""
comments
everything 
between
"""
#------------
#DATA TYPES
#------------

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

# In Python, the data type is set when you assign a value to a variable:
x = "Hello World" # str  "" or '' do the same thing
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name" : "John", "age" : 36} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # 	bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview
x = None # NoneType

#------------
#OUTPOUT & PRINTING
#------------

#normal print
print('hello world')
print('4.5', "hello", 87, False, x, end='\n') # coma to separate, it ads a space between

#------------
#USER INPUT
#------------

name = input('Name: ')
age = input('Age: ')
print('Hello', name, 'you are', age, 'years old')

#------------
#ARITHMETIC OPERATORS
#------------

x = 9
y = 3
#Basic operatores + , - , *, /
#exponents  x ** y    - x to the power of y
#floor division  x // y
#mod  x % y   - rest of division
result = int(x / y) 
print(result)

#Order of operations BEDMAS
#B brackets
#E exponents
#D division
#M multiplication
#A addition
#S subtraction

num = input('Number: ') #it gets a string
print(int(num) - 5)

#------------
#STRING METHODS
#------------

hello = 'hello'
print(type(hello.lower()))

#.upper() -> upercases all characters in the string
#.lower() -> downcases all characters in the string
#.capitalize() -> upercase the first characters and downcases the rest in the string
#.count() -> counts the characters in the string we can specify the character, WARNING .count('l') is only going to search the lowercase l
print(hello.lower().count('ll')) # We can just lower case everything to search the lower case ls

#------------
#STRING MULTIPLICATION & ADDITION
#------------

x = 'hello'
y = 3
z = 'yes'
print(x * y) #multiplies the times its gonna print hello
print(x + z) #concatenation of strings

#------------
#CONDITIONAL OPERATORES
#------------
#There are more but these are the core
#  ==  | equality
#  !=  | not equal to
#  <=  | less than equal to
#  >=  | greater than equal to
#  <   | less than
#  >   | greater than

print('a' > 'Z')
print(ord('a')) # ord() to see the value of the character in the ASCII table

#------------
#CHAINED CONDITIONALS
#------------

x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or not result2 and result3 
# OR  = if any of them is true then the result4 is true
# NOT = reverse to the other, example: if it is false then it becomes true
# AND = if both are true then it becomes true else its false
# ORDER OF OPERATIONS, NOT, AND, OR

#------------
# IF / ELSE / ELIF
#------------

#if condition:
    #result
#elif:
    #another result
#elif:
    #another result
#else:
    #other result

# ONLY 1 IF and 1 ELSE, u can use as many ELIF as u want

#------------
# COLLECTION / CONTAINERS
#------------
# LIST & TUPLES
#------------

#lists
x = [4, True, 'hi']
print(len(x)) # lenght of the list, how many thing are in the list, if used on a string u get the quantity of characters there

x.append('hello') # adds something to the end of the list
x.extend([4,5,45,5,4,54,45]) # adds another list to the end of the list
x.pop() # remove and return the last elemente of the list
x.pop(0) # remove the first elemente of the list

#tuples its a list that cant be changed once defined

y = (0,0,3,3)
#y[0] = 5   doesnt work because u cant change it
print(y[0])

#we can have list inside list x = [[8,9,4], [2,6,5], (1,1,1)]

#------------
# FOR LOOPS
#------------

# WE USE FOR LOOPS WHEN WE KNOW HOW MANY TIME IT'S GOING TO LOOP

for i in range(10): #range as start, stop, step, if we only use one number it is the stop, step is the incremente. 
    print(i)        #EXAMPLE: range(1,10,2) starts at 1, stops at 10, increments by 2 (1,3,5...), we can use negative numbers
    
#example with list
x = [3,5,47,9,85,5]

for i in range(len(x)):
    print(x[i])
    
#fancy version
for i, element in enumerate(x):
    print(i, element)
    
#------------
# WHILE LOOPS
#------------

# WE USE WHILE LOOPS WHEN WE DON'T KNOW HOW MANY TIME IT'S GOING TO LOOP

i = 0
while True:
    print('run')
    i += 1
    if i == 10:
        break
    
#------------
# SLICE OPERATOR
#------------

x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"

sliced = x[0:4:2] # START : STOP : STEP
print(sliced) # its going to print [0,2]

# we can reverse lists with this
sliced = x[::-1] # START : STOP : STEP
print(sliced)

#------------
# SETS
#------------

# Unordered unique colection of elements
# use only in situations u care if something exists or doesn't
# they are very fast

# x - set()

#------------
# DICTIONARIES
#------------

# x = {'key': value}

x = {'key': 4}
print(x['key'])

x['key2'] = 5
x[2] = 8
x[3] = [2,2,1,2]
print(x)

print('key' in x)
print(list(x.values()))
print(list(x.keys()))

del x['key']
print(x)

for key, value in x.items():
    print(key, value)
    
for key in x:
    print(key, x[key])
    
#------------
# COMPREHENSIONS
#------------

x = [x for x in range(5)]
print(x) # result = [0, 1, 2, 3, 4]

x = [x + 5 for x in range(5)]
print(x) # result = [5, 6, 7, 9, 10]

x = [x % 5 for x in range(5)]
print(x) # result = [0, 1, 2, 3, 4]

x = [[0 for x in range(100)] for x in range(5)]
print(x) # result = alot of lists with 0

x = [i for i in range(100) if i % 5 == 0]
print(x) # result = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95] all the increments of 5

#------------
# FUNCTIONS
#------------

def func(x, y, z=None):
    print('run', x, y, z)
    return x * y , x / y

print(func(5, 6, 7))
r1, r2 = func(5, 6)
print(r1, r2)

#------------
# UNPACK OPERATOR / *ARGS AND **KWARGS
#------------

def func(x):
    def func2():
        print(x)
    
    return func2

print(func(3)())
#same as 
x = func(3)
x = ()

def func(*args, **kwargs):
    print(args, kwargs)

x = [1,23,23156456,56789]
print(x)
print(*x) # * unpacks what we have in lists and tuples, ** is used in dictionaries

func(1,2,3,4,5,one=0, two=1)

#------------
# SCOPE AND GLOBAL
#------------

x = 'tim'

def func(name):
    global x #  VERY RARE TO BE NEEDED
    x = name

print(x)
func('changed')
print(x)

#------------
# EXCEPTIONS
#------------

#raise Exception('Bad')
#raise FileExistsError('no bueno')

#how to handle exceptions

try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('finally')

#------------
# LAMBDA
#------------

#one line anonymous function

x = lambda x, y: x + y

print(x(2,32))

#------------
# MAP AND FILTER
#------------

x = [12,45,78,96,45,678,97,654,789,7645]

mp = map(lambda i: i + 2, x)
print(list(mp))
mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

#------------
# F STRINGS
#------------

x = f'hello {6 + 8} {tim} {67+9}'
print(f'hello {tim}')

#------------
# OBJECT ORIENTED PROGRAMMING
#------------

#------------
# Advance language features
#------------
