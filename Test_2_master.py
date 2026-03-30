# CSC 131 
# All functions include descriptions (docstrings)

# Q1
def posDiff(a, b):
    """Returns the positive difference between two integers."""
    if a > b:
        return a - b
    else:
        return b - a

# Q2
def countUpper(s):
    """Returns the number of uppercase letters in a string."""
    count = 0
    for ch in s:
        if 'A' <= ch <= 'Z':
            count += 1
    return count

# Q3
def sumDivisible(a, b):
    """Returns sum of numbers divisible by 3 between a and b inclusive."""
    total = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            total += i
    return total

# Q4
def zeroNegatives(lst):
    """Replaces negative numbers in the list with 0 (in-place)."""
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0

# Q5
def longestWord(lst):
    """Returns the longest word in a list of strings."""
    longest = lst[0]
    for word in lst:
        if len(word) > len(longest):
            longest = word
    return longest

# Q6
def reverseNum(n):
    """Returns the reversed integer."""
    result = 0
    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n = n // 10
    return result

# Q7
def hasCommon(lst1, lst2):
    """Returns True if the two lists share at least one value."""
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
    return False

# Q8
def countPairs(lst):
    """Counts adjacent equal values in a list."""
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            count += 1
    return count

# Q11
def temperatureConv(letter, temp):
    """Converts temperature between Celsius and Fahrenheit."""
    if letter == 'f' or letter == 'F':
        return int((temp - 32) * 5/9)
    elif letter == 'c' or letter == 'C':
        return int((temp * 9/5) + 32)
    else:
        return -1

# Q12
def backward(num):
    """Returns a list counting down from num to 0."""
    return list(range(num, -1, -1))

# Q13
def sumEven(p1, p2):
    """Returns the sum of all even numbers between p1 and p2."""
    total = 0
    for i in range(p1, p2 + 1):
        if i % 2 == 0:
            total += i
    return total

# Q14
def negativeIntDiff(a, b):
    """Returns the negative difference between two integers."""
    if a > b:
        return b - a
    else:
        return a - b

# Q15
def sumOfSquares(n):
    """Returns the sum of squares from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

# Q16
def numSpaces(s):
    """Returns number of spaces in a string."""
    count = 0
    for ch in s:
        if ch == ' ':
            count += 1
    return count

# Q17
def convertToInts(lst):
    """Converts all string elements in the list to integers."""
    for i in range(len(lst)):
        lst[i] = int(lst[i])

# Q18
def commonItem(lst1, lst2):
    """Returns True if lists share at least one common item."""
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
    return False

# Q19
def countVowels(s):
    """Returns number of vowels in a string."""
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count

# Q 20
def countUpperLower(lst):
    """Returns total uppercase and lowercase letters in a list of strings."""
    upper = 0
    lower = 0

    for word in lst:
        for ch in word:
            if 'A' <= ch <= 'Z':
                upper += 1
            elif 'a' <= ch <= 'z':
                lower += 1

    return upper, lower

#Q 21
def countUpperLowerTwo(s1, s2):
    """Returns total uppercase and lowercase letters in two strings."""
    upper = 0
    lower = 0

    for ch in s1:
        if 'A' <= ch <= 'Z':
            upper += 1
        elif 'a' <= ch <= 'z':
            lower += 1

    for ch in s2:
        if 'A' <= ch <= 'Z':
            upper += 1
        elif 'a' <= ch <= 'z':
            lower += 1

    return upper, lower


def countUpperLower(s):
    """
    QUESTION:
    Count uppercase and lowercase letters in a string.
    """
    upper = 0
    lower = 0

    for ch in s:
        if 'A' <= ch <= 'Z':
            upper += 1
        elif 'a' <= ch <= 'z':
            lower += 1

    return upper, lower


# ============================================================
# 🔹 Q3 – Sum Even Numbers
# ============================================================

def sumEven(a, b):
    """
    QUESTION:
    Return sum of even numbers between a and b inclusive.
    """
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            total += i
    return total


# ============================================================
# 🔹 Q4 – Modify List In Place
# ============================================================

def zeroNegatives(lst):
    """
    QUESTION:
    Replace negative numbers with 0 (in-place).
    """
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0


# ============================================================
# 🔹 Q5 – Longest Word
# ============================================================

def longestWord(lst):
    """
    QUESTION:
    Return longest string in list.
    """
    longest = lst[0]
    for word in lst:
        if len(word) > len(longest):
            longest = word
    return longest


# ============================================================
# 🔹 Q6 – Reverse Number
# ============================================================

def reverseNum(n):
    """
    QUESTION:
    Reverse digits of an integer.
    """
    result = 0
    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n = n // 10
    return result


# ============================================================
# 🔹 Q7 – Nested Loop (Common Values)
# ============================================================

def hasCommon(lst1, lst2):
    """
    QUESTION:
    Return True if lists share a value.
    """
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
    return False


# ============================================================
# 🔹 STAR PATTERNS
# ============================================================

def starTriangle(rows):
    """Prints triangle of stars."""
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()


def starGrid(rows, cols):
    """Prints grid of stars."""
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()
