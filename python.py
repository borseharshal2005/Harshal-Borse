# What is python - python is high level , interpreted language ,and easy to learn programming language to created by Guido Van Russam in 1991.
# It widely use  of 1. Web Devlopment 2. data science  3 . artificial intelligence , 4. automation , 5. scientific computing , 6.software devlopemnt

# This program display the message "Hello, Harry !" on the screen
# print("Hello, Harray !")

# print("---------------- Variable ----------------")
# # What is variable - Variable is a named memory location used to store data. Its value can be changed during program execution. - Doesnot start keyword ,number and space.

a = 10  # a  is variable_name and 10  is a value of the variable  - Its a Integer type
price = 3.14  # float type
name = "Harry"  # -  String
is_Harry = True  # bool Type
num = 3 + 4j  # complex number
fruits = ["Apple", "Banana", "Mango"]  # list
colors = ("Red", "Green", "Blue")  # Tuple
numbers = {1, 2, 3, 4}  # set
student = {"name": "Harshal", "age": 20}  # Dictinary


print(" --------- Taking a Input in python-----------")
# Input is  used to take input from the user through

name = input("Enter your name : ")
print("Hey", name)  # -> Suppose input is a "Javad" So print - "Hey Javad"
age = int(input("Enter the age :"))  # Integer Value
price = float(input("Enter the Pi Value "))  # Floating


import math
print("--------- Type conversion in python---------")

# Type Conversion means changing the one datatype to another datatype - ex int convert the str ,str convert the int etc.

# string to Integer
x = "100"
y = int(x)
print("y:", y)  # y: 100
print(type(y))  # <class 'int'>
print(type(x))  # <class 'str'>

# number to bool
x = 1
y = bool(x)
print(y)  # True
print(type(y))  # <class 'bool'>


print("----------- String --------------")
# String is sequence of the character enclosed in single quotes '' , double quotes "" , triple quotes ''' ''' , """ """ .
print('Hey, Tony')
print("Hello Stark")
print(""" """)  # mostly use multiline string
print(" ---- Indexing,Slicing--------")
name = 'Harry Potter'
print(len(name))
print(name[1])  # indexing start from - 0 So print -> H
print(name[-1])  # it's a negative indexing start from  -1 So print "r"
print(name[1:4])  # arr
print(name[5:1])  # No error ,its means empty string
print(name[1:8:2])  # [start:end:stop] -> ar o
print(name[-1:-5:-1])  # rett
print(name[::-1])  # reverse the string -> rettoP yrraH
print(name[::2])  # HryPte
print(name[1:-1])  # arry Potte

print("------ Formatted Strings ----------")
name = "Harshal"
print(f"Hey  {name}")  # Hey Harshal

age = 20
# My name is Harshal and I am 20 years old.
print(f"My name is {name} and I am {age} years old.")
print(f"{len(name)}{age}")  # 720

a, b = 10, 2
print(f"Addition =  {a + b}")  # Addition = 12

pi = 3.14159
print(f"Value of pi = {pi:.2f}")  # Value of pi = 3.14

first, last = "Tony", "Stark"
print(f"{first}" + f"{last}")  # TonyStark
print(f"{len(first) + len(last)}")  # 9
print(f"{first} {last}")  # Tony Stark

print("---------Strings Method----------")
you = "Harshal Borse"
print(len(you))  # 13
print(you.upper())  # HARSHAL BORSE
print(you.lower())  # harshal borse
# Harshal Borse  -> convert the first letter of each word to uppercase
print(you.title())
# Harshal borse -> Converts the first letter to uppercase.
print(you.capitalize())
print(you.strip())  # - > REmove the space form both ends -> " Harshal Borse"
print(you.replace("Borse", "Satish Borse"))  # Harshal Satish Borse
print(you.find("H"))  # 0
print(you.count("h"))  # 1
print(you.split(","))  # ['Harshal Borse']
print(you.startswith("Ha"))  # True -> print("Ha" in you)
print(you.endswith("Bo"))  # False -> print("Br" in you)

