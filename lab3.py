#Rustambek Saidniyozov  1/23/2026
#CSC131-001
#
#Purpose of the following programs are to complete teachers instructions
#Variables are users inputs



#######################################
#Problem 1
print("Problem 1")
names = []          # list to store the names

name = input("Enter a name: ")
names.append(name)

name = input("Enter a name: ")
names.append(name)

name = input("Enter a name: ")
names.append(name)

print(names)
#######################################
#Problem 2
print("Problem 2")
numbers = []

num = int(input("Enter an integer: "))
numbers.append(num)

num = int(input("Enter an integer: "))
numbers.append(num)

num = int(input("Enter an integer: "))
numbers.append(num)

print(numbers)
#######################################
#Problem 3
print("Problem 3")
new_videos = int(input("Enter number of new videos that you would like to rent: "))
old_videos = int(input("Enter number of old videos that you would like to rent: "))
nights = int(input("Enter number of nights that you would like to keep them for: "))

total_cost = (new_videos * 3.00 + old_videos * 2.00) * nights

print(f"Total cost will be: ${total_cost:,.2f}")
