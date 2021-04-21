import itertools as itera
"""s="Hello#81@21349"
ss=set()
n=-1
for i in s:
    if i.isdigit():
        ss.add(i)
new_set=list(itera.permutations(ss))
for i in new_set:
    k="".join(i)
    if int(k)%2==0 and int(k)>n:
        n=int(k)
print(n)
"""
"""def sortlist(L):
    l=len(L)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if(L[j][1]>L[j+1][1]):
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp
    return L
L1=[]

L=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
sortlist(L)
L1[0:]=L[1][0],L[2][0]
L2=sorted(L1)
for j in range(len(L2)):
    print(L2[j])
"""

#Sum of Factorial of digits of a number is equal to the number iteself
"""
def factorial(number):

    if number==1:
       return 1
    elif number==0:
        return 1
    else:
       return number*factorial(number-1)


def find_strong_numbers(num_list):
    L=[]
    
    for i in num_list:
        temp=i
        sum=0
        while(temp!=0):
            n=temp%10
            k=factorial(n)
            sum=sum+k
            temp=temp//10
        if sum==i:
            L.append(sum)
        else:
            pass
    return L


num_list=[145,375,100,2,10]
print(find_strong_numbers(num_list))
#print(strong_num_list)
"""

#Pair of numbers in list equal to 'n'

"""
def find_pairs_of_numbers(num_list,n):
    count=0
    for i in num_list:
        s=n-i
        if s in num_list:
            count+=1
    return count//2
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
"""

#Double of the given number equal to the numbers consisting of same digits

"""
def check_double(number):
    s=str(number)
    temp=[]
    for j in s:
        temp.append(j)
    s=str(number*2)
    i=0
    count=0
    for j in s:
        if j not in temp:
            return False
        if temp[i]==j:
            count+=1
    if count==len(s):
        return False
    return True


            

#Provide different values for number and test your program
print(check_double(125874))
"""



#numbers not between 5 and 8 and numbers in between 5 and 8

"""
num_list=[3,4,5,2,7,9,8,3,2]

num1=sum(num_list[:num_list.index(5)])
num2=sum(num_list[num_list.index(8)+1:])

first_sum=int(num1)+int(num2)

rest=num_list[num_list.index(5):num_list.index(8)+1]
total1=""
for i in rest:
    total1+=str(i)
total=int(total1)+first_sum

print(total)
"""

#if a number is not pallindrome then reverse the number and add to the original number

"""
number=145
def pallincheck(number):
    s=str(number)
    s1=s[::-1]
    if s==s1:
        return True
    else:
        return False
#pallincheck(number)
val=0
k=0
while(True):
    if (pallincheck(number)):
        val=len(str(number))
        print(val)
        break
    else:
        s1=str(number)
        s=s1[::-1]
        k=number+int(s)
        number=str(k)
        pallincheck(number)
"""

#map function
"""def myfunc(n,o):
    return len(n)+len(o)

x=map(myfunc,('apple','banana'),('jhv','jhvhj'))

print(list(x))
"""
#lambda function
"""
x=lambda a,b,c:a*b+c
print(x(5,7,2))
"""
"""
x='(4+3)'
y=int(eval(x))
print(y)
"""

#OTP generation
"""
def otp_gen(otp1):
    x=""
    for i in range(len(otp1)):
        if i%2!=0:
            x+=str(int(otp1[i])*int(otp1[i]))
            
    return x[:]


otp1='3456767'
print(otp_gen(otp1))
"""

#reversing a string extreacting the characters only
"""
s='dsd$^f#'
res=""
d={}
for i in range(len(s)):
    if s[i].isalnum==False:
        d.update({i:s[i]})
    else:
        res+=s[i]
        res1=list(res[::-1])
for i,j in d.items():
    res1.insert(i,j)
print("".join(res1))
"""


#repeating chars
"""
l="BBBBA"
a=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[j] in a:
            break
        else:
            a.append(l[j])
print(len(a))
"""


#factor game
"""
def factsumfunc(n):
    sum=0
    for j in range(1,n+1):
        if n%j==0:
            sum+=j
    return sum
l=[1,2,4,7]
l1=[]
for i in l:
    val=factsumfunc(i)
    if val in l:
        l1.append(i)
if len(l1)==0:
    print("-1")
else:
    print(sorted(l1))


#print(factsumfunc(7))
"""



#largest even no
"""
s1=set()
s='%#2373#@'
for i in s:
    if i.isdigit():
        s1.add(i)
s2=sorted(s1,reverse=True)
k="".join(s2)
if int(k)%2==0:
    print(k)
else:
    print(-1)
"""


#string of brackets
""""
s1=[]
op=['(','{','[']
cl=[')','}',']']
def validate(s):
    for i in range(len(s)):
        if s[i] in op:
            s1.append(s[i])
        elif s[i] in cl:
            res=cl.index(s[i])
            if(len(s1)>0) and (op[res]==s1[len(s1)-1]):
                s1.pop()
            else:
                return (i+1)
    if(len(s1)==0):
        return 0
    else:
        return len(s)+1
s=str(input())
print(validate(s))

"""



#longest prefix_seffix
"""
def longestPreSuf(s) : 
    n = len(s) 
    prsf = [0] * n 
    l = 0 
    i = 1 
    while (i < n) : 
        if (s[i] == s[l]) : 
            l = l + 1
            prsf[i] = l 
            i = i + 1
        else : 
            if (l != 0) :
                l = prsf[l-1] 
            else : 
                prsf[i] = 0
                i = i + 1
    res = prsf[n-1] 
    if(res > n/2) :
        return n//2 
    else :  
        return res 
s = "codeecode"
print(longestPreSuf(s)) 
"""



#String rotation special manner
"""
s=input().split(",")
sa=[]
num=[]
for i in s:
     s1,n=i.split(":")
     sa.append(s1)
     num.append(n)
def rotate(s2,n):
     n=list(str(n))
     s=0
     for i in n:
         s+=int(i)**2
     if s%2==0:
         return s2[-1:]+s2[:-1] #right rotate
     else:
         return s2[2:]+s2[:2] #left rotate
for i in range(len(num)):
      print(rotate(sa[i],num[i]))
"""



#Word Manipulation
"""
s = 'HelLoWOrld'
l = sorted(set(s.upper()))
res=[]
for i in range(len(l)):
    newstr=""
    for j in s:
        if(l[i]==j.upper()):
            newstr+=j 
    res.append(newstr)
i=0
j=len(res)-1
out=""
while i<=j:
    if i==j:
        out+=res[i]
    else:
        out+=res[i]+res[j]
    i+=1
    j-=1
print(out)   
"""