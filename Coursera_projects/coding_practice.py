"""
Implementing RPSLS for Practice Project
"""

def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else:
        return 4
    
print(name_to_number("rock"))		# output - 0
print(name_to_number("Spock"))		# output - 1
print(name_to_number("paper"))		# output - 2
print(name_to_number("lizard"))		# output - 3
print(name_to_number("scissors"))	# output - 4


def number_to_name(number):
    """
    Taking numbers as input(0-1-2-3-4)
    and returns string as (rock-Spock-paper-lizard-scissors)
    """
    if number==0:
        a="rock"
        print(a)
        """
    elif number==1:
        return Spock
    elif number==2:
        return paper
    elif number==3:
        return lizard
    elif number==4:
        return scissors
    """
    else:
        print("Wrong input!!!")
            
    print(number_to_name(0))        #output- rock
    print(number_to_name(1))        #output- Spock
    print(number_to_name(2))        #output- paper  
    print(number_to_name(3))        #output- lizard
    print(number_to_name(4))        #output- scissors