print("-------- Arithmetic Operator ------------")
print(10 + 2)  # 12
print(10 - 2)  # 8
print(10 * 2)  # 20
print(10 / 2)  # 5.0
print(10 % 2)  # 0
print(10 // 2)  # 5
print(10 ** 2)  # 100
x = 10
x = x + 2
print(x)  # 12

print("--------operator precedence ----------")
num = 5 + 2 * 3  # 2 * 3 is evaluated first, then 5 + 6.
print(num)  # 11
print((5 + 2) * 3)  # 21 -> Parentheses are evaluated first.
print(2 ** 3 + 1)  # 9 -> 2 ** 3 = 8, then 8 + 1 = 9.
print(10 > 5 and 8 < 12)  # True

print("--------Math Function - abs,round,max,min etc ------------")
print(abs(-10))  # print positive value  -> 10
print(round(1.2))  # print nearest intger -> 1
print(max(10, 20, 30))  # max number -> 30
print(min(10, 20, 30))  # min number -> 10
print(math.sqrt(25))  # 5.0
print(math.ceil(1.2))  # next integer -> 2


print("---------- if statement ----------")
age = 18
if age >= 18:
    print("you are eligible to vote !")

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")  # It's a cold day   ,Enjoy your day
else:
    print("It's a lovely day")
print("Enjoy your day")

print("-----short circuit evalutions")
# short circuit evallutions means it's a feature of python where logical expression (and ,or ) stop evalution as soon as the final result is know
age = 18
if age >= 18 and age < 60:  # check the first condition is False, python does not check the second condition
    print("Eligible")
else:
    print("Not Eligible")

print("================")

age = 20
if age >=18 or age < 60: # If first condition is True,python does not check the second condition
    print("Condition is True")


print("---------- logical operator ------------")

print(10 > 20 and 10 > 9)  # False
print(15.5 > 20 or 12 > 20)  # False
print(not (10 > 20))  # True
print("a" > "A" and "b" > "a")  # True
print(not ("abc" > "cba"))  # True

print("---------- comparison operator ------------")

print(2 == 2)  # True
print(2 != 2)  # False
print(3.4 > 3.14)  # True
print(12345 < 1234.99)  # False
print(18 >= 18)  # True
print(21 <= 21)  # True

age = int(input("Enter your age: "))
if age == 18:
    print("You are exactly 18 years old. You are eligible to vote.")

elif age > 18:
    print("You are older than 18. You are eligible to vote.")

elif age < 18:
    print("You are under 18. You are not eligible to vote.")

username = input("Enter the Username: ")
password = input("Enter the Password: ")

if username == "Harshal" and password == "Harshal2580":
    print("Access Granted")
else:
    print("Try Again")

print("---------chaining comparsion operator ------------")
age = 22
if age <= 18 < 65:
    print("Eligible")

print("---------- While loop ----------------")
count = 5
while count > 0:  # check 5,4,3,2,1,than 0 stop the program
    print(count)
    count -= 1
print("Time's Up")

password = ""
while password != "python":
    password = input("Enter Password: ")

print("Access Granted")

i = 1
while i <= 5:
    print("*" * i)
    i = i + 1

print("------------ for loop ---------------")
# range(5) → 0, 1, 2, 3, 4
# range(1, 6) → 1, 2, 3, 4, 5
# range(2, 11, 2) → 2, 4, 6, 8, 10

for i in range(1, 6):  # -> 1,2,3,4,5
    print(i)
for i in range(6, 0, -1):  # -> 6,5,4,3,2,1
    print(i)

prices = [10, 20, 30]
total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")

print("------- nested loop ----------")
for x in range(4):  # -> 0,1,2,3
    for y in range(3):  # -> 0 ,1,2,
        print(f'({x},{y})')

print("-------- function --------")
# function - function is a block of code that perform the specific task. It helps avolid writing the same code multiple lines .


def greet():  # function without parameters

    print("Hi,Harry :)")  # -> Hi,Harry :)


greet()


def greet(name, age):  # -> Parameters
    print("Name:", name, "\nAge:", age)


greet("Harshal", 20)  # -> Arguments   -> This is positional arguments

print("--------Keywoord Argument ------------")
# Keyword arguments are arguments passed to a function by specifying the parameter name


def student(name, age):
    print(f"Name : {name}")
    print(f'Age : {age}')


# function_name(parameter1=value1, parameter2=value2)   ->
student(name="Harshal", age=20)
student(age=20, name="Harshal")  # -> In different order

print("--------default arguments ------------")


def greet(name="Tony"):  # No have a argument So print default argumment
    print("Hello", name)  # -> Hello Tony


greet()  # without argument


def greet(name="Guest"):  # this is default argument
    # so first check the the (positioanl)argument it's valid to print "Hello Harshal" And It's not valid than print default argument
    print("Hello", name)


greet("Harshal")  # with argument

print('--------xargs -------------')

# *args allows a function to accept any number of positional arguments.
# The arguments are stored as a tuple.


def numbers(*args):
    print(args)  # (1, 2, 3, 4)


numbers(1, 2, 3, 4)


def fruits(*args):
    for item in args:
        print(item)  # all fruits print sepreatly


fruits("Apple", "Mango", "Graphs")
