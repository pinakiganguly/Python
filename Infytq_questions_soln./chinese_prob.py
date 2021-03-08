heads=int(input("Enter the number of heads="))
legs=int(input("Enter the number of legs="))
no_of_rabits=int((legs-(heads*2))/2)
#print(no_of_rabits)
if heads>legs or legs%2!=0 or heads==0 :
    print("No solution")
else:
    print(no_of_rabits,end=" ")
    no_of_hens=heads-no_of_rabits
    print(no_of_hens)