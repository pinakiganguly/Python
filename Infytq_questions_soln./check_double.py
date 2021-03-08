def check_double(number):
    num = str(number)
    temp = []
    for numb in num:
        temp.append(numb)
    num = str(number*2)
    i = 0
    count = 0
    for numb in num:
        if numb not in temp:
            return False
        if temp[i] == numb:
            count += 1
    if count == len(num):
        return False
    return True       

print(check_double(5))