Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello Pinaki");
Hello Pinaki
>>> print(Hello)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(Hello)
NameError: name 'Hello' is not defined
>>> print('Hello')
Hello
>>> print(4)
4
>>> print(1,"Hello",3.14)
1 Hello 3.14
>>> print('Hi',sep='-',1,2,3,4)
SyntaxError: positional argument follows keyword argument
>>> print('Hi',1,2,3,4,sep='-)
      
SyntaxError: EOL while scanning string literal
>>> print('Hi',1,2,3,4,,sep='-')
SyntaxError: invalid syntax
>>> print("Hi",1,2,3,4,,sep='-')
SyntaxError: invalid syntax
>>> print(1,2,3,4,,sep='-')
SyntaxError: invalid syntax
>>> print('Hi',1,2,3,4,,sep='/')
SyntaxError: invalid syntax
>>> print('Hi',1,2,3,4,sep='-')
Hi-1-2-3-4
>>> 5+5j
(5+5j)
>>> #List
>>> [1,2,3,4]
[1, 2, 3, 4]
>>> #Dictionaries
>>> {"Name":"Pinaki","Age":21}
{'Name': 'Pinaki', 'Age': 21}
>>> 

>>> #variables
>>> a=5
>>> c=a+6
>>> c
11
>>> #Dynamic typing
>>> 
>>> a=3
>>> a="Haldia"
>>> a
'Haldia'
>>> #Dynamic Binding
>>> 
>>> #user input
>>> name=input("Enter your name")
Enter your namePinaki
>>> print(name)
Pinaki
>>> #by default a input function returns String value
>>> 
>>> #Type conversion
>>> int(5.6)
5
>>> float(6)
6.0
>>> int('123')
123
>>> bool(0)
False
>>> int(5+5j)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(5+5j)
TypeError: can't convert complex to int
>>> int(5+0j)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(5+0j)
TypeError: can't convert complex to int
>>> 
>>> Height=input("Enter Height")
Enter Height34
>>> height
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    height
NameError: name 'height' is not defined
>>> Height
'34'
>>> (int)Height/100
SyntaxError: invalid syntax
>>> int(Height)/100
0.34
>>> #This is temporary
>>> 
>>> #Types of type conversion
>>> 
>>> #Explicit,Implicit
>>> 
>>> 4+4.5
8.5
>>> #This is implicit TC
>>> 
>>> #Type function
>>> typeof(5)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    typeof(5)
NameError: name 'typeof' is not defined
>>> type(5)
<class 'int'>
>>> type({1,2,3,4})
<class 'set'>
>>> type((1,2,3,4))
<class 'tuple'>
>>> 
>>> #Operators
>>> 
>>> #Arithmatic
>>> #Relational
>>> #Logical
>>> #Bitwise
>>> #Assignment
>>> #Membership
>>> 
>>> 4**2  #powerof
16
>>> 5//2  #coverting quotient to integer
2
>>> 3>4
False
>>> 4<=4
True
>>> 4==6
False
>>> 3!=3
False
>>> 3!=90
True
>>> 
>>> 
>>> #Logical
>>> 0 and 1
0
>>> 0 or 1
1
>>> not 1
False
>>> #Bitwise
>>> 
>>> #Works on bit value
>>> 2 | 3
3
>>> 2 ^ 3
1
>>> 2<<5
64
>>> # a++ / ++a does not work in python
>>> 
>>> #membership
>>> 
>>> 'K' in "Kolaghta"
True
>>> 'O' in "Kolkata"
False
>>> 'O' not in "Kolkata"
True
>>> #Literals
>>> 
>>> a=0b0100
>>> a
4
>>> c=0o749
SyntaxError: invalid digit '9' in octal literal
>>> c=0o342
>>> c
226
>>> a=1.4e5
>>> a
140000.0
>>> 
>>> x=None
>>> x
>>> 3 and 4
4
>>> 