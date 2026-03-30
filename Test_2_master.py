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


# ============================================================
# Q1 – Count Digits
# ============================================================
def countDigits(s):
    """Returns number of digits in a string."""
    count = 0
    for ch in s:
        if '0' <= ch <= '9':
            count += 1
    return count

# ============================================================
# Q2 – Sum and Count
# ============================================================
def sumAndCount(lst):
    """Returns sum and count of list values."""
    total = 0
    count = 0
    for num in lst:
        total += num
        count += 1
    return total, count

# ============================================================
# Q3 – Positives (new list)
# ============================================================
def positives(lst):
    """Returns a new list of positive numbers."""
    new_list = []
    for num in lst:
        if num > 0:
            new_list.append(num)
    return new_list

# ============================================================
# Q4 – Sum Even Index
# ============================================================
def sumEvenIndex(lst):
    """Returns sum of elements at even indexes."""
    total = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            total += lst[i]
    return total

# ============================================================
# Q5 – Replace 'a'
# ============================================================
def replaceA(s):
    """Replaces 'a' with '*' in a string."""
    result = ""
    for ch in s:
        if ch == 'a':
            result += '*'
        else:
            result += ch
    return result

# ============================================================
# Q6 – Manual Length
# ============================================================
def myLen(s):
    """Returns length of string without len()."""
    count = 0
    for _ in s:
        count += 1
    return count

# ============================================================
# Q7 – Running Total
# ============================================================
def runningTotal(lst):
    """Returns cumulative sum list."""
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

# ============================================================
# Q8 – Count Positive Even
# ============================================================
def countPosEven(lst):
    """Counts numbers that are positive and even."""
    count = 0
    for num in lst:
        if num > 0 and num % 2 == 0:
            count += 1
    return count

# ============================================================
# Q9 – First Negative
# ============================================================
def firstNegative(lst):
    """Returns first negative number or None."""
    for num in lst:
        if num < 0:
            return num
    return None

# ============================================================
# Q10 – Sort Two Values
# ============================================================
def sortTwo(a, b):
    """Returns two values in ascending order."""
    if a < b:
        return [a, b]
    else:
        return [b, a]

# ============================================================
# Q11 – Count Consonants
# ============================================================
def countConsonants(s):
    """Counts consonants in a string."""
    count = 0
    for ch in s:
        if ('A' <= ch <= 'Z' or 'a' <= ch <= 'z') and ch not in "aeiouAEIOU":
            count += 1
    return count

# ============================================================
# Q12 – Multiply List
# ============================================================
def multiplyList(lst):
    """Returns product of all numbers in a list."""
    result = 1
    for num in lst:
        result *= num
    return result

# ============================================================
# Q13 – Largest Even
# ============================================================
def largestEven(lst):
    """Returns largest even number or None."""
    largest = None
    for num in lst:
        if num % 2 == 0:
            if largest is None or num > largest:
                largest = num
    return largest

# ============================================================
# Q14 – Remove Zeros
# ============================================================
def removeZeros(lst):
    """Returns new list without zeros."""
    new_list = []
    for num in lst:
        if num != 0:
            new_list.append(num)
    return new_list

# ============================================================
# Q15 – Count Words
# ============================================================
def countWords(s):
    """Counts number of words in a string."""
    count = 1
    for ch in s:
        if ch == ' ':
            count += 1
    return count

# ============================================================
# Q16 – Palindrome Check
# ============================================================
def isPalindrome(s):
    """Returns True if string is palindrome."""
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# ============================================================
# Q17 – Double Alternate
# ============================================================
def doubleAlternate(lst):
    """Doubles elements at even indexes."""
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] *= 2

# ============================================================
# Q18 – Count Above Average
# ============================================================
def countAboveAvg(lst):
    """Counts values above average."""
    total = 0
    for num in lst:
        total += num
    avg = total / len(lst)
    count = 0
    for num in lst:
        if num > avg:
            count += 1
    return count

# ============================================================
# Q19 – Merge Lists
# ============================================================
def mergeLists(lst1, lst2):
    """Returns new list combining two lists."""
    new_list = []
    for item in lst1:
        new_list.append(item)
    for item in lst2:
        new_list.append(item)
    return new_list

# ============================================================
# Q20 – Second Largest
# ============================================================
def secondLargest(lst):
    """Returns second largest value."""
    largest = lst[0]
    second = lst[0]
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second









        
