# The first letter of a variable name must be an alphabet or an underscore character
# The first letter of a variable name cannot be a number
# We can use only alphanumeric and underscore characters in a variable name

_ (valid)
1w (invalid)
12 (invalid)
we (valid)
w$e (invalid)

# This is a print statement

# Comments are just needed to explain a line of code
# Comments are not executed in python
print("Python Programming 2")

# Types of values in Python

# 12 (Integer)
# 1.1 (Float)
# 13 (Integer)
# "Python Programming" (A String)
# True (Boolean)
# False (Boolean)
# 2 + 3i (A complex number)

# type is a function is python using which we can find what type of value a variable is

name = 12
print(type(name))

name = 1.1
print(type(name))

name = "Python is a good language"
print(type(name))

name = True
print(type(name))

# Boolean is a data type in all languages

name = complex(2, 3)
print(type(name))

# Single line comment in Python
# There are other types of values also like list, tuple, dictionary
# But we will not learn them now

"""
Multiline comment in Python
Content 1

Content 2

Content 3

print("Hello World")

Whatever you write will not be executed
"""

print("Hello World")

# Variable names

# Reserved words in python = Which are used by Python internally

# while for if else elif float int str ....
# For (Not a reserved word)
# foR is not a reserved word
# for (This is a reserved word)
# Reserve words are also case-sensitive

For = 12

print(For)

# input() method in Python

var = input()

print("Hello World")
print(var)

# A variation of print statement
print("Hello World", "Python Programming", "Next word", 12, 34.5)

var = input()



# A special concept of Type Casting
# Type Conversion

# Can we convert name to an integer?
name = "12"
secondName = int(name)
floatName = float(name)


print("Type of name: ", type(name))
print("Type of secondName: ",type(secondName))
print("floatName: ", floatName, type(floatName))

# Integer to string conversion

name = 12
var = str (name)

print(type(name))
print(type(var))

name = "12"
var = int(name)

print("Type of var: ", type(var))

var = input()

# User has given this input: 12.3

# var = 12.3 (Wrong)

var = "12.3"

print("Type of var: ", type(var))

var = input()

# var = for (Wrong)
var = "for"

print("Type of var: ", type(var))

var = input()

# var = True (Wrong)
var = "True"

print("Type of var: ", type(var))

# Mathematical expressions in Python

# Precedence and Associativity

# 3 + 4 * 10 = 43
# * is done before +

var = 3 + 4 * 10
print(var)

# Modulus operator

var = -2 % 5
print(var)

var = 2 % -5
print(var)

var = 4 % -5
print(var)

# Bitwise operators

# The binary representation of decimal numbers

# 5 is in decimal 
# 5 in binary = 101

# How we convert decimal numbers to binary and binary to decimal

# 9: 1001

# &, |, ^, <<, >>

# & operation

# +, -, *, /

print(9 << 1, 9 >> 1)

print(1011 & 1100)

Discussed Till Now
1. Naming Convention
2. Types of Values
3. input() method
4. Type Conversion
5. Comments in Python
6. Mathematical expressions
7. Binary operators (&, |, ^, <<, >>) and modulus operator

Logical Operators

(and) -> English's and

There are three logical operators:
1. and
2. or
3. not

Lets say A and B are two comparisions.
Then A and B will be true if and only if:
1. A (and) B both are true

A or B will be true:
1. At least any one of them is true

!A will be true:
1. If A is false

Conditional Statements

If Statement

Syntax:

```
if (condition):
  // Statements
```



# The if condition
money = 10

# If money >= 10, I want to print: This much money is enough

if (money >= 10):
  print("This much money is enough")

n = 10

if (n >= 8):
  n = n * 10
  print(n)

n = 10

if (n > 10):
  print("Too much n")

val = 3 + 4 * 10

if (val > 50):
  print("Val is greater than 50")

print("Val:", val)

if (2 & 3):
  print("Yayy", end = " ")

print("Hello World")

print(2 & 3)

if-else in Python

Syntax:


```
if (condition):
  // Statements 1
else:
  // Statements 2
```



n = 10

if (n > 10):
  print("n is greater than 10")
else:
  print("n is smaller than or equal to 10")

