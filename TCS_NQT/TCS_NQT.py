"""
def checkConsecutive_check(l,N):
    sum=0
    l1=[]
    for i in l:
        if i<0:
            l1.append(abs(i))
        else:
            l1.append(i)
    #print(l1)
     
    if sorted(l1) == list(range(min(l1), max(l1)+1)):
        for j in l:
            sum=sum+j
            #print(sum)
            if sum==0:
                k=1
            else:
                k=0
    return k
      
# Driver Code
lst = [-1,2,3,-4]
N=4
print(checkConsecutive_check(lst,N))
"""

#--------------------------------------------------------------------
def encode(string):
    l=[]
    str=""
    x=string.replace(", ","")
    for i in range(len(x)):
        a=ord(x[i])
        b=a+5
        l.append(chr(b))
    return str.join(l)

def decode(string):
    l=[]
    str=""
    #x=string.replace(", ","")
    for i in range(len(string)):
        a=ord(string[i])
        b=a-5
        l.append(chr(b))
    return str.join(l)
    
    
      
# Driver Program
string = 'Hello, sir'
string1='Mjqqtxnw'
print(encode(string))
print(decode(string1))

