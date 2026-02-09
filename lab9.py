#Rustambek Saidniyozov  2/9/2026
#CSC131-001
#
#Problem 1- 3:This program prints each item in a sequence using a while loop and two different types of for loops.



# s = ['Apple', 'Banana', 'Cherry']
# s = 'Apple'
s = 'Hello World'
# s = ['ABCDEF']
# s = 'ABCDEF'

print("Problems 1-3")
print("seq:", s)
print()
print("Using while loop:")
i = 0
while i < len(s):
    print(s[i])
    i += 1
print()
print("Using for loop (item):")
for item in s:
    print(item)
print()
print("Using for loop (index):")
for i in range(len(s)):
    print(s[i])
print()

#Problem 4:This program uses a for loop to add all even numbers between 100 and 200 and prints the total.
print("Problems 4")
print("............Problem 4 - Practicing For Loop.............")
print("...Adding up even numbers between 100 and 200, inclusive!...")

total = 0

for num in range(100, 201):
    if num % 2 == 0:
        total += num

print("The total value equals to", total)
print()

#Problems 5-6:This program gets two numbers from the user and prints all numbers between them using both while and for loops.
print("Problems 5-6")
num1 = int(input("num1: "))
num2 = int(input("num2: "))

print("Using while loop:")
if num1 <= num2:
    i = num1
    while i <= num2:
        print(i)
        i += 1
else:
    i = num1
    while i >= num2:
        print(i)
        i -= 1

print("Using for loop:")
if num1 <= num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    for i in range(num1, num2 - 1, -1):
        print(i)
