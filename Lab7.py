#Saidniyozov Rustambek                      #2/4/2026

#CSC-131

#Purpose of the problem 1 is to calculate sum of all even numbers between 100 and 200

#Purpose of problem 2 is to calculate the sum of numbers entered by the user until -1 is entered

#Purpose of problem 3 is to calculate the sum of positive numbers less than 100 entered by the user until -1 is entered

#Purpose of problem 4 is to count how many positive and negative numbers are entered by the user until q is entered

###########################################################################
#Problem 1
print("STARTING Problem 1")
print("...........Problem 1 - Practicing While Loop...........")
print("...Adding up even numbers between 100 and 200, inclusive!...")

total = 0
num = 100

while num <= 201:
    total = total + num
    num = num + 2

print(total)
print("Ending Problem 1")
print()
###########################################################################
#Problem 2
print("STARTING Problem 2")
print("Problem 2 - Adding values entered by user")

total = 0
num = int(input("Enter a number (-1 to quit): "))

while num != -1:
    total = total + num
    num = int(input("Enter a number (-1 to quit): "))

print("The total is:", total)
print("Ending Problem 2")
print()
###########################################################################
#Problem 3
print("STARTING Problem 3")
print("...........Problem 3 - Practicing While Loop...........")
print("Summing positive values entered by the user that are less than 100!")

total = 0

num = int(input("Please enter first number to sum (enter -1 to quit): "))

while num != -1:
    if num > 0 and num < 100:
        total = total + num

    num = int(input("Please enter next number (enter -1 to quit): "))

print("The sum all all the positive values less than 100 is:", total)
print("Ending Problem 3")
print()
###########################################################################
#Problem 4
print("STARTING Problem 4")
print("...........Problem 4 - Practicing While Loop...........")
print("Counting the number of positive and negative values entered by the user")

positive_count = 0
negative_count = 0

value = input("Please enter first number (enter q to quit): ")

while value != "q":
    num = int(value)

    if num > 0:
        positive_count = positive_count + 1
    elif num < 0:
        negative_count = negative_count + 1

    value = input("Please enter next number (enter q to quit): ")

print("Number of positive values entered:", positive_count)
print("Number of negative values entered:", negative_count)
print("Ending Problem 4")
