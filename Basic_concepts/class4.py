Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #aliasing
>>> a=5
>>> b=a
>>> id(a)
140707182204704
>>> id(b)
140707182204704
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
5
>>> a=5
>>> b=a
>>> a=6
>>> b
5
>>> b=a
>>> b
6
>>> import sys
>>> a="Pinaki"
>>> b=1
>>> b
1
>>> b=a
>>> c=b
>>> b
'Pinaki'
>>> c
'Pinaki'
>>> sys.getrefcount(a)
5
>>> a="qiefu"
>>> a=b
>>> b=a
>>> b=c
>>> sys.getrefcount(a)
4
>>> 
>>> 
>>> 
>>> 
>>> #Weirdness1
>>> a=2
>>> b=a
>>> c=b
>>> 
>>> sys.getrefcount(a)
375
>>> a=73
>>> b=a
>>> c
2
>>> c=b
>>> sys.getrefcount(a)
9
>>> a=420
>>> b=a
>>> c=b
>>> sys.getrefcount(a)
4
>>> #Weirdness2
>>> a=4
>>> b=4
>>> 
>>> 
>>> id(a)
140707182204672
>>> id(b)
140707182204672
>>> a=256
>>> b=256
>>> id(a)
140707182212736
>>> id(b)
140707182212736
>>> a=257
>>> b=257
>>> id(a)
1392606378704
>>> id(b)
1392606378736
>>> # -5 to 256 same id
>>> 
>>> a="haldia"
>>> b="haldia"
>>> id(a)
1392606238448
>>> id(b)
1392606238448
>>> a="haldia inst tech"
>>> b="haldia inst tech"
>>> id(a)
1392606441264
>>> id(b)
1392606441104
>>> a="haldia_inst_tech"
>>> b="haldia_inst_tech"
>>> id(a)
1392606441024
>>> id(b)
1392606441024
>>> #for valid identifiers
>>> 
>>> L=[1,2,3,4]
>>> id(L)
1392606486656
>>> id(1)
140707182204576
>>> id(L[0])
140707182204576
>>> L[2]=1
>>> L
[1, 2, 1, 4]
>>> id(L[2])
140707182204576
>>> a="Hi"
>>> id(a)
1392573934768
>>> a=a+"world"
>>> a
'Hiworld'
>>> id(a)
1392606238448
>>> 
>>> T=(1,2,3)
>>> id(T)
1392606487936
>>> T=T+(2,7,4)
>>> T
(1, 2, 3, 2, 7, 4)
>>> id(T)
1392606604544
>>> 

>>> #cloning
>>> L=[1,2,3]
>>> L1=[:]
SyntaxError: invalid syntax
>>> L1=L[:]
>>> L1.append(5)
>>> L1
[1, 2, 3, 5]
>>> L
[1, 2, 3]
>>> 
>>> 
>>> a=[1,2]
>>> b=[3,4]
>>> c=(a,b)
>>> c
([1, 2], [3, 4])
>>> id(a)
1392606553600
>>> id(b)
1392574989440
>>> id(c)
1392606551424
>>> c[0][0]=100
>>> c
([100, 2], [3, 4])
>>> id(a)
1392606553600
>>> id(c)
1392606551424
>>> 
>>> 
>>> L=[1,2,3]
>>> L.extend(5)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    L.extend(5)
TypeError: 'int' object is not iterable
>>> L.extend([4,5])
>>> L
[1, 2, 3, 4, 5]
>>> 

>>> def(a=1,b=1)
SyntaxError: invalid syntax
>>> def power(a=1,b=1):
	return a**b
prower(2,3)
SyntaxError: invalid syntax
>>> power(2,3)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    power(2,3)
NameError: name 'power' is not defined
>>>  def power(a=1,b=1):
	return a**b
SyntaxError: unexpected indent
>>> def power(a=1,b=1):
	return a**b

>>> power(2,3)
8
>>> power()
1
>>> power(b=3,a=3)
27
>>> power(b=2,a=3)
9
>>> print(1,2,3)
1 2 3
>>> def flexi(*number):
	product=1
	for i in number:
		product=product*i
	print(product)

	
>>> flexi(1)
1
>>> flexi(1,2)
2
>>> flexi(1,2,3,4,5)
120
>>> 
>>> 
>>> def flexi(*number):
	product=1
	print(number)
	print(type(number))
	for i in number:
		product=product*i
	print(product)

	
>>> flexi(1,2,3,4)
(1, 2, 3, 4)
<class 'tuple'>
24
>>> 