print("Hello World")

n = input("Enter n: ")

if (n == 10):
  print("The number you have given is 10")
else:
  print("The number is not ten")

if-elif-else statement



```
if (condition 1):
  // Statements 1
elif (condition 2):
  // Statements 2
elif (condition 3):
  // Statements 3
else:
  // Statements 4
```



n = -2

if (n <= 18):
  print("Child or Teenager")
elif (n <= 40):
  print("Adult")
else:
  print("Senior Citizen")

print("Hello World")

n1 = input("Enter n1: ")
n1 = int(n1)

n2 = input("Enter n2: ")
n2 = int(n2)

n3 = input("Enter n3: ")
n3 = int(n3)

if (n1 >= n2 and n1 >= n3):
  print("n1 is the largest")
elif (n2 >= n1 and n2 >= n3):
  print("n2 is the largest")
elif (n3 >= n1 and n3 >= n2):
  print("n3 is the largest")


Find if the year provided as input is a leap year. If it is a leap year, output "Yes", otherwise "No".

Conditions for leap year:
1. Divisible by 400 
OR
2. Divisible by 4 and not divisible by 100

# Method 1

y = input()
y = int(y)

if (y%400 == 0):
  print("Yes")
elif (y%4==0 and y%100 != 0):
  print("Yes")
else:
  print("No")

# Method 2

y = input()
y = int(y)

if (y%400 == 0 or (y%4 == 0 and y%100 != 0)):
  print("Yes")
else:
  print("No")

Given three numbers as input, find the second largest number.

n1 = input()
n1 = int(n1)

n2 = input()
n2 = int(n2)

n3 = input()
n3 = int(n3)

mx = -1
mn = -1

# what is the maximum number of these three
# What is the minimum number of these three

if (n1 >= n2 and n1 >= n3):
  mx = n1
elif (n2 >= n1 and n2 >= n3):
  mx = n2
else:
  mx = n3

if (n1 <= n2 and n1 <= n3):
  mn = n1
elif (n2 <= n1 and n2 <= n3):
  mn = n2
else:
  mn = n3

if (n1 >= mn and n1 <= mx):
  print(n1)
elif (n2 >= mn and n2 <= mx):
  print(n2)
else:
  print(n3)

n1 = int(input())

n2 = int(input())

n3 = int(input())

if (n1<n2<n3 or n3<n2<n1):
  print(n2)
elif (n2<n1<n3 or n3<n1<n2):
  print(n1)
else:
  print(n3)

n1 = int(input())

n2 = int(input())

n3 = int(input())

if ((n1 > n2 and n1 < n3) or (n1 > n3 and n1 < n2)):
  print(n1)
## We can complete this code

Given three numbers, determine if a triangle can be formed out of them.

a = int(input())
b = int(input())
c = int(input())

if (a+b > c and a+c > b and b+c > a):
  print("Yes")
else:
  print("No")

Given a character as input, determine if it is a vowel.

char = input()

if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
  print("Yes")
else:
  print("No")
print(a)

char = input()

if(char == a or 'e' or 'i' or 'o' or 'u'):
  print("Yes")
else:
  print("No")

# If you are printing a string, it must be under quotes
# If you don't put it under quotes, the compiler will look for a variable named as the word you want to print

print("yes")

Nested if-elif-else conditions


```
if (condition 1):
  if (condition 2):
    // Statements
  else:
    // Statements
elif (condition 3):
  if(condition 4):
    // Statements
```



n1 = 12
n2 = 14

if(n1 != n2):
  if(n1 > n2):
    print("n1 is greater")
  else:
    print("n2 is greater")
else:
  print("both are equal")
  n3 = 12
  print(n3)
  if(n3 == 11):
    print("n3 is equal to 11")
  else:
    print("n3 is not 11")

n1 = int(input())
n2 = int(input())

if (n1 * 10 < n2):


  if(n1 * 20 < n2):


    if(n1 * 30 < n2):
      print("Hello")

      
  else:
    print("Yayy")

n = 13

if (n == 13):

  if (n > 15):
    print("n is greater than 15")
  
  if (n < 10):
    print("n is less than 10")
  
  else:
    print("n is greater than 10")

  else:
    print("n is less than 15")

