Students=1
scholarship=0
#Scholarship_amount=0
#Final_fee=0
#branch_study=str(input("Enter the branch"))
#score=int(input("Enter the score"))
while Students<=5:
    branch_study=str(input("Enter the branch"))
    score=int(input("Enter the score"))
    course_fee=50000
    if(branch_study=="Arts"):
        if(score>=90):
            scholarship=50
            
        elif(score%2!=0):
            scholarship=5
            
    elif(branch_study=="Engineering"):
        if(score>85):
            scholarship=50
            
        elif(score%7==0):
            scholarship=5
            
    Scholarship_amount=course_fee*(scholarship)/100
    Final_fee=course_fee-Scholarship_amount
    Students+=1
    print(Final_fee)
#print(Scholarship_amount)

    
