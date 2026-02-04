#Rustambek Saidniyozov  1/30/2026
#CSC131-001
#
#Purpose of the following program is to be able to choose which problem to run
##########################################################################################


choice = int(input("What problem do you want to run? (1-7): "))
#Problem 1: Performs basic list operations such as insert, append, remove,
##########################################################################################
and displays the length of the list.
if choice == 1:
    print("Problem 1")
    fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]
    print(len(fruits))

    fruits.insert(3, "Orange")
    print(fruits)

    fruits.append("Plum")
    print(fruits)

    fruits.remove("Melon")
    print(fruits)
#Problem 2: Prompts the user for a name and counts the number of lowercase letter 'a' characters in the name.
##########################################################################################
elif choice == 2:
    name = input("Please enter a name: ")
    count_a = name.count("a")
    print(f'character "a" appears {count_a} time(s) within name {name}')
#Problem 3: Prompts the user for a name and counts the number of uppercase and lowercase 'a' characters in the name.
##########################################################################################
elif choice == 3:
    name = input("Please enter a name: ")
    lower_name = name.lower()
    count_a = lower_name.count("a")
    print(f'character "a/A" appears {count_a} time(s) within name {name}')
#Problem 4: Collects five numbers from the user and displays the minimum, maximum, and average values.
##########################################################################################    
elif choice == 4:
    numbers = []

    numbers.append(int(input("Please enter a number: ")))
    numbers.append(int(input("Please enter a number: ")))
    numbers.append(int(input("Please enter a number: ")))
    numbers.append(int(input("Please enter a number: ")))
    numbers.append(int(input("Please enter a number: ")))

    print("Number list is:", numbers)
    print("Min value is", min(numbers),
          ", the max value is", max(numbers),
          ", and average value is", sum(numbers) / len(numbers))
#Problem 5: Demonstrates list and tuple operations including slicing,indexing, membership testing, and concatenation.
##########################################################################################
elif choice == 5:
    numList = [-4, 0, 2, 10]
    numTuple = (2, 3, 1)

    print("Using slice operator on numList:", numList[1:3])
    print("Using slice operator on numTuple:", numTuple[1:3])

    print("the index number of 2 in numList is", numList.index(2))
    print("the index number of 2 in numTuple is", numTuple.index(2))

    print("-4 is a member of numList:", -4 in numList)
    print("-4 is a member of numTuple:", -4 in numTuple)

    print("Concatenated as a list:", numList + list(numTuple))
    print("Concatenated as a tuple:", tuple(numList) + numTuple)
#Problem 6: Prompts the user for a number and determines whether it is even, odd, or zero.    
##########################################################################################
elif choice == 6:
    num = int(input("Enter a number: "))

    if num == 0:
        print("0 is neither even or odd!")
    elif num % 2 == 0:
        print(f"{num} is an even number!")
    else:
        print(f"{num} is an odd number")
#Problem 7: Prompts the user for a number and determines whether it is positive, negative, or zero.        
##########################################################################################
elif choice == 7:
    num = int(input("Enter a number: "))

    if num == 0:
        print("0 is neither positive or negative")
    elif num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")        
else:
    print("Invalid Input -- Must be within 1 to 7")
