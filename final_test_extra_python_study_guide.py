#=============================================================================
# PROGRAM PURPOSE:
# Extra Python study guide for CSC 131 style tests.
#
# This file focuses on what helps when the teacher changes the problems:
# counting, summing, building lists, building strings, files, dictionaries,
# nested loops, 2D lists, restrictions, and common mistakes.
#=============================================================================


#=============================================================================
# 1. FUNCTION STRUCTURE
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Most test problems ask you to create a function.
# Always check the function name, parameters, return type, restrictions,
# and whether the function should print or return.

def basicFunctionExample(x):
    """Returns the value that was passed into the function."""
    return x


#=============================================================================
# 2. RETURN VS PRINT
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If the problem says "return", use return.
# If the problem says "display" or "print", use print.

def returnExample(x):
    """Returns double the value."""
    return x * 2


def printExample(x):
    """Prints double the value."""
    print(x * 2)


#=============================================================================
# 3. COUNTING PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Any time the problem says "count", start with count = 0.

def countItemsEqualToTarget(items, target):
    """Counts how many items equal the target."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


#=============================================================================
# 4. SUMMING PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Any time the problem says "sum" or "total", start with total = 0.

def sumNumbers(numbers):
    """Returns the sum of numbers in a list."""
    total = 0

    for number in numbers:
        total += number

    return total


#=============================================================================
# 5. BUILDING A LIST PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Any time the problem says "return a list", usually start with result = [].

def returnEvenNumbers(numbers):
    """Returns a list of even numbers."""
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


#=============================================================================
# 6. BUILDING A STRING PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Any time the problem says "create a word", "build a sentence", or
# "concatenate", start with result = "".

def joinCharacters(chars):
    """Joins a list of characters into one string."""
    result = ""

    for ch in chars:
        result += ch

    return result


#=============================================================================
# 7. INDEX LOOP PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use indexes when changing a list in place, comparing neighbors,
# comparing matching indexes, or getting every second item.

def indexLoopExample(items):
    """Returns a list of items with their indexes."""
    result = []

    for i in range(len(items)):
        result.append((i, items[i]))

    return result


#=============================================================================
# 8. CHANGE A LIST IN PLACE
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If the problem says change the list itself, modify the list, do not create
# a new list, or return None, use indexes.

def doubleListInPlace(numbers):
    """Doubles every value in the list in place."""
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2


#=============================================================================
# 9. DO NOT CHANGE ORIGINAL LIST
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If the problem says "return a new list", create a new result list.

def doubleListNew(numbers):
    """Returns a new list with every value doubled."""
    result = []

    for number in numbers:
        result.append(number * 2)

    return result


#=============================================================================
# 10. CHECK SORTED LIST
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If the problem asks if a list is sorted, compare each item to the next item.

def isSorted(numbers):
    """Returns True if the list is sorted in ascending order."""
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


#=============================================================================
# 11. CHECK IF ALL ITEMS MEET A RULE
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If one item fails, return False immediately.
# If the loop finishes, return True.

def allDivisibleBy5(numbers):
    """Returns True if all numbers are divisible by 5."""
    for number in numbers:
        if number % 5 != 0:
            return False

    return True


#=============================================================================
# 12. CHECK IF ANY ITEM MEETS A RULE
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If one item matches, return True immediately.
# If the loop finishes, return False.

def anyNegative(numbers):
    """Returns True if at least one number is negative."""
    for number in numbers:
        if number < 0:
            return True

    return False


#=============================================================================
# 13. COMMON ITEM BETWEEN TWO LISTS
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use nested loops when comparing every item from one list to every item
# from another list.

def commonItem(list1, list2):
    """Returns True if two lists share at least one item."""
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True

    return False


#=============================================================================
# 14. PAIRS FROM ONE LIST
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use this when you need to find pairs in one list.
# Start the second loop at i + 1 so you do not count the same pair twice.

def countPairsOneList(numbers, target):
    """Counts unique pairs from one list that add to the target."""
    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1

    return count


#=============================================================================
# 15. PAIRS FROM TWO LISTS
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use this when one number comes from list1 and the other comes from list2.

def countPairsTwoLists(list1, list2, target):
    """Counts pairs from two lists that add to the target."""
    count = 0

    for num1 in list1:
        for num2 in list2:
            if num1 + num2 == target:
                count += 1

    return count


#=============================================================================
# 16. FILE READING PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# For file problems: open, loop through lines, strip, convert if needed, close.

def readFileLines(filename):
    """Reads a file and returns a list of stripped lines."""
    infile = open(filename, "r")

    result = []

    for line in infile:
        result.append(line.strip())

    infile.close()

    return result


#=============================================================================
# 17. FILE READING WITH FILE NOT FOUND EXCEPTION
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If the problem says to handle file not found, use try/except.

def readFileSafe(filename):
    """Reads a file or returns None if the file is not found."""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    contents = infile.read()
    infile.close()

    return contents


#=============================================================================
# 18. FILE WRITING PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Open with "w", use file.write(), add "\\n" for new lines, close the file.

def writeItemsToFile(filename, items):
    """Writes each item in a list to a file on a separate line."""
    outfile = open(filename, "w")

    for item in items:
        outfile.write(str(item) + "\n")

    outfile.close()


#=============================================================================
# 19. READ NUMBERS FROM FILE AND RETURN SUM
#=============================================================================
# WHAT YOU NEED TO KNOW:
# This is one of the most common file patterns.

def readNumbersSum(filename):
    """Reads integers from a file and returns their sum."""
    infile = open(filename, "r")

    total = 0

    for line in infile:
        total += int(line.strip())

    infile.close()

    return total


#=============================================================================
# 20. STRIP, SPLIT, LOWER, UPPER
#=============================================================================
# WHAT YOU NEED TO KNOW:
# strip() removes newline/spaces from edges.
# split() breaks a sentence into words.
# lower() makes lowercase.
# upper() makes uppercase.

def cleanAndSplit(text):
    """Strips a string, lowers it, and splits it into words."""
    text = text.strip()
    text = text.lower()
    words = text.split()

    return words


#=============================================================================
# 21. CHARACTER CHECKING
#=============================================================================
# WHAT YOU NEED TO KNOW:
# isalpha() checks letters.
# isdigit() checks digits.
# isupper() checks uppercase.
# islower() checks lowercase.

def countLettersAndDigits(text):
    """Returns a tuple with the number of letters and digits."""
    letters = 0
    digits = 0

    for ch in text:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    return (letters, digits)


#=============================================================================
# 22. PASSWORD OR FORMAT VALIDATION PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use boolean flags for validation problems.

def basicPasswordCheck(password):
    """Returns True if a password has uppercase, lowercase, digit, and length 8."""
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) < 8:
        return False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


#=============================================================================
# 23. DICTIONARY FREQUENCY PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If the problem says "frequency", use a dictionary.

def wordFrequency(text):
    """Returns a dictionary counting each word in a string."""
    words = text.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


#=============================================================================
# 24. REMOVE SPECIAL CHARACTERS FROM WORDS
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If punctuation must be removed, loop through each character and keep only
# the characters you want.

def removeSpecialCharacters(word):
    """Returns a word without special characters."""
    special = "#!@#$%^&*()-_=+|{};:/?.>"
    result = ""

    for ch in word:
        if ch not in special:
            result += ch

    return result


#=============================================================================
# 25. MANUAL MINIMUM AND MAXIMUM
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If max() and min() are restricted, use the first item as your starting value.

def manualMinMax(numbers):
    """Returns the minimum and maximum without using min or max."""
    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return (smallest, largest)


#=============================================================================
# 26. MANUAL LENGTH
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If len() is restricted, count manually.

def manualLength(items):
    """Returns the length of a sequence without using len."""
    count = 0

    for item in items:
        count += 1

    return count


#=============================================================================
# 27. MANUAL COUNT
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If count() is restricted, count manually.

def manualCount(items, target):
    """Counts target without using count."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


