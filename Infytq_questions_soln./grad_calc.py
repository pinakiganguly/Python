grade_per=float(input("Enter the percentage="))
if grade_per>=80.0 and grade_per<=100.0:
    print("A")
elif grade_per>=73.0 and grade_per<=79.0:
    print("B")
elif grade_per>=65.0 and grade_per<=72.0:
    print("C")
elif grade_per>=0.0 and grade_per<=64.0:
    print("D")
else:
    print("Z")