#Rustambek Saidniyozov  1/23/2026
#CSC131-001
#
#Purpose of the following programs are to complete teachers instructions
#Variables are users inputs



#######################################
#Problem 1
print("Problem 1")
fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]
print(len(fruits))

fruits.insert(3, "Orange")
print(fruits)

fruits.append("Plum")
print(fruits)

fruits.remove("Melon")
print(fruits)
print("Program finished")
#######################################
#Problem 2
print("Problem 2")
n = input("Please enter a name: ")

count_a = n.count("a")

print(f'character "a" appears {count_a} time(s) within name {n}')
print("Program finished")
#######################################
#Problem 3
print("Problem 3")
n = input("Please enter a name: ")

n = n.lower()
count_a = n.count("a")  

print(f'character "a/A" appears {count_a} time(s) within name {n}')
print("Program finished")
#######################################
#Problem 4
print("Problem 4")
lst = []

num = int(input("Enter an integer: "))
lst.append(num)

num = int(input("Enter an integer: "))
lst.append(num)

num = int(input("Enter an integer: "))
lst.append(num)

num = int(input("Enter an integer: "))
lst.append(num)

num = int(input("Enter an integer: "))
lst.append(num)

print(lst)
print("Minimum:", min(lst))
print("Maximum:", max(lst))
print("Average:", sum(lst) / len(lst))
print("Program finished")
#######################################
#Problem 5
print("Problem 5")
numList = [-4, 0, 2, 10]
numTuple = (2, 3, 1)

print("Using slice operator on numList:", numList[1:3])
print("Using slice operator on numTuple:", numTuple[1:3])

print("-" * 60)

print("the index number of 2 in numList is", numList.index(2))
print("the index number of 2 in numTuple is", numTuple.index(2))

print("-" * 60)

print("-4 is a member of numList:", -4 in numList)
print("-4 is a member of numTuple:", -4 in numTuple)

print("-" * 60)

concat_list = numList + list(numTuple)
concat_tuple = tuple(numList) + numTuple

print("Concatenated as a list:", concat_list)
print("Concatenated as a tuple:", concat_tuple)
print("Program finished")
