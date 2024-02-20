# Rustambek Saidniyozov
# 2/20/2024
# P1HW2
#Travel expense calculator


print("This program calculates and displays travel expenses")
user_num1 = int(input('Enter budget:\n'))
dest = input("Enter your travel destination:")
user_num2 = int(input('How much do you think you will spend on gas:\n'))
user_num3 = int(input('Approximately how will you need for accomodation/hotel?:\n'))
user_num4 = int(input("Last, how uch do you need for food:\n"))
print("-----------Travel Expenses----------")          
print("Location:",dest)
print("Initial Budget:", user_num1)

print("Fuel:", user_num2)
print("Accomodation:", user_num3)
print("Food:", user_num4)

print("Remaining blance:", user_num1-user_num2-user_num3-user_num4)           
           
#This program has been created in order to calculate any travel expense one might have.
#I have made a list of all integers that needed to be added and got them calculated.