# Iterative Statements 

Types of Statements in Python:

1. Print Statements
2. Assignment Statements
3. Conditional Statements
4. Iterative Statements
5. Function declaration statements

# Assignment Statements

a = 4
b = 4 * 7 +19
c = 1100 & 1001

# Conditional Statements

if (2 > 3):
  print("Math is weird")

# Iterative Statements

print(2)
print(4)
print(6)
print(8)

Iterative Statements perform the same operation again and again. For example, they will print again and again.

## While loop in Python



```
while (condition):
  // Statements to execute
```



# while loop in python

i = 0
while (i < 10):
  print(i)
  i = i + 1

# Find the digits of a number

n = 9812
print(2)
print(1)
print(8)
print(9)

n = int(input())

while (n > 0):
  digit = n % 10
  print(digit)
  n = n // 10

# Types of Errors

1. Syntax Errors: When the rules defined by Python to write python programs are not followed.
2. Runtime Errors: Errors that occur during runtime due to some wrong algorithm or invalid operation. One example of invalid operation is division by zero.

if True
  print("Yes")

a = 10
b = 0

print(a/b)

print("Python","at","LPU")
print("Python""at""LPU")

# Properties of Python Language

1. Simple Programming Language
2. Easy to learn
3. Free Programming Language
4. Open Source programming language
5. Interpreted programming language (Not compiled prog. lang.)
6. Portable Programming Language

# Keywords in Python

1. Keywords are reserved words in Python.
2. Python2 has 32 keywords.
3. Python3 has 33 keywords.
4. Python 3.7 has 35 keywords (async and await)

# This program display the list of all keywords in Python
import keyword

print(keyword.kwlist)

# How to find out if a word is keyword or not

var = 'for'
print(keyword.iskeyword(var))

var = 'For'
print(keyword.iskeyword(var))

# Docstrings in Python

1. For providing documentation in python
2. It is a simple string that is used to explain what a piece of code does.
3. It is not intended to explain how a piece of code performs an operation.
4. So, it answers that what part not the how part.
5. It is mentioned in the beginning itself
6. According to python coding conventions, a docstring should always start with a capital letter and end with a period (.).
7. It is used to explain the functionality of a method, function, classes, modules, etc.

## Single-line docstrings

def add(a, b):
  """ Adds two numbers."""

  return a + b

def power(e, x):
  '''Returns the power value.'''
  return e ** x

## Multi-line docstrings

def power(e, x):
  """ Returns the power value

  e: It is the base
  x: It is the power.
  """

  print("The power value calculation in progress..")
  return e ** x

# Properties of docstrings

1. All functions are objects in Python and objects have certain properties also known as attributes.
2. \__doc__ attribute holds the value of docstrings that is attached with a function, method, class or module.
3. Properties or attributes of an object are accessed using this synatax:


```
object_name.attribute_name
```



def power(e, x):
  """ Returns the power value

  e: It is the base
  x: It is the power.
  """

  print("The power value calculation in progress..")
  return e ** x

print(power.__doc__)

## Chained Assignment

index = 10

var1 = var2 = var3 = var4 = 10

print(index)

## Multiple Assignments

a, b = 10, 12

index, name, var, lang = 12, 1.5, "Python", "LPU"
print(a)
print(b)

print(lang)

## Augmented Assignment

a = 12
b = 10

# a = a + 5
a += 5

# a = a * b
a *= b

# a = a >> 1
a >>= 1

print(a)

# Indentation in Python

A standard is to give either two spaces or a tab as indentation.

if (True):
    print("Hello")

    a = 10

    a += 6

print(a)

# Strings

1. Strings are nothing but a sequence of characters.
2. There are two standards of Character Encoding: ASCII and Unicode
3. Unicode encodes more number of characters than ASCII.
4. ASCII uses 8 bits for character encoding, however Unicode uses 32 bits for character encoding
5. Python uses Unicode standard of Character Encoding

## How to declare a string in python

1. Under double quotes
""
2. Under single quotes
''
3. Multi-line strings
"""


"""

index = "PYTHON"

