#Rustambek Saidniyozov  3/10/2026
#CSC131-001
#Not 100 % sure I did this right.


# Problem 1: spacer() prints a separator line.
def spacer():
    print("=" * 40)


# Problem 2: happyBirthday(name) prints the happy birthday song for one person.
def happyBirthday(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear " + name + "!")
    print("Happy birthday to you!")


# Problem 3: zeroCheck(num1, num2, num3) returns True if any value is 0.
def zeroCheck(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return True
    else:
        return False


# Problem 4: ordered3(num1, num2, num3) returns True if the numbers are in order from smallest to largest.
def ordered3(num1, num2, num3):
    if num1 <= num2 and num2 <= num3:
        return True
    else:
        return False


# Problem 0: main() calls and tests the functions from the other problems.
def main():
    print("Problem 1: spacer()")
    spacer()

    print("Problem 2: happyBirthday()")
    happyBirthday("Emily")
    spacer()

    print("Problem 3: zeroCheck()")
    print("passing values to zeroCheck(): 2, 3, and 4")
    print("returned value:", zeroCheck(2, 3, 4))
    print("passing values to zeroCheck(): 12, 0, and 6")
    print("returned value:", zeroCheck(12, 0, 6))
    spacer()

    print("Problem 4: ordered3()")
    print("passing values to ordered3(): 12, 0, and 6")
    print("returned value:", ordered3(12, 0, 6))
    print("passing values to ordered3(): 0, 10, and 20")
    print("returned value:", ordered3(0, 10, 20))
    spacer()


main()
    
