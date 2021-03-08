current_year=int(input("Enter the current year="))
leap_year_list=[]
leap=[]
for i in range(current_year,current_year+15):
    if i%4==0 and i%100!=0:
        leap.append(i)
    elif i%400==0 and i%100!=0:
        leap.append(i)
leap_year_list=leap[:]
print(leap_year_list)

