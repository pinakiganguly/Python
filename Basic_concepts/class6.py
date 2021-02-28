Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # lambda functions
>>> x=lambda x:x**2
>>> x(9)
81
>>> a=lambda x,y:(x+y)
>>> a(4,5)
9
>>> #Differnece
>>> #1. has no return value
>>> #2. one line
>>> #3. Not used for code reusability
>>> #4. No name
>>> 
>>> b=lambda x:x[0]=='a'
>>> b("apple")
True
>>> b("how")
False
>>> b=lambda x:"Even" if x%2==0 else "odd"
>>> b(3)
'odd'
>>> b(6)
'Even'
>>> 
>>> 
>>> #Higher order functions
>>> 
>>> 
=== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/lambda1.py ===
88
235
45
>>> #map
>>> L=[1,2,3,4]
>>> map(lambda x:x*2,L)
<map object at 0x0000016D92F72730>
>>> list(map(lambda x:x*2,L))
[2, 4, 6, 8]
>>> list(map(lambda x:x%2==0,L))
[False, True, False, True]
>>> 
>>> 
>>> #filter
>>> L=[1,2,3,4,5,6,,7,89,5,32]
SyntaxError: invalid syntax
>>> L=[1,2,3,4,5,6,7,89,5,32]
>>> list(filter x:x>4,L)
SyntaxError: invalid syntax
>>> list(filter (lambda x:x>4,L))
[5, 6, 7, 89, 5, 32]
>>> 
>>> fruits=['Apple','Orange','Mango','Guava']
>>> 
>>> list(filter(lambda fruit: 'e'in fruit,fruits))
['Apple', 'Orange']
>>> 
>>> #reduce
>>> import functools
>>> L
[1, 2, 3, 4, 5, 6, 7, 89, 5, 32]
>>> functools.reduce(lambda x,y:x+y,L)
154
>>> L1=[12,34,56,11,21,58]
>>> L1
[12, 34, 56, 11, 21, 58]
>>> functools.reduce(lambda x,y:x if x>y else y,L1)
58
>>> L
[1, 2, 3, 4, 5, 6, 7, 89, 5, 32]
>>> L1=[items*2 for item in L]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    L1=[items*2 for item in L]
  File "<pyshell#46>", line 1, in <listcomp>
    L1=[items*2 for item in L]
NameError: name 'items' is not defined
>>> L1
[12, 34, 56, 11, 21, 58]
>>> L1=[item*2 for item in L]
>>> L1
[2, 4, 6, 8, 10, 12, 14, 178, 10, 64]
>>> fruits
['Apple', 'Orange', 'Mango', 'Guava']
>>> L4=[fruit for every fruit in fruits if fruit[0]=="O"]
SyntaxError: invalid syntax
>>> L4=[fruit for fruit in fruits if fruit[0]=="O"]
>>> L4
['Orange']
>>> D
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> D={"Name":"Pinaki","Gender":"Male","Age":21}
>>> D.items()
dict_items([('Name', 'Pinaki'), ('Gender', 'Male'), ('Age', 21)])
>>> D1={key:value for key,value in D.items() if len(key)>3}
>>> D1
{'Name': 'Pinaki', 'Gender': 'Male'}
>>> L
[1, 2, 3, 4, 5, 6, 7, 89, 5, 32]
>>> D2={item*item**2 for item in L}
>>> D2
{64, 1, 32768, 8, 704969, 343, 216, 27, 125}
>>> D2={item:item**2 for item in L}
>>> D2
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 89: 7921, 32: 1024}
>>> D3={item:item**2 for item in L if item%2==0}
>>> D3
{2: 4, 4: 16, 6: 36, 32: 1024}
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/exception1.py =
division by zero
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/exception1.py =
division by zero
HJi
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/exception1.py =
5.0
HJi
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/exception1.py =
name 'city' is not defined
HJi
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/exception1.py =
Variable not declared!
HJi
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/exception1.py =
Division by 0 not possible
HJi
>>> 
===================== RESTART: C:/Python/Python38/file1.py =====================
>>> 
===================== RESTART: C:/Python/Python38/file1.py =====================
>>> 
===================== RESTART: C:/Python/Python38/file1.py =====================

 PINAKI GANGULY
 PINAKI GANGULY
>>> 
===================== RESTART: C:/Python/Python38/file1.py =====================

 PINAKI GANGULY
 PINAKI GANGULY
>>> 
===================== RESTART: C:/Python/Python38/file1.py =====================
File not found
>>> 
==== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/thread.py ===
11

48

279

1664

12525

36216

34349

51264

72981

1000100

>>> 