index = 'PYTHON'

index = """Hello Everyone

We are in LPU

Learning python
"""

print(index)

## Indexing in strings

name = "python"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


print(name[6]) # Runtime error

## Negative indexing in python

name = "python"
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])

# LPU's batches
name = "LPU's batches"

# "KOC32 Batch"
index = '"KOC32 Batch"'

# Python's "LPU"
example = """Python's "LPU" """

print(name)
print(index)
print(example)

### Escape Characters

name = 'LPU\'s Batches'
index = "\"Python\""

var = "desktop\"python"
print(name)
print(index)
print(var)

print("LPU\nPython")

# Syntax error where the ending quotes are not provided.
print("LPU\")

## String operations

1. \+ operator or concatenation operator
2. reverse function


index = "Python at " + "LPU"

print(index)

# Slicing a string

name = "Python at LPU"

print(name[2:10])

var = "Hello"

# To print ell

substring = var[1:4]
print(substring)

1. When the second index is not provided, the substring starting with the first index till the last is printed.

var = "Hello"

substring = var[1:]
print(substring)

1. Negative indices can be provided as well

var = "Hello"

substring = var[-4:-1]
print(substring)

1. When the indices a, b are like this: a >= b then nothing is printed.

var = "Hello"

# a must be less than b
# a must be less than the length of the string
print(var[3:1])

1. a must be less than the length of the string
2. If b is greater than or equal to the length of the string, whole substring starting with index a till the end is printed.
3. When both: a and b are not provided then the whole string is printed.

# Example of first point

var = "Hello"

print(var[5:10])

# Example of 2nd Point

var = "Hello"

print(var[1:5])

# Example of 3rd point

print(var[:])

1. How to reverse a string.

# Reversing the printed string

var = "Hello"

reversedVar = var[::-1]

print(reversedVar)

# ord() and chr() in Python

1. Using ord() function, we can print the number assigned to a character in Unicode standard of Character Encoding. It is also called ordinal values.
2. Using chr(), we can find the character which is assigned a given number

# ord function: It shows the ordinal values of characters

numberAssignedtoCapitalA = ord('A')
print(numberAssignedtoCapitalA)

var = ord('$')
print("Number assigned to $:", var)

# chr function

char = chr(65)
print(char)

## String update

1. Direct character assignment at any index is not allowed in Python
2. However, strings can be converted to lists and then they can be updated.

var = "Hello"

# Lets changed: Hello to Hemlo
var[2] = 'm'

print(var)

# Two possible ways to update

# 1. Using slicing

var = "Hello"

sub1 = var[0:2]

middleString = "m"

sub2 = var[3:]

print(sub1 + middleString + sub2)

## Delete a string

Using the del keyword

var = "Hello"

del var

print(var)

## Output or String Formatting in Python

1. Using the % syntax
2. Using the str.format() function

## String formatting using % operator

1. This is standard C-style formatting.
2. %: String modulo operator when used with strings

### Argument Specifiers

1. %s: A string argument specifier. It is used to specify that a string value or argument is going to take its place
2. %d: Integer argument specifier.
3. %\<number_of_digits>d: Used to allocate digits to the integer and then integer is printed.
4. %f: This is used to specifier a float is going to take its place.
5. %.\<number_of_digits>f: Floating numbers with fixed number of digits is going to take my place
6. %x or %X: Integers in hexadecimal representation
7. %o: Integers in octal representation

# Example of first point
ex1 = "Python at %s" %"LPU"

# Example of first and 2nd point
ex2 = "%d students passed %s exam" %(90, "Python")

# Example of first, second and 5th point
ex3 = "%d students passed %s exam with %.3f percentage" %(24, "Python", 85.5)

print("ex1:", ex1)
print("ex2:", ex2)
print("ex3:", ex3)

# Example of 3rd point, 4th point
# 1. Six digits are the decimal point, rounded values are there
var = "Python %4d value 123 %f" %(22, 4.2111119111111)

print(var)


# Remaining points

var = "Hex representation of 16: %x" %(16)

ex2 = "Hex representation of 15: %x" % 15

oc1 = "Octal Representation of 12 and 15: %o %o" %(12, 15)
print(var)
print(ex2)

print(oc1)

var = input()

name = "User name is %s" % var

print(name)

## str.format() function

1. It eliminates the need of % operator in strings
2. {} and .format() replace the % operators

### Argument Specifiers
1. Argument specifiers are here as well but they look like this:
2. {}: Any String or object with a string representation like numbers
3. {0: \<number_of_digits>d}: Integers will take my place
4. {0: .\<number_of_digits>f}: Floating point will take my place with only the specified number of digits after the decimal point
5. {0:X}: Integers in hex representation
6. {0:o}: Integers in octal representation
7. {0:b}: Integers in binary representation

# Example of 2nd point
var = "My name is {} and I am a {} in {}".format("Aman", "Mentor", 2022)

print(var)

var = input()

answer = "     {}".format(var)
print(answer)

var = input()

print(4 * " ", var)

# sep argument in print function

# Example of 3rd point

var = "Mary has {0:d} balloons in her {1:d} pockets.".format(20, 3)

print(var)

name = "Rohit has {1:d} other names as well from {2:d} anything {0:d} no sense is here".format(3, 2, 10)

print(name)

# We can also specify the number of digits

name = "Guess my name in {0:10d} attempts.".format(20)

print(name)

# Example of 4th point

var = "{0:d} students passed with {1:f} percentage".format(10, 90.2)

ex2 = "{0:.2f} is a cool number".format(12.246)

print(var)
print(ex2)

# Example of 5th, 6th and 7th points

ex1 = "The octal representation of 18: {0:o}".format(18)

ex2 = "The hex representation of 15: {0:x}".format(15)

ex3 = "The binary representation of 4: {0:10b}".format(4)

print(ex1)
print(ex2)
print(ex3)

# Indexing is allowed inside curly braces
var = "{1} has whatever text {0} putting it {2} there".format("one", "two", "three")

print(var)

1. If you want to put raw values and named values together as arguments in the str.format() function, then put the raw values first and then the named values
2. It is a convention.

# Naming is also allowed

var = "{pr} Agastya Muni has {num} skills at ancient times next number {0}.".format(12, pr = 8, num = 10)

print(var)

num = int(input())

print("{0:b}".format(num))

# divmod() function

print(divmod(11, 3))

## Two's complement and not operator

print(2&3)

print(~6)

# 11110110
# 11110101
# 11110011
# 11101010

## Lists, sets and tuples in Python

### List
1. It is a data type in Python. It is used to store multiple values in a single variable. List is represented by [ ].

# Examples of lists

var = [1, "LPU", "Python", 12.2, complex(1, 2)]

var1 = []

var2 = ["Doe", 12,2, 19]

# How to access the values
# Indexing
var = [1, "LPU", "Python", 12.2, complex(1, 2)]

print(var[0])
print(var[1])
print(var[2])
print(var[3])

# Negative Indexing
var = [1, "LPU", "Python", 12.2, complex(1, 2)]

print(var[-1])
print(var[-2])
print(var[-3])

# Printing a list

var = [1, "LPU", "Python", 12.2, complex(1, 2)]
print(var)
print(*var)

# List Slicing (String Slicing)

var = [1, "LPU", "Python", 12.2, complex(1, 2)]

slicedVar = var[1:3]

s2 = var[1:]

s3 = var[6:10]

s4 = var[:]

print(slicedVar)

print(s2)
print(s3)
print(s4)

# Addition in Lists

l1 = [1, 2, "Python"]
l2 = ["LPU", "Second", 12.2]

additionList = l1 + l2
print(additionList)

# Multiplication operator in Lists

l1 = ["Python", 2] * 10

print(l1)

# Nested Lists

var = [1, "Python", "LPU", 12.2, [12, 5, "Help"]]

print(var[2])

lst = var[4]

print(lst)

# Unique type of indexing
var = [1, "Python", "LPU", 12.2, [12, 5, "Help"]]

elem = var[4][1]

print(elem)

elem2 = var[4][3]

print(elem2)

var = [2, "Python", [1, 4, ["Next level", 12.2]], "Second", "LPU", [3, 1, "Helo"], "LPU"]

print(var[2][2][0])