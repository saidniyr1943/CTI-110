########################################
#Rustambek Saidniyozov  1/27/2026
#
#Problem 1 and 2: To determine the status of the student based on the credits earned
#Problem 3 and 4: To display appropriate words when given a certain input
#Problem 5:To determine which type of triangle based on user inputs
########################################
print("Problem 1")
print("-----Problem 1:-----")

credits = int(input("Enter the number of college credits earned: "))

if credits > 90:
    print("Senior Status")
else:
    if credits > 60:
        print("Junior Status")
    else:
        if credits > 30:
            print("Sophomore Status")
        else:
            print("Freshman Status")
print()
########################################
print("-----Problem 2:-----")
credits = int(input("Enter the number of college credits earned: "))

if credits > 90:
    print("Senior Status")
elif credits > 60:
    print("Junior Status")
elif credits > 30:
    print("Sophomore Status")
else:
    print("Freshman Status")
print()
########################################
print("-----Problem 3:-----")

letter = input("Enter 'A' for apple, 'B' for banana, and 'C' for coconut: ")

if letter == 'A' or letter == 'a':
    print("Apple")
else:
    if letter == 'B' or letter == 'b':
        print("Banana")
    else:
        if letter == 'C' or letter == 'c':
            print("Coconut")
        else:
            print("Invalid Input!")
print()
########################################
print("-----Problem 4:-----")
letter = input("Enter 'A' for apple, 'B' for banana, and 'C' for coconut: ")

if letter == 'A' or letter == 'a':
    print("Apple")
elif letter == 'B' or letter == 'b':
    print("Banana")
elif letter == 'C' or letter == 'c':
    print("Coconut")
else:
    print("Invalid Input!")
print()
########################################
print("-----Problem 5:-----")

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2 and side2 == side3:
    print("This is an Equilateral triangle!")

elif round(side1**2 + side2**2, 1) == round(side3**2, 1) or \
     round(side1**2 + side3**2, 1) == round(side2**2, 1) or \
     round(side2**2 + side3**2, 1) == round(side1**2, 1):
    print("This is a Right triangle!")

elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an Isosceles triangle!")

else:
    print("This is a Scalene triangle!")
print("End of the Lab")    
