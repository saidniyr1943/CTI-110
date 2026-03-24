#Rustambek Saidniyozov  3/15/2026
#CSC131-001


####################################################
# Problem 1-Prints "Hello world, my name is   " using the name passed into the function.

def helloWorld(name):
    print("Hello world, my name is", name)


#####################################################
# Problem 2- Prints a line of asterisks (*) based on the number given, but never more than 15.

def printAsterisks(n):

    if n > 15:
        n = 15

    for i in range(n):
        print("*", end=" ")

    print()


#####################################################
# Problem 3- Asks the user if they want to continue until they enter 'y' or 'n', then returns the answer.

def getContinue():

    while True:
        answer = input("Do you want to continue? ")

        if answer.lower() == "y" or answer.lower() == "n":
            return answer.lower()

#####################################################
# Problem 4- Description: Counts how many numbers from 1 to n are evenly divisible by m.

def modCount(n, m):

    count = 0

    for i in range(1, n + 1):
        if i % m == 0:
            count += 1

    return count

#####################################################
# Main Function- Calls and tests all the functions.

def main():

    # Problem 1
    print("----------helloWorld() function----------")
    print("passing values to helloWorld(): Alex")
    helloWorld("Alex")

    print("passing values to helloWorld(): Sarah")
    helloWorld("Sarah")

    # Problem 2
    print("\n----------printAsterisks() function----------")

    n1 = int(input("How many asterisks do you want to see: "))
    printAsterisks(n1)

    n2 = int(input("How many asterisks do you want to see: "))
    printAsterisks(n2)

    # Problem 3
    print("\n----------validInput() function----------")
    result = getContinue()
    print("returned value:", result)

    # Problem 4
    print("\n----------modCount() function----------")

    n = int(input("Enter the value for n: "))
    m = int(input("Enter the value for m: "))

    result = modCount(n, m)

    print("Numbers from 1 to", n, "divisible by", m, ":", result)


main()
    
