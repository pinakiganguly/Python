Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Functions as object
>>> 
>>> def f(num):
	return num**2

>>> f(2)
4
>>> x=f
>>> x
<function f at 0x000001A6CE375790>
>>> x(20)
400
>>> del x
>>> f
<function f at 0x000001A6CE375790>
>>> f(2)
4
>>> del f
>>> f(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    f(3)
NameError: name 'f' is not defined
>>>  def f(num):
	return num**2
SyntaxError: unexpected indent
>>> 
>>> def f(num):
	return num**2

>>> type(f)
<class 'function'>
>>> L=[1,2,3,f]
>>> L
[1, 2, 3, <function f at 0x000001A6CE3DF670>]
>>> L[-1](2)
4
>>> L=[1,2,3,4,x(40)]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    L=[1,2,3,4,x(40)]
NameError: name 'x' is not defined
>>> L=[1,2,3,4,f(40)]
>>> L
[1, 2, 3, 4, 1600]
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
30
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
120
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
120
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
Traceback (most recent call last):
  File "C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py", line 28, in <module>
    pallin("malayalam")
  File "C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py", line 24, in pallin
    palin(text[1:-1])
NameError: name 'palin' is not defined
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
Traceback (most recent call last):
  File "C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py", line 28, in <module>
    pallin("malayalam")
  File "C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py", line 24, in pallin
    pallin(text[1:-1])
NameError: name 'text' is not defined
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
Pallindeome
Pallindeome
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
144
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
233
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
233
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
24157817
>>> 
== RESTART: C:/Users/pinak/Desktop/Study/College_Training/Python/recursion.py ==
24157817
20.154146432876587
>>> 