#=============================================================================
# 28. MANUAL SUM
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If sum() is restricted, add manually.

def manualSum(numbers):
    """Returns the sum without using sum."""
    total = 0

    for number in numbers:
        total += number

    return total


#=============================================================================
# 29. MANUAL POSITIVE DIFFERENCE
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If abs() is restricted, use an if statement.

def manualPositiveDifference(a, b):
    """Returns the positive difference without using abs."""
    if a > b:
        return a - b
    else:
        return b - a


#=============================================================================
# 30. MANUAL REVERSE STRING
#=============================================================================
# WHAT YOU NEED TO KNOW:
# If slicing and reverse() are restricted, loop backward with range.

def manualReverseString(text):
    """Returns a string backward without slicing or reverse."""
    result = ""

    for i in range(len(text) - 1, -1, -1):
        result += text[i]

    return result


#=============================================================================
# 31. PALINDROME CHECK
#=============================================================================
# WHAT YOU NEED TO KNOW:
# A palindrome reads the same forward and backward.

def isPalindrome(value):
    """Returns True if a value is a palindrome."""
    text = str(value)
    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    return text == reversed_text


#=============================================================================
# 32. PRIME NUMBER CHECK
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Prime means only divisible by 1 and itself.

def isPrime(number):
    """Returns True if a number is prime."""
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


#=============================================================================
# 33. FACTORIAL
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Factorial means multiplying from 1 to n.

def factorial(n):
    """Returns the factorial of n."""
    total = 1

    for i in range(1, n + 1):
        total *= i

    return total


#=============================================================================
# 34. NESTED LOOP FOR ALL COMBINATIONS
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use nested loops when every item from one list must pair with every item
# from another list.

def allNameCombinations(first_names, last_names):
    """Returns all first-name and last-name combinations."""
    result = []

    for first in first_names:
        for last in last_names:
            result.append(first + " " + last)

    return result


