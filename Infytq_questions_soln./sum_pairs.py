def find_pairs_of_numbers(number_list,sum):
    count=0
    for i in number_list:
        s=sum-i
        if s in number_list:
            count+=1
    return count//2

number_list=[1,2,7,4,5,6,0,3]
sum=6
print(find_pairs_of_numbers(number_list,sum))