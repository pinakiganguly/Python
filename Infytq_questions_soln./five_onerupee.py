five_rupee=int(input("How many 5 rupee coin u have="))
one_rupee=int(input("How many 1 rupee coin u have="))
total_amount=int(input("Enter the total amount="))

five_coins_needed=total_amount//5
one_coins_needed=total_amount%5
if five_coins_needed<=five_rupee and one_coins_needed<=one_rupee:
    print("No. of 5 rupee coins needed=",five_coins_needed)
    print("No. of 1 rupee coins needed=",one_coins_needed)
elif five_coins_needed>five_rupee:
    total=five_rupee*5
    one_coins_needed=total_amount-total
    if one_coins_needed<=one_rupee:
        print("No. of five needed=",five_rupee)
        print("No of 1 needed=",one_coins_needed)
    else:
        print(-1)
else:
    print(-1)

"""
if ((five_rupee*5)+(one_rupee)*1)<total_amount:
    print(-1)
else:
    five_coins_needed=total_amount//5
    one_coins_needed=total_amount-(5*(five_coins_needed))
    print("No. of 5 rupee coins=",five_coins_needed)
    print("No. of 1 rupee coins=",one_coins_needed)
"""