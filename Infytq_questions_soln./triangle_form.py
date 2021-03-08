def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    if (num1+num2)>num3 and (num2+num3)>num1 and (num1+num3)>num2:
        return success
    
    else:
        return failure
    """
    #Use the following messages to return the result wherever necessary
    return success
    return failure
    """
print(form_triangle(3,2,5))