

# Rustambek Saidniyozov
# 3/7/2024
# P2HW1
# Travel expense calculator


print("This program calculates and displays travel expenses")
user_num1 = float(input('Enter budget:'))
dest = input("Enter your travel destination:")
user_num2 = float(input('How much do you think you will spend on gas:'))
user_num3 = float(input('Approximately how will you need for accomodation/hotel?:'))
user_num4 = float(input("Last, how uch do you need for food:"))
print("-----------Travel Expenses----------")          
print("Location:            "+ dest)
print(f"Initial Budget:      ${user_num1:.2f}")
print(f"Fuel:                ${user_num2:.2f}")
print(f"Accomodation:        ${user_num3:.2f}")
print(f"Food:                ${user_num4:.2f}")
print()
print("------------------------------------")
print(f"Remaining blance:    ${user_num1-user_num2-user_num3-user_num4:.2f}")           
           
#This program has been created in order to calculate any travel expense one might have.
#I have made a list of all integers that needed to be added and got them calculated.
