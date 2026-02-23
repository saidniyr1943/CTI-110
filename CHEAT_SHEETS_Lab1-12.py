
# =============================================================
# CSC131 MASTER CHEAT SHEET (LABS 1–12 + PRACTICE TEST)
# Beginner Friendly – Covers EVERYTHING You Practiced
# =============================================================

# =============================================================
# 1) BASIC INPUT / OUTPUT
# =============================================================

# Integer input
num = int(input("Enter integer: "))

# Float input
num = float(input("Enter float: "))

# Basic print formatting
print(f"{num:.2f}")      # 2 decimal places
print(f"{num:4}")        # width 4 spacing
print(format(num, ",.3f"))

# Scientific notation
print(f"{num:.6e}")

# =============================================================
# 2) BASIC MATH OPERATORS
# =============================================================

a = 5
b = 2

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiply
print(a / b)   # division
print(a // b)  # integer division
print(a % b)   # remainder (used for even/odd)
print(a ** b)  # exponent

# =============================================================
# 3) EVEN / ODD / ZERO
# =============================================================

if num == 0:
    print("zero")
elif num % 2 == 0:
    print("even")
else:
    print("odd")

# =============================================================
# 4) POSITIVE / NEGATIVE / ZERO
# =============================================================

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# =============================================================
# 5) DIFFERENCE CHECK (Practice Test Q1)
# =============================================================

a = int(input())
b = int(input())
diff = a - b

if diff == 0:
    print("zero")
elif diff % 2 == 0:
    print("even")
else:
    print("odd")

# =============================================================
# 6) IF / ELIF STRUCTURE
# =============================================================

if condition1:
    pass
elif condition2:
    pass
else:
    pass

# =============================================================
# 7) FOR LOOPS
# =============================================================

for i in range(5):           # 0 to 4
    print(i)

for i in range(1, 6):        # 1 to 5
    print(i)

for i in range(10, 0, -1):   # countdown
    print(i)

# IMPORTANT: range(start, end+1) includes end

# =============================================================
# 8) WHILE LOOPS
# =============================================================

i = 0
while i < 5:
    print(i)
    i += 1

# Sentinel loop
value = input("Enter number (q to quit): ")
while value != "q":
    print(value)
    value = input("Enter number (q to quit): ")

# =============================================================
# 9) ACCUMULATOR PATTERN (Adding numbers)
# =============================================================

total = 0
for i in range(1, 6):
    total += i

# =============================================================
# 10) SUM BETWEEN NUMBERS
# =============================================================

total = 0
for i in range(start, end + 1):
    total += i

# Even numbers only
for i in range(100, 201):
    if i % 2 == 0:
        total += i

# =============================================================
# 11) SIGMA SUM (Practice Test Q2)
# Sum n/(n+1) from k to m
# =============================================================

k = int(input())
m = int(input())

total = 0
for n in range(k, m + 1):
    total += n / (n + 1)

print(f"{total:.2f}")

# =============================================================
# 12) NESTED LOOPS
# =============================================================

# Multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()

# Star pattern
rows = int(input())
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# =============================================================
# 13) LIST BASICS
# =============================================================

myList = [1, 2, 3]

myList.append(4)
myList.insert(1, 10)
myList.remove(2)

print(len(myList))
print(min(myList))
print(max(myList))
print(sum(myList))
print(sum(myList)/len(myList))

# Membership
if 5 in myList:
    print("Found")

# Slicing
print(myList[1:3])

# =============================================================
# 14) BUILDING A LIST
# =============================================================

result = []
for item in myList:
    if item > 2:
        result.append(item)

# =============================================================
# 15) STRINGS
# =============================================================

word = "Hello"

for char in word:
    print(char)

print(word.count("l"))
print(word.lower().count("a"))

# =============================================================
# 16) SUM OF DIGITS IN STRING (Practice Q3)
# =============================================================

stringNumber = "321"
digit_sum = 0

for digit in stringNumber:
    digit_sum += int(digit)

print(digit_sum)

# =============================================================
# 17) FILTER LIST BY DIGIT SUM
# =============================================================

myList = ['123', '546', '321', '11112']
sumValue = 6
result = []

for num in myList:
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    if digit_sum == sumValue:
        result.append(num)

print(result)

# =============================================================
# 18) COUNT POSITIVE / NEGATIVE
# =============================================================

positive = 0
negative = 0

value = input("Enter number (q to quit): ")
while value != "q":
    num = int(value)
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    value = input("Enter number (q to quit): ")

# =============================================================
# 19) TRIANGLE TYPES
# =============================================================

a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")

# Right triangle check
if round(a*a + b*b, 1) == round(c*c, 1):
    print("Right triangle")

# =============================================================
# 20) FIND WORD WITH MOST DUPLICATE LETTER (Practice Q4)
# =============================================================

work_list = ['aardvark', 'mississippi', 'ssssnake']

max_count = 0
max_word = ""
max_char = ""

for word in work_list:
    for char in word:
        count = word.count(char)
        if count > max_count:
            max_count = count
            max_word = word
            max_char = char

print((max_word, max_count, max_char))

# =============================================================
# REMINDERS
# =============================================================

# % 2 → even/odd
# range(start, end+1) → includes end
# total = 0 → accumulator
# result = [] → build list
# word.count(char) → duplicates
# int() → convert string to number
# Always initialize variables before loops




#Q1
# Q1 - Difference Odd / Even / Zero

# Get two integers from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Calculate the difference
diff = num1 - num2

# Determine if the difference is zero, even, or odd
if diff == 0:
    print("zero")
elif diff % 2 == 0:
    print("even")
else:
    print("odd")





#Q2
# Q2 - Sigma Summation

# Get positive integers k and m
k = int(input("Enter starting value (k): "))
m = int(input("Enter ending value (m): "))

# Initialize total accumulator
total = 0

# Loop from k to m inclusive
for n in range(k, m + 1):
    total += n / (n + 1)

# Print result formatted to 2 decimal places
print(f"{total:.2f}")

# Q3 - Filter list by digit sum

# Define variables
myList = ['123', '136', '343', '2212']
sumValue = 10

# Create empty list to store matching values
result = []

# Loop through each numeric string
for num in myList:
    digit_sum = 0
    
    # Add digits inside the string
    for digit in num:
        digit_sum += int(digit)
    
    # Check if digit sum matches sumValue
    if digit_sum == sumValue:
        result.append(num)

# Print final filtered list
print(result)



# Q4 - Word with most duplicate character

# Create list of words
work_list = ['aardvark', 'mississippi', 'ssssnake']

# Initialize tracking variables
max_count = 0
max_word = ""
max_char = ""

# Loop through each word
for word in work_list:
    
    # Check each character in the word
    for char in word:
        count = word.count(char)
        
        # Update if this is the highest duplicate count so far
        if count > max_count:
            max_count = count
            max_word = word
            max_char = char

# Print result as tuple
print((max_word, max_count, max_char))






############################################################
#Practice
# CSC131 MOCK PRACTICE TEST
# Questions + Solutions Included
# Same Difficulty as Your Real Practice Test
# ============================================================


# ============================================================
# QUESTION 1 (10 pts)
# ------------------------------------------------------------
# Write a program that:
# 1) Prompts the user for TWO integers
# 2) Finds their SUM
# 3) Prints whether the sum is:
#       "positive"
#       "negative"
#       "zero"
# ============================================================

# ---- SOLUTION ----

num1 = int(input("Q1 - Enter first integer: "))
num2 = int(input("Q1 - Enter second integer: "))

total = num1 + num2

if total > 0:
    print("positive")
elif total < 0:
    print("negative")
else:
    print("zero")


# ============================================================
# QUESTION 2 (10 pts)
# ------------------------------------------------------------
# Write a program that:
# 1) Prompts user for positive integer n
# 2) Computes:
#       SUM from i=1 to n of  i/(i+2)
# 3) Prints result formatted to 3 decimal places
# ============================================================

# ---- SOLUTION ----

n = int(input("Q2 - Enter a positive integer: "))

total = 0

for i in range(1, n + 1):
    total += i / (i + 2)

print(f"{total:.3f}")


# ============================================================
# QUESTION 3 (10 pts)
# ------------------------------------------------------------
# Given:
# numbers = ['222', '135', '4444', '1234']
# target = 12
#
# Write a program that:
# 1) Keeps only strings whose digits add to target
# 2) Stores them in a new list
# 3) Prints the new list
# ============================================================

# ---- SOLUTION ----

numbers = ['222', '135', '4444', '1234']
target = 12

result = []

for num in numbers:
    digit_sum = 0
    
    for digit in num:
        digit_sum += int(digit)
    
    if digit_sum == target:
        result.append(num)

print(result)


# ============================================================
# QUESTION 4 (5 pts Extra Credit)
# ------------------------------------------------------------
# Given:
# words = ['committee', 'balloon', 'mississippi']
#
# Write a program that:
# 1) Finds the word with the largest number of repeating letters
# 2) Prints a tuple like:
#       (word, count, letter)
# ============================================================

# ---- SOLUTION ----

words = ['committee', 'balloon', 'mississippi']

max_count = 0
max_word = ""
max_letter = ""

for word in words:
    for char in word:
        count = word.count(char)
        
        if count > max_count:
            max_count = count
            max_word = word
            max_letter = char

print((max_word, max_count, max_letter))


# ============================================================
# QUESTION 5 (10 pts)
# ------------------------------------------------------------
# Write a program that:
# 1) Prompts user for integer rows
# 2) Prints pattern:
#
# If rows = 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ============================================================

# ---- SOLUTION ----

rows = int(input("Q5 - Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ============================================================
# END OF MOCK TEST
# ============================================================
