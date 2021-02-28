Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sent1="Let's chill"
>>> sent1
"Let's chill"
>>> sent2="""Hello"""
>>> sent2
'Hello'
>>> city="Kolkata"
>>> city[0]
'K'
>>> city[-1]
'a'
>>> city[-7]
'K'
>>> city[0:3]
'Kol'
>>> city[4:]
'ata'
>>> city[:2]
'Ko'
>>> city[0:6:2]
'Kla'
>>> city[-1:-5:2]
''
>>> city
'Kolkata'
>>> city[-4:-1:2]
'kt'
>>> city[:]
'Kolkata'
>>> city[::-1]
'atakloK'
>>> #reverse
>>> 
>>> 
>>> city[-1]='x'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    city[-1]='x'
TypeError: 'str' object does not support item assignment
>>> #strings are immutable in python
>>> #Add also not possible in string
>>> city=city+"xyz"
>>> city
'Kolkataxyz'
>>> city
'Kolkataxyz'
>>> id(city)
2554830878320
>>> city="Kolkata"
>>> city
'Kolkata'
>>> id(city)
2554830934320
>>> 
>>> 
>>> #Delete
>>> del city
>>> city
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    city
NameError: name 'city' is not defined
>>> city="Kolkata"
>>> del city[0:3:2]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del city[0:3:2]
TypeError: 'str' object does not support item deletion
>>> city+" "+"Pine
SyntaxError: EOL while scanning string literal
>>> city+" "+"Pine"
'Kolkata Pine'
>>> city*3
'KolkataKolkataKolkata'
>>> "Mumbai">"Kolkata"
True
>>> "Vizag">"vizag"
False
>>> for i in "Kolkata":
	print(i)

