num1=int(input("Enter the starting number="))
num2=int(input("Enter the ending number="))
l=[]
max_list=[]
sum=0
j=0
if num1<num2:
    for i in range(num1,num2):
        l.append(i)
        max_list=l[:]
        #print(max_list)
        while max_list[j]>0:
            sum=sum+(max_list[j]%10)
            max_list[j]=max_list[j]//10
    #print(sum)
    if sum%3==0 and (max_list[j]>9 or max_list[j]<100) and max_list[j]%5==0:
        print(max_list[j])
    else:
        print(-1)
else:
    print(-1)

"""
max_list=l[:]
print(max_list)
#print(max_list[0])
"""