#=============================================================================
# 35. 2D LIST LOOP
#=============================================================================
# WHAT YOU NEED TO KNOW:
# A 2D list is a list inside a list.

def print2DList(items):
    """Prints every item in a 2D list."""
    for sublist in items:
        for item in sublist:
            print(item)


#=============================================================================
# 36. SUM EACH SUBLIST
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Very common with 2D lists.

def sumEachSublist(items):
    """Returns a list with the sum of each sublist."""
    result = []

    for sublist in items:
        total = 0

        for number in sublist:
            total += number

        result.append(total)

    return result


#=============================================================================
# 37. COLUMN LOOP FOR LIST OF LISTS
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use this when you need to add or join matching positions from each sublist.

def sumColumns(items):
    """Returns sums of matching columns from a list of lists."""
    result = []

    for col in range(len(items[0])):
        total = 0

        for row in range(len(items)):
            total += items[row][col]

        result.append(total)

    return result


#=============================================================================
# 38. MAKE WORDS FROM COLUMNS
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Same pattern as sumColumns, but with letters.

def makeWordsFromColumns(letter_lists):
    """Returns words built from matching columns."""
    result = []

    for col in range(len(letter_lists[0])):
        word = ""

        for row in range(len(letter_lists)):
            word += letter_lists[row][col]

        result.append(word)

    return result


#=============================================================================
# 39. DIAGONAL WORD PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# Use this when the problem says:
# first character of first word,
# second character of second word,
# third character of third word, and so on.

def diagonalWord(words):
    """Returns a word made from diagonal letters."""
    result = ""

    for i in range(len(words)):
        result += words[i][i]

    return result


#=============================================================================
# 40. EVERY SECOND ITEM PATTERN
#=============================================================================
# WHAT YOU NEED TO KNOW:
# range(1, len(items), 2) gets indexes 1, 3, 5, 7, etc.
# range(0, len(items), 2) gets indexes 0, 2, 4, 6, etc.

def everySecondItem(items):
    """Returns every second item starting at index 1."""
    result = []

    for i in range(1, len(items), 2):
        result.append(items[i])

    return result


#=============================================================================
# 41. COMMON TEST MISTAKES
#=============================================================================
# WHAT YOU NEED TO KNOW:
#
# Mistake 1:
# count =+ 1
# This is wrong.
# Use:
# count += 1
#
# Mistake 2:
# if ch == "a" or "e":
# This is wrong.
# Use:
# if ch == "a" or ch == "e":
# Or:
# if ch in "ae":
#
# Mistake 3:
# Changing item in a for loop does not change the list.
# Wrong:
# for item in lst:
#     item = item * 2
#
# Correct:
# for i in range(len(lst)):
#     lst[i] = lst[i] * 2
#
# Mistake 4:
# Forgetting to close files.
#
# Mistake 5:
# Forgetting to convert numbers from strings:
# int(line.strip())
#=============================================================================


#=============================================================================
# 42. HOW TO READ A TEST PROBLEM QUICKLY
#=============================================================================
# Step 1: Find the function name.
# Step 2: Find the parameters.
# Step 3: Find what it returns.
# Step 4: Find restrictions.
# Step 5: Ask what pattern it is:
# count, sum, build list, build string, check True/False, read file,
# write file, nested loop, dictionary frequency, or change list in place.
#=============================================================================


#=============================================================================
# 43. CTRL+F SEARCH WORDS FOR YOUR MASTER FILE
#=============================================================================
# count
# total = 0
# append
# return False
# file = open
# strip
# write
# nested
# dictionary
# in place
# range(len
# sublist
# tuple
# vowel
# sorted
# common
# pair
# palindrome
# prime
# factorial
#=============================================================================


#=============================================================================
# 44. MINI FINAL CHECKLIST BEFORE SUBMITTING
#=============================================================================
# 1. Did I spell the function name exactly right?
# 2. Did I use the exact number of parameters?
# 3. Did I include a docstring?
# 4. Did I return instead of print?
# 5. Did I close the file?
# 6. Did I use try/except if file-not-found was required?
# 7. Did I avoid restricted functions?
# 8. Did I convert strings to ints when reading numbers?
# 9. Did I use "\\n" when writing separate lines?
# 10. Did I test with the examples from the problem?
#=============================================================================


#=============================================================================
# SAMPLE MAIN FOR TESTING ONLY
#=============================================================================

def main():
    """Runs small examples from this study guide."""
    print(countItemsEqualToTarget([1, 2, 2, 3], 2))
    print(sumNumbers([1, 2, 3]))
    print(returnEvenNumbers([1, 2, 3, 4]))
    print(isSorted([1, 2, 3]))
    print(manualReverseString("desserts"))
    print(isPalindrome("anna"))
    print(sumColumns([[1, 2, 3], [4, 5, 6]]))
    print(makeWordsFromColumns([["c", "d"], ["a", "o"], ["t", "g"]]))


if __name__ == "__main__":
    main()
