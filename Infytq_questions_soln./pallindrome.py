inp_no=int(input("Enter a no. to check pallindrome or not="))
temp=inp_no
remainder=0
rev=0
while(inp_no>0):
    remainder=inp_no%10
    rev=rev*10+remainder
    inp_no=inp_no//10
if(temp==rev):
    print("The number is pallindrome")
else:
    print("Number is not pallindrome")