K
o
l
k
a
t
a
>>> 'o' in "Kolkata"
True
>>> len(city)
7
>>> city=" Kolkata"
>>> len(city)
8
>>> min(city)
' '
>>> min("Vizag")
'V'
>>> sorted("Mumbai")
['M', 'a', 'b', 'i', 'm', 'u']
>>> sorted('Mumbai',reverse=True)
['u', 'm', 'i', 'b', 'a', 'M']
>>> 
>>> 
>>> #Capitalized
>>> 
>>> sent4="let's swim today"
>>> sent4.capitalize()
"Let's swim today"
>>> sent4.title()
"Let'S Swim Today"
>>> 
>>> 
>>> #Count
>>> 
>>> sent5="I am very very happy"
>>> sent5.count('very')
2
>>> sent5.find('very')
5
>>> #Format
>>> 
>>> "Hi{}".format(city)
'Hi Kolkata'
>>> "{}has 1.3billion people".format("India")
'Indiahas 1.3billion people'
>>> "{1} has 1.3 billion people and {2} is the capital".format(city,"India","Delhi")
'India has 1.3 billion people and Delhi is the capital'
>>> "{a} is a big country".format(a="India")
'India is a big country'
>>> sent5
'I am very very happy'
>>> semt6.index("happy)
	    
SyntaxError: EOL while scanning string literal
>>> sent6.index("happy")
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    sent6.index("happy")
NameError: name 'sent6' is not defined
>>> sent5.index("happy")
15
>>> "Hi5".isalnum()
True
>>> "Hi".isalpha()
True
>>> "5.0".isdecimal()
False
>>> "5".isdecimal()
True
>>> "5.9".isdigit()
False
>>> "4".isdigit()
True
>>> 
>>> 
>>> #split
>>> sent5
'I am very very happy'
>>> sent5.split()
['I', 'am', 'very', 'very', 'happy']
>>> sent5.split("very")
['I am ', ' ', ' happy']
>>> #split is used in natural language processing
>>> 
>>> sent5.split(" ")
['I', 'am', 'very', 'very', 'happy']
>>> #split used in 'Quora'
>>> 
>>> #Join
>>> 
>>> ".".join(['I', 'am', 'very', 'very', 'happy'])
'I.am.very.very.happy'
>>> 
>>> 
>>> #Replace
>>> 
>>> "India is a huge country".replace("India","USA")
'USA is a huge country'
>>> sent6="India is a huge country"
>>> sent6.replace("India","USA")
'USA is a huge country'
>>> sent6
'India is a huge country'
>>> name="-----------Pinaki-------------"
>>> name.strip()
'-----------Pinaki-------------'
>>> name="            Pinaki    "
>>> name.strip()
'Pinaki'
>>> 
>>> 

>>> #List
>>> 
>>> L=[]
>>> L
[]
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> l=["h",3.4,4,"rr"]
>>> l
['h', 3.4, 4, 'rr']
>>> 
>>> #Multi-dimensional List
>>> 
>>> #2D
>>> l1=[1,2,3,[4,5]]
>>> l1
[1, 2, 3, [4, 5]]
>>> 
>>> #3d list
>>> l2=[1,2,[4,5],[["s","t"]]]
>>> l2
[1, 2, [4, 5], [['s', 't']]]
>>> type(l2)
<class 'list'>
>>> L3=list("Haldi")
>>> L3
['H', 'a', 'l', 'd', 'i']
>>> L
[]
>>> l
['h', 3.4, 4, 'rr']
>>> l[0]
'h'
>>> l[-1]
'rr'
>>> l[::-1]
['rr', 4, 3.4, 'h']
>>> l[1:5:2]
[3.4, 'rr']
>>> l1
[1, 2, 3, [4, 5]]
>>> l1[-1]
[4, 5]
>>> a=l1
>>> a
[1, 2, 3, [4, 5]]
>>> a=l1[-1]
>>> a
[4, 5]
>>> a[0]
4
>>> l1[-1][0]
4
>>> l1[-1][1]
5
>>> l4=[[[1,2],[3,4],[5,6]]]
>>> l4
[[[1, 2], [3, 4], [5, 6]]]
>>> l4=[[[1,2],[3,4]],[[5,6],[7,8]]]
>>> l4
[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>>> l4[1][1][0]
7
>>> l4[0][1][1]
4
>>> 
>>> 
>>> l
['h', 3.4, 4, 'rr']
>>> l[0]=100
>>> l
[100, 3.4, 4, 'rr']
>>> #Lists are mutable in python
>>> l[-1]
'rr'
>>> l[1:4]=[100,300,400]
>>> l
[100, 100, 300, 400]
>>> l.append(500)
>>> l
[100, 100, 300, 400, 500]
>>> l.extend([5000,6000,7000,"Hello"])
>>> l
[100, 100, 300, 400, 500, 5000, 6000, 7000, 'Hello']
>>> l.append([5,4])
>>> l
[100, 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', [5, 4]]
>>> l.extend("Goa")
>>> l
[100, 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', [5, 4], 'G', 'o', 'a']
>>> l.add(1)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    l.add(1)
AttributeError: 'list' object has no attribute 'add'
>>> l.insert(1)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    l.insert(1)
TypeError: insert expected 2 arguments, got 1
>>> l.insert(1,"India")
>>> l
[100, 'India', 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', [5, 4], 'G', 'o', 'a']
>>> 
>>> 
>>> #Delete
>>> l.del(1)
SyntaxError: invalid syntax
>>> l
[100, 'India', 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', [5, 4], 'G', 'o', 'a']
>>> del l[0]
>>> l
['India', 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', [5, 4], 'G', 'o', 'a']
>>> del l[-4]
>>> l
['India', 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', 'G', 'o', 'a']
>>> del l[-3:-1]
>>> l
['India', 100, 300, 400, 500, 5000, 6000, 7000, 'Hello', 'a']
>>> del l[-3:]
>>> l
['India', 100, 300, 400, 500, 5000, 6000]
>>> l.remove("Hello")
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    l.remove("Hello")
ValueError: list.remove(x): x not in list
>>> l
['India', 100, 300, 400, 500, 5000, 6000]
>>> l.pop()
6000
>>> l
['India', 100, 300, 400, 500, 5000]
>>> l.remove(400)
>>> l
['India', 100, 300, 500, 5000]
>>> l.remove("Hello")
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    l.remove("Hello")
ValueError: list.remove(x): x not in list
>>> l.clear
<built-in method clear of list object at 0x00000252D7CA5240>
>>> l.clear()
>>> l
[]
>>> l=[1,2,3,4]
>>> l1=[4,5,6,7]
>>> l+l1
[1, 2, 3, 4, 4, 5, 6, 7]
>>> l*l1
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    l*l1
TypeError: can't multiply sequence by non-int of type 'list'
>>> l*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> 4 in l1
True
>>> L3=[1,2,3,[4,5]]
>>> L3
[1, 2, 3, [4, 5]]
>>> 4 in L3
False
>>> [4,5] in L3
True
>>> for i in L3:
	print(i)

	
1
2
3
[4, 5]
>>> len(L3)
4
>>> sorted(L3)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    sorted(L3)
TypeError: '<' not supported between instances of 'list' and 'int'
>>> L9=[3,7,1,4,9,2]
>>> L9.sorted()
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    L9.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> sorted(L9)
[1, 2, 3, 4, 7, 9]
>>> L9.sort()
>>> L9
[1, 2, 3, 4, 7, 9]
>>> L9
[1, 2, 3, 4, 7, 9]
>>> L9.index(3)
2
>>> String1="hello how are you"
>>> String1
'hello how are you'
>>> String1.split()
['hello', 'how', 'are', 'you']
>>> split1=String1.split()
>>> split1
['hello', 'how', 'are', 'you']
>>> for i in range split1:
	
SyntaxError: invalid syntax
>>> for i in range (split1):
	print(i.capitalize())

	
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    for i in range (split1):
TypeError: 'list' object cannot be interpreted as an integer
>>> for i in split1:
	print(i.capitalize())

	
Hello
How
Are
You
>>> for i in split1:
	print(i.capitalize(),end=" ")

	
Hello How Are You 
>>> email=abc@gmail.com
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    email=abc@gmail.com
NameError: name 'abc' is not defined
>>> email="abc@gmail.com"
>>> print[:email.index('@')]
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    print[:email.index('@')]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(email([:email.index('@')]))
SyntaxError: invalid syntax
>>> print(email[:email.index('@')])
abc
>>> L10=[1,1,2,2,3,3,4,4]
>>> l1=[]
>>> for i in L10:
	if i not in l1:
		l1.append()
print(l1)
SyntaxError: invalid syntax
>>> for i in L10:
	if i not in l1:
		l1.append(i)
print(l1)
SyntaxError: invalid syntax
>>> for i in L10:
	if i not in l1:
		l1.append(i)
	print(l1)

	
[1]
[1]
[1, 2]
[1, 2]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4]
>>>  for i in L10:
	if i not in l1:
		l1.append(i)
print(l1)
SyntaxError: unexpected indent
>>> for i in L10:
	if i not in l1:
		l1.append(i)
print(l1)
SyntaxError: invalid syntax
>>> for i in L10:
	if i not in l1:
		l1.append(i)
print(l1)
SyntaxError: invalid syntax
>>> L1=[1,2,3,[4,5]]
>>> L1
[1, 2, 3, [4, 5]]
>>> print(str(L1))
[1, 2, 3, [4, 5]]
>>> print(str(list(chain.from_iterable(L1))

L1
	  
SyntaxError: invalid syntax
>>> print(strlist(chain.from_iterable(L1)))
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    print(strlist(chain.from_iterable(L1)))
NameError: name 'strlist' is not defined
>>> print(str(list(chain.from_iterable(L1)))



      l1
      
SyntaxError: invalid syntax
>>> L=[]
>>> for i in L1:
	L.extend(i)
print(L)
SyntaxError: invalid syntax
>>> 
==================== RESTART: C:/Users/pinak/Desktop/qei.py ====================
Traceback (most recent call last):
  File "C:/Users/pinak/Desktop/qei.py", line 4, in <module>
    L.extend(i)
TypeError: 'int' object is not iterable
>>> 
==================== RESTART: C:/Users/pinak/Desktop/qei.py ====================
Traceback (most recent call last):
  File "C:/Users/pinak/Desktop/qei.py", line 4, in <module>
    L.extend(i)
TypeError: 'int' object is not iterable
>>> 