"""Master completed solutions for the five CSC 131 final review files.

This version keeps the original problem instructions from the uploaded review files
above each matching solution so the file can be used as a study guide.
"""

import random


# ============================================================================
# Practice Final 1
# ============================================================================

#=============================================================================
# q1 - create function quarter() to meet the conditions below
#    - accept one parameter:  a string (month name)
#    - add a meaningful docstring
#    - determine the quarter of the year given the month name
#    - return the quarter # (1, 2, 3, or 4)
#    - you can assume that the input parameter is a valid, full name of a month
#
#    --- e.g. for March -> returns 1
#    --- e.g. for June -> returns 2
#    --- e.g. for October -> returns 4
#
#    The quarters are:
#    --- quarter 1: January - March
#    --- quarter 2: April - June
#    --- quarter 3: July - September
#    --- quarter 4: October - December
#
#    - RESTRICTIONS:  None
#
#    - param:   string
#    - return:  integer
#=============================================================================

def quarter(month):
    """Return the quarter number for a full month name."""
    if month in ["January", "February", "March"]:
        return 1
    if month in ["April", "May", "June"]:
        return 2
    if month in ["July", "August", "September"]:
        return 3
    return 4


#=============================================================================
# q2 - create function listOfLists() to meet the conditions below
#    - accept one parameter:  a list of lists of integer values
#    - add a meaningful docstring
#    - the lists in the list are all of a same size
#    --- e.g. [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#    --- e.g. [ [4, 3, 2, 1], [4, 4, 3, 6], [1, 0, 5, 2] ]
#    --- e.g. [ [3, 2], [6, 6], [1, 9], [2, 8] ]
#    - calculate the sum of the matched items from all the lists,
#       store them into a new list and return it
#    --- e.g. [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] -> returns [12, 15, 18]
#    --- e.g. [ [4, 3, 2, 1], [4, 4, 3, 6], [1, 0, 5, 2] ] -> returns [9, 7, 10, 9]
#    --- e.g. [ [3, 2], [6, 6], [1, 9], [2, 8] ] -> returns [12, 25]
#    - return the new list
#
#    - RESTRICTIONS:  None
#
#    - params:  integer
#               integer
#    - return:  integer
#=============================================================================

def listOfLists(values):
    """Return a list containing the column sums from a list of equal-sized lists."""
    result = []
    for col in range(len(values[0])):
        total = 0
        for row in range(len(values)):
            total += values[row][col]
        result.append(total)
    return result


#==========================================================================
# q3 - create function longestLength() to meet the conditions below
#    - accept unknown number of parameters: n strings (n>0)
#    - add a meaningful docstring
#    - return the length of the longest string
#
#    --- e.g. "Hello" and "Good-bye", 'Hi'; function returns 8
#    --- e.g. "Hello"; function returns 5
#
#    - RESTRICTIONS: None
#
#    - params:  n number of string(s)
#    - return:  integer
#==========================================================================

def longestLength(*words):
    """Return the length of the longest string argument."""
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


#==========================================================================
# q4 - create function numTriangle() to meet the conditions below
#    - accept one parameter: a single digit integer
#    - add a meaningful docstring
#    - creates a number triangle with x rows.
#    - each row consists of the row numbers starting from 10.
#    - you can assume the parameter is a value between 2 and 9 (both inclusive).
#
#    --- e.g. 3 is passed to the function
#       displays:
#       10
#       10 11
#       10 11 12
#    --- e.g. 5 is passed to the function
#       displays:
#       10
#       10 11
#       10 11 12
#       10 11 12 13
#       10 11 12 13 14
#
#    - RESTRICTIONS: None
#
#    - param:   integer
#    - return:  None
#==========================================================================

def numTriangle(rows):
    """Print a number triangle with the requested number of rows."""
    for row in range(rows):
        line = ""
        for num in range(10, 10 + row + 1):
            line += str(num) + " "
        print(line.strip())


#==========================================================================
# q5 - create function combineWords() to meet the conditions below
#    - accept two parameters: two lists named firstnames and lastnames
#    - add a meaningful docstring
#    - returns a new list representing all possible combinations of EACH
#    - firstname string and EACH lastname string with a space between
#
#    --- e.g. first: ["sara", "alex"] and last: ["smith", "murphy"]
#       returns the final list:
#       ["sara smith", "sara murphy", "alex smith", "alex murphy"]
#       
#
#    - RESTRICTIONS: None
#
#    - params:  list
#               list
#    - return:  list
#==========================================================================

def combineWords(firstnames, lastnames):
    """Return all first-name and last-name combinations with a space between them."""
    result = []
    for first in firstnames:
        for last in lastnames:
            result.append(first + " " + last)
    return result


#==========================================================================
# q6 - create function secondIndex() to meet the conditions below
#    - accept two parameters: a list of integers and an integer
#    - add a meaningful docstring
#    - find the index of the SECOND occurrence of the number (2nd parameter)
#       in the list (1st parameter).
#    - return: Index of second occurrence of the integer in the list.
#    - -1 if the number does not occur two or more times in the list.
#
#    --- e.g. 1: secondIndex([2,34,3,45,34,45,3,3], 3) returns 6
#    --- e.g. 2: secondIndex([2,34,3,45,34,45,3,3], 45) returns 5
#    --- e.g. 3: secondIndex([2,34,3,45,134,45,3,3], 134) returns -1
#    --- e.g. 4: secondIndex([2,34,3,45,134,45,3,3], 100) returns -1
#
#    - RESTRICTIONS: None
#
#    - params:  list
#               integer
#    - return:  integer
#==========================================================================

def secondIndex(numbers, target):
    """Return the index of the second occurrence of target, or -1 if it is not found twice."""
    count = 0
    for index in range(len(numbers)):
        if numbers[index] == target:
            count += 1
            if count == 2:
                return index
    return -1


#==========================================================================
# q7 - create function lineLengths() to meet the conditions below
#    - accept one parameter: a string (filename)
#    - add a meaningful docstring
#    - open the file and read each line
#    - count the characters in each line
#    - don't forget to close the file
#    - return the length of the longest line in the file
#    - it's not required for you to handle the line breaks at the end.
#    - test files (sample1.txt, sample2.txt) will be created by the testing code.
#
#    - RESTRICTIONS: None
#
#    - param:   string
#    - return:  integer
#==========================================================================

def lineLengths(filename):
    """Return the length of the longest line in a file."""
    infile = open(filename, "r")
    longest = 0
    for line in infile:
        length = len(line.rstrip("\n"))
        if length > longest:
            longest = length
    infile.close()
    return longest


#==========================================================================
# q8 - create function writeRandomNumbers() to meet the conditions below
#    - accept one parameter: a string (filename) 
#    - add a meaningful docstring
#    - write ten random integers (of your choice) between 0 and 100 into the textfile
#      ---NOTE:  if done correctly, the output textfile is placed in the same
#                directory as this exam file
#    - don't forget to add the newline (line break) character to each line
#    - don't forget to close the file
#    - the testing code will create two files by itself for two test cases.
#    - return None 
#
#    - RESTRICTIONS:  None
#
#    - param:   string
#    - return:  None
#
#==========================================================================

def writeRandomNumbers(filename):
    """Write ten random integers from 0 through 100 to a file."""
    outfile = open(filename, "w")
    for _ in range(10):
        outfile.write(str(random.randint(0, 100)) + "\n")
    outfile.close()
    return None


#==========================================================================
# q9 - create function mergeLists() to meet the conditions below
#    - accept two parameters:  two lists
#    - add a meaningful docstring
#    - you may assume the lists are the same length
#    - return the merged dictionary
#
#    --- e.g.
#        list1 is: ['A', 'B', 'C']
#        list2 is : [1, 4, 5]
#        Resultant dictionary is : {'A': 1, 'B': 4, 'C': 5}
#
#    - RESTRICTIONS:  None
#
#    - params:  list
#               list
#    - return:  dictionary
#==========================================================================

def mergeLists(list1, list2):
    """Return a dictionary made by matching each item in the first list to the same-index item in the second list."""
    result = {}
    for index in range(len(list1)):
        result[list1[index]] = list2[index]
    return result


#==========================================================================
# q10- create function sumNum() to meet the conditions below
#    - accept one parameter: an n-character string
#    - add a meaningful docstring
#    - find all the string numbers in the string, convert them to integer
#      and add them together
#    - you may assume all numbers are single digit
#    - return the integer result
#
#    --- e.g. "2KL5", returns 7
#    --- e.g. "Z3r5Q1h2g5Q", returns 16
#    --- e.g. "5A1E3yfE0", returns 9
#
#    - RESTRICTIONS:  None
#
#    - param:   string
#    - return:  integer
#==========================================================================

def sumNum(text):
    """Return the sum of numbers in a string, handling either single digits or hyphen-separated numbers."""
    if "-" in text:
        total = 0
        current = ""
        for ch in text:
            if ch == "-":
                if current != "":
                    total += int(current)
                    current = ""
            else:
                current += ch
        if current != "":
            total += int(current)
        return total
    total = 0
    for ch in text:
        if ch.isdigit():
            total += int(ch)
    return total


#==========================================================================
# q11 - DEBUG function numVowels(sentence)
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - accept one parameter: sentence - a string  
#
#    - numVowels should iterate over the string and count how many of the
#      characters are vowels
#    - you may assume all the letters are lowercases.
#    - return the number of vowels
#
#    ---e.g. 'Hello' returns 2
#
#    - RESTRICTIONS: do NOT re-write the function, just find/fix error(s)
#
#    - param:  string
#    - return: integer
#
#==========================================================================

def numVowels(sentence):
    """Return the number of lowercase vowels in a string."""
    count = 0
    for ch in sentence:
        if ch in "aeiou":
            count += 1
    return count


# ============================================================================
# Practice Final 2
# ============================================================================

#==========================================================================
# q1 - create function isIntDiffEven() to meet the conditions below
#    - accept 2 integer parameters of any value
#    - add a meaningful docstring
#    - determine if the integer difference between the values is even.
#    --- e.g. submitted ints are -7 and 12; diff is -19(odd); returns False
#    --- e.g. submitted ints are 13 and 9; diff is 4(even); returns True
#    --- e.g. submitted ints are -2 and -5; diff is 3(odd); return False
#    --- you may assume the user arguments will be integers
#    - return the resultant integer
#
#    - params:  integer
#               integer
#    - return:  boolean
#==========================================================================

def isIntDiffEven(num1, num2):
    """Return True if the difference between two integers is even."""
    return (num1 - num2) % 2 == 0


#==========================================================================
# q2 - create function numCount() to meet the conditions below
#    - accept two parameters: a list of arbitrary numbers and an integer value
#    - add a meaningful docstring
#    - searchs the number of times the passed integer number occurs in a list.
#    - return the number of times the number is repeated in the list. 
#    --- e.g. [2,5,2,7,1,2,1] and 2 -> returns 3
#    --- e.g. [1,5,0,2] and 100 -> returns 0
#    --- e.g. [1,5,5,2,4,5,2,3,1,5,3] and 5 -> returns 4 
#
#    Restriction: you are not allowed to use count() function
#
#    - param:  list
#              integer
#    - return: integer
#==========================================================================

def numCount(numbers, target):
    """Return how many times target appears in the list."""
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count


#==========================================================================
# q3 - create function sumValues() to meet the conditions below
#    - accept two parameters:
#       a list of arbitrary numbers and an integer value (n)
#    - add a meaningful docstring
#    - return sum of the first n value in the list.
#    - you many assume n is less or equal to the length of the list
#    --- e.g. [2,5,4,7,1,2,1] and 3 -> returns 11 (which is the result of 2+5+4)
#    --- e.g. [1,5,0,2] and 4 -> returns 8 (which is the result of 1+5+0+2)
#
#    Restriction: you are not allowed to use sum() function
#
#    - param:  list
#              integer
#    - return: integer
#==========================================================================

def sumValues(numbers, n):
    """Return the sum of the first n values in a list."""
    total = 0
    for index in range(n):
        total += numbers[index]
    return total


#==========================================================================
# q4 - create function countPairs() to meet the conditions below
#    - accept two lists of arbitrary numbers and an integer as parameters
#    - add a meaningful docstring
#    - find the evey possible pair between list1 and list1 that when add up
#       is equal to the integer value
#    - returns the number of pairs
#    --- e.g. [2,5,4,7,2], [1,2,1,4,2], and 8 -> returns 3 because
#       (4,4),(7,1),(7,1)
#    --- e.g. [1,2,3,4], [2,3,4,5], and 6 -> returns 4 because
#       (1,5),(2,4),(3,4),(4,2)
#
#    Restriction: None
#
#    - param:  list
#              list
#              integer
#    - return: integer
#==========================================================================

def countPairs(*args):
    """Count pairs that add to a target for either one list or two list inputs."""
    if len(args) == 3:
        list1, list2, target = args
        count = 0
        for item1 in list1:
            for item2 in list2:
                if item1 + item2 == target:
                    count += 1
        return count
    if len(args) == 2:
        numbers, target = args
        count = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    count += 1
        return count
    return 0


#==========================================================================
# q5 - create function commonItem() to meet the conditions below
#    - accept two lists of arbitrary values as parameters
#    - add a meaningful docstring 
#    - returns True if the lists share at least one common member
#       False otherwise
#    --- e.g. [2,5,4,7,2] and [1,2,1,4,2] -> returns True
#    --- e.g. ['a','b','c','a'] and ['g','z','f'] -> returns False
#
#    Restriction: You are not allowed to use set() functions
#
#    - param:  list
#              list
#    - return: boolean
#==========================================================================

def commonItem(list1, list2):
    """Return True if two lists share at least one item."""
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False


#==========================================================================
# q6 - create function createWord() to meet the conditions below
#    - accept a list of string as parameter
#    - add a meaningful docstring 
#    - extract the first charcter of the first item,
#       second character of the second item,
#       third character of the third item, and so on
#       add them to each and return the resultant string
#       you may assume the strings have enough letters in them
#    --- e.g. ['case', 'poor', 'from', 'yellow'] -> returns cool
#    --- e.g. ['red','you','return'] -> returns rot
#
#    Restriction: None
#
#    - param:  list
#    - return: string
#==========================================================================

def createWord(words):
    """Return a word made from the first character of the first word, second of the second word, and so on."""
    result = ""
    for index in range(len(words)):
        result += words[index][index]
    return result


#==========================================================================
# q7 - create function openAndReturnFML() to meet the conditions below
#    - accept 1 parameter; 1 string (name of a file) 
#    - add a docstring
#    - the file will contain an unknown odd number of lines
#    - store the first, middle and last lines of the file in a single string var
#    - you may assume there are odd number of lines in the file
#    --- ensure to strip the newline character from the lines
#    --- e.g.   textfile:
#    --- e.g.   "line one\n"
#    ---        "line two\n"
#    ---        "line three\n"
#    ---        "line four\n"
#    ---        "line five\n"
#    ---        integer: 2
#    --- e.g. "line one" + "line three" + "line five"will be
#             "line oneline threelinefive"
#
#
#    - params:  string               
#    - return:  string
#==========================================================================

def openAndReturnFML(filename):
    """Return the first, middle, and last lines of an odd-line file joined together."""
    infile = open(filename, "r")
    lines = []
    for line in infile:
        lines.append(line.strip())
    infile.close()
    middle = len(lines) // 2
    return lines[0] + lines[middle] + lines[-1]


#=============================================================================
# q8 - create function writeEvenNumbers() to meet the conditions below
#    - accept two parameters:  a string (name of a file)
#                              an integer value
#    - add a meaningful docstring
#    - open the filename for writing
#    - write to the file all of the even numbers between 2 and the
#        integer value inclusive. Each number should be on a separate line
#        in the file. 
#      --- don't forget to close the file
#    - return None
#
#    Restriction:  None
#
#    - params:  string
#               integer
#    - return:  None
#=============================================================================

def writeEvenNumbers(filename, number):
    """Write all even numbers from 2 through number to a file and return the line count."""
    outfile = open(filename, "w")
    count = 0
    for value in range(2, number + 1, 2):
        outfile.write(str(value) + "\n")
        count += 1
    outfile.close()
    return count


#=============================================================================
# q9 - create function translateMorse() to meet the conditions below
#    - accept two parameters:  a Morse-code-to-English dictionary and
#      a tuple of Morse code characters
#    --- dictionary looks like:  {'.-': 'a', ...etc... '--..': 'z', '/' : ' '}
#        where Morse is the key and English is the value for each pair
#    - add a meaningful docstring
#    - iterate over the tuple, convert the Morse to English, and concatenate
#      in a string
#    - return the string translation
#
#    - Example: dictionary: {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
#                           '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
#                           '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
#                           '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
#                           '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
#                            '--..': 'z', '/' : ' '}
#               tuple parameter = ('-.-.', '.-..', '.', '...-', '.', '.-.')
#               return "clever"
#
#    - RESTRICTIONS:  None
#
#    - params:  dictionary
#               tuple
#    - return:  string
#
#=============================================================================

def translateMorse(morse_dictionary, morse_tuple):
    """Translate a tuple of Morse-code symbols into an English string."""
    result = ""
    for code in morse_tuple:
        result += morse_dictionary[code]
    return result


#=============================================================================
# q10 - create function dupWords() 
#    - accept one parameter:  a tuple of strings
#    - add a meaningful docstring
#    - iterate over the tuple, determine if any word is in the tuple more
#      than one time; if so, add it to a list
#    - sort the list
#    - return the sorted list
#
#    - Example:  tuple parameter = ('yes','no','no','hi','bye','hi','hi')
#                return ['hi','no']
#
#    - RESTRICTIONS:  None
#
#    - params:  tuple (of strings)
#    - return:  list (sorted(resultantList))
#
#=============================================================================

def dupWords(words):
    """Return a sorted list of words that occur more than one time in a tuple."""
    result = []
    for word in words:
        count = 0
        for other in words:
            if word == other:
                count += 1
        if count > 1 and word not in result:
            result.append(word)
    result.sort()
    return result


#=============================================================================
# q11 - DEBUG function numOdds(intList) 
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - the program accepts a list of arbitrary numbers as parameter:
#      --- intList - a list of integers
#
#    - numOdds should iterate over the numbers in the intList and count 
#      how many of the integers are odd, then return this count
#
#    - Example:
#      intList = [1,1,4,66,-13,0,22,51]
#      return 4
#
#    - RESTRICTIONS:  do NOT re-write the function, just find/fix error(s)
#
#    - params:  list (of integers)
#    - return:  integer
#=============================================================================

def numOdds(intList):
    """Return the number of odd integers in a list."""
    count = 0
    for number in intList:
        if number % 2 != 0:
            count += 1
    return count



# ==========================================================================
# Test 2 Additional Problems From Uploaded Images
# ==========================================================================

# ==========================================================================
# q1 - create function multipleFour() to meet the conditions below
#    - accept one parameter: an integer value (x)
#
#    - return a list of all positive integers that are multiples of 4
#       and less than num.
#       --- e.g. x = 21   -> returns [4,8,12,16,20]
#       --- e.g. x = 20   -> returns [4,8,12,16]
#       --- e.g. x = -20  -> returns []
#       --- e.g. x = 4    -> returns []
#
#    - HINT: None
#
#    - RESTRICTIONS: You may not use list comprehension
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param: integer
#    - return: list
# ==========================================================================

def multipleFour(x):
    """Return positive multiples of 4 that are less than the given number."""
    result = []
    number = 4
    while number < x:
        result.append(number)
        number += 4
    return result


# ==========================================================================
# q2 - create a function named: passwordChecker()
#    - accept one parameter: one string
#
#    - Write a function that checks the strength of a password based on
#       the following criteria:
#       - At least 8 characters long
#       - Contains at least one letter
#       - Contains at least one numerical digit
#
#    - returns True if the password is strong and False otherwise
#
#    - Here are some examples:
#    - e.g. 1: s = 'Strong6 Password'   -> return True
#    - e.g. 2: s = 'passw0rd'           -> return True
#    - e.g. 3: s = 'SECURE2025'         -> return True
#    - e.g. 4: s = 'password'           -> return False
#    - e.g. 5: s = '12345678'           -> return False
#    - e.g. 6: s = 'R8?'                -> return False
#
#    - returns True if the password is strong and False otherwise
#
#    - HINT: None
#
#    - RESTRICTIONS: None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param: string
#    - return: boolean
# ==========================================================================

def passwordChecker(s):
    """Return True if a password is long enough and contains a letter and digit."""
    has_letter = False
    has_digit = False

    for char in s:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    return len(s) >= 8 and has_letter and has_digit


# ==========================================================================
# q3 - create function countNonVowelsLetters() to meet the conditions below
#    - accept one parameter: a string value
#
#    - Write a program that counts the number of non-vowels in a given string.
#
#    - it must count all the non-vowels letters
#       (Count all alphabetical characters that are not vowels (aeiouAEIOU).)
#       --- e.g. 1: parameter is "Anna!"; return value is 2
#                   'n' and 'n' are non-vowel letter
#       --- e.g. 2: parameter is "Audio"; return value is 1
#                   'd'
#       --- e.g. 3: parameter is "Louie!"; return value is 1
#                   'L'
#       --- e.g. 4: parameter is "fly"; return value is 3
#                   'f','l', and 'y'
#       --- e.g. 5: parameter is "Roar"; return value is 2
#                   'R' and 'r'
#       --- e.g. 6: parameter is "a 1 !"; return value is 0
#
#    - return resultant interger value
#
#    - HINT: None
#
#    - RESTRICTIONS: You are not allowed to use set() function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param: string
#    - return: integer
# ==========================================================================

def countNonVowelsLetters(s):
    """Count alphabetic characters in a string that are not vowels."""
    count = 0
    vowels = "aeiouAEIOU"

    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1

    return count


# ==========================================================================
# q4 - create function increaseValues() to meet the conditions below
#    - accept two parameters: a list of numbers and a number (num)
#
#    - Use a loop traversing using index numbers
#    - The function should add "num" to each value in the list.
#    - The change must happen directly in the list (do not make a new list).
#
#    - you MUST change the values within the list and NOT create a new list
#    - You may assume there are at least two values in the list.
#
#       --- Example 1: [6, 2, 1, 10], 2   -> [8, 4, 3, 12]
#       --- Example 2: [2,5], 5           -> [7, 10]
#
#    - HINT: You may use traversing over index number to make it easier
#       to update the values in the list.
#
#    - RESTRICTIONS: The change must be done in place WITHOUT using an empty list.
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params: list (of numbers)
#              integer
#    - return: None (points will be deducted if you return a value)
# ==========================================================================

def increaseValues(values, num):
    """Increase each value in the list by the given number in place."""
    for index in range(len(values)):
        values[index] += num


# ==========================================================================
# q5 - create function sharedValue() to meet the conditions below
#    - accept two seqs (string, list, or tuple) of arbitrary sizes
#
#    - returns True if the lists share at least one common member
#       False otherwise
#       --- Example 1: 'hello' and 'rainy' -> returns False
#       --- Example 2: ('a','a','z') and ['g','z','f'] -> returns True
#       --- Example 3: ('a','a','z') and 'rainy' -> returns True
#
#    - RESTRICTIONS: You are NOT allowed to use set() function.
#       You also may NOT use the "in" operator with an "if" statement.
#       'in' is allowed in the context of the for loop (e.g., for x in s1:),
#       just not as a membership test (if x in s2:).
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param: list, tuple or string
#             list, tuple or string
#    - return: boolean
# ==========================================================================

def sharedValue(seq1, seq2):
    """Return True if two sequences share at least one common value."""
    for item1 in seq1:
        for item2 in seq2:
            if item1 == item2:
                return True
    return False


# ==========================================================================
# q6 - create function divisibleByFirstTwo() to meet the conditions below
#    - accept one parameter: a list
#
#    - store the first two values (n1 and n2) into two variables
#    - returns a list of numbers starting from the index 2 (the third element)
#       to the end of the list that are divisible by n1 and n2
#
#    NOTE:
#       --- you may assume the list is not empty and has at least 3 items
#
#       --- example 1: [3,2,12,5,9,6]       -> returns [12, 6]
#       --- example 2: [3,4,4,24,12,8,10,144] -> returns [24, 12, 144]
#       --- example 3: [6,10,4,9,2,8,15,3] -> returns []
#       --- example 4: [2, 3, 5, 7]        -> returns []
#
#    - HINT: None
#
#    - RESTRICTIONS: None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params: list (of int values)
#    - return: list (of int values)
# ==========================================================================

def divisibleByFirstTwo(values):
    """Return values after the first two that are divisible by both first values."""
    n1 = values[0]
    n2 = values[1]
    result = []

    for index in range(2, len(values)):
        if n1 != 0 and n2 != 0 and values[index] % n1 == 0 and values[index] % n2 == 0:
            result.append(values[index])

    return result


# ==========================================================================
# q7 - create function sumPairs() to meet the conditions below
#    - accept one parameter: a list numeric values
#
#    - store the sum of each two adjacent values into a new list
#       note: each value in the list will be used only once
#
#       --- assume there are EVEN number of items in the list
#       You do not need to handle lists with an odd number of elements.
#
#       --- example 1:
#       - lst -> [2, 1, 4, 2, 3, 5, 1, 1] -> return [3, 6, 8, 2]
#       - 3 which is the result of (2+1)
#       - 6 which is the result of (4+2)
#       - 8 which is the result of (3+5)
#       - 2 which is the result of (1+1)
#
#       --- example 2:
#       - lst -> [-2, 4, 1, 2] -> return [2,3]
#
#    - RESTRICTIONS: None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param: list of numeric values
#    - return: list of numeric values
# ==========================================================================

def sumPairs(values):
    """Return a list containing the sums of each pair of adjacent values."""
    result = []

    for index in range(0, len(values), 2):
        result.append(values[index] + values[index + 1])

    return result

# ============================================================================
# Practice Final 3
# ============================================================================

#========================================================================== 
# q1 - create a function named:  isequilateral()
#    - add a meaningful docstring
#    - accept three parameters: three sides of a triangle (integer values)
#    - add a meaningful docstring
#    - returns True if the triangle is equilateral, False if it is not.
#    - return the total
#    - In geometry, an equilateral triangle is a triangle in which all
#       three sides have the same length. 
#
#    - param:  three integers
#    - return:  boolean
#==========================================================================

def isequilateral(side1, side2, side3):
    """Return True if all three triangle sides are equal."""
    return side1 == side2 and side2 == side3


#==========================================================================
# q2 - create a function named:  validate2Lists()
#    - add a meaningful docstring
#    - accept 2 list parameters in this order:
#    --- a list of 3-character strings, e.g. ["2KL", "ZQQ", "AEE"]
#    --- a list of 4-character strings, e.g. ["1234", "A999", "4567"]
#    - validate that each element of list 1 contains only letters
#    - validate that each element of list 2 contains only numeric strings
#    - remove any invalid elements or create new lists w/ only valid elements
#    --- INVALID characters ONLY occur in the FIRST position:
#    --- e.g. invalid 3-letter combo above:  "2KL"
#    --- e.g. invalid 4-digit numeric string above:  "A999"
#    - return two sorted valid lists (3-letter combo; 4-digit numeric string)
#
#    - param:   list
#               list
#    - return:  soreted(list1), sorted(list2)
#               
#==========================================================================

def validate2Lists(letter_list, number_list):
    """Return sorted valid letter-only strings and numeric-only strings from two lists."""
    valid_letters = []
    valid_numbers = []
    for item in letter_list:
        if item.isalpha():
            valid_letters.append(item)
    for item in number_list:
        if item.isdigit():
            valid_numbers.append(item)
    valid_letters.sort()
    valid_numbers.sort()
    return valid_letters, valid_numbers


#==========================================================================
# q3 - create function isPrime() to meet the conditions below
#    - accept one parameter: an integer
#    - add a meaningful docstring
#    - determine if the param is prime
#    A number is prime if it is evenly divisible only by 1 and itself.
#    --- e.g. 20 -> returns False
#    --- e.g. 17 -> returns True
#    - return True or False 
#
#    - param:  an int
#    - return:  a boolean
#
#    - param:  int
#    - return: Boolean
#==========================================================================

def isPrime(number):
    """Return True if a number is prime."""
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


#==========================================================================
# q4 - create function lunchCombos() to meet the conditions below
#    - accept three parameters
#    - add a meaningful docstring
#    - Suppose there is a dinning hall on campus which provide
#    - lunch combo. Every day, they have a full truck of fruits, vegies
#    - and drinks. They will pre-make lunch combos that contains one
#    - type of fruit, one type of vegie and one drink.
#
#    - write this function given available fruits, vegies and drinks
#    - as three lists, and return a list of strings as the possible combo name.
#    - each combo name should be [fruit name], [vegie name] and [drink name]
#    - as a string, for example, 'apple, carrot and smoothie'
#    - make sure there is a ', ' after fruit's name and ' and ' between
#       the last two items similar to the example
#    - e.g., fruit = ['apple', 'banana']
#            vegie = ['carrot', 'pea']
#            drink = ['root beer']
#       returns: ['apple, carrot and root beer', 'apple, pea and root beer',
#                   'banana, carrot and root beer', 'banana, pea and root beer']       
#    
#    - return the list of strings of combos.
#
#    - RESTRICTIONS:  None
#
#    - param:  list
#              list
#              list
#    - return: list
#
#==========================================================================

def lunchCombos(fruits, vegies, drinks):
    """Return all lunch combo strings using each fruit, vegetable, and drink."""
    combos = []
    for fruit in fruits:
        for vegie in vegies:
            for drink in drinks:
                combos.append(fruit + ", " + vegie + " and " + drink)
    return combos


#=============================================================================
# q5 - create function convertToUniCode() to meet the conditions below
#    - accept one parameter:  a string
#    - add a meaningful docstring
#    - create a list of the UniCode values for each character in the string
#    --- e.g. " apple" would produce the list [32, 97, 112, 112, 108, 101]
#    - Hint: ord() and chr() are built-in functions. They are used to convert
#        a character to an int and vice versa. Python ord() and chr()
#        functions are exactly opposite of each other.
#    - return the list
#
#    - RESTRICTIONS:  you may NOT use the built-in function range()
#
#    - param:  string
#    - return:  list (of integers)
#=============================================================================

def convertToUniCode(text):
    """Return a list of Unicode values for each character in a string."""
    result = []
    for ch in text:
        result.append(ord(ch))
    return result


#==========================================================================
# q6 - create function fullNames() to meet the conditions below
#    - accept two parameters:  a list of first names and a corresponding
#                              list of last names
#    - add a meaningful docstring
#    - iterate over the lists and combine the names (in order) to form   
#      full names; add them to a new list, and return the new list
#    --- e.g. first list = ["Sam", "Malachi", "Jim"]
#             last list = ["Poteet", "Strand", "Wilkins"]
#             returns ["Sam Poteet", "Malachi Strand", "Jim Wilkins"]
#    NOTE: in the return list, there must be a space between first and last names
#    NOTE: you can assume both lists have the same number of strings in them
#    - return the list of full names
#
#    - RESTRICTIONS:  None
#
#    - params:  list (of strings)
#               list (of strings)
#    - return:  list (of strings)
#=============================================================================

def fullNames(first_names, last_names):
    """Return a list of full names made from matching first and last name lists."""
    result = []
    for index in range(len(first_names)):
        result.append(first_names[index] + " " + last_names[index])
    return result


#=============================================================================
# q7 - create function readIt() to meet the conditions below
#    - accept one parameter:  a file name 
#    - add a meaningful docstring
#    - return the sum of the values in the textfile
#      --- NOTE:  the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#      --- catch a exception and returnNone if the file 
#         doesn't exist using exception handling mehtod.
#      --- don't forget to close the file
#    - you may assume all the values on the text file are integers
#    - return the sum
#
#    - RESTRICTIONS:  None
#
#    - params:  string
#    - return:  integer
#=============================================================================

def readIt(filename):
    """Return the sum of all integer values in a text file, or None if the file does not exist."""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None
    total = 0
    for line in infile:
        if line.strip() != "":
            total += int(line.strip())
    infile.close()
    return total


#=============================================================================
# q8 - create function writeEvenNumbers() to meet the conditions below
#    - accept two parameters:  a file name,
#                              and an integer value
#    
#    - open the named file for writing
#    - write to the file all the even numbers between 2 and the
#        integer value, both included.
#        Each number should be on a separate line in the file.
#      --- don't forget to close the file
#    - return the number of lines written to the file
#
#    - RESTRICTIONS:  you may NOT use the built-in function len()
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               integer
#    - return:  integer
#=============================================================================

def writeEvenNumbers(filename, number):
    """Write all even numbers from 2 through number to a file and return the line count."""
    outfile = open(filename, "w")
    count = 0
    for value in range(2, number + 1, 2):
        outfile.write(str(value) + "\n")
        count += 1
    outfile.close()
    return count


#==========================================================================
# q9 - create function translateDictionary() to meet the conditions below
#    - accept two parameters: a dictionary and a string 
#    - add a meaningful docstring
#    - each word in the string is a key for its translation in the dictionary
#    - build a translated string for the string param
#    - return the translated string
#    - Example:  dictionary = {"I": "wo", "love": "ai", "coding": "bian cheng"}
#                string = "I love coding"
#                returns: "wo ai bian cheng"
#    - Hint: you are allowed to use split() functions.
#
#    - RESTRICTIONS:  None
#
#    - params:  dictionary
#               string
#    - return:  string
#==========================================================================

def translateDictionary(dictionary, text):
    """Translate each word in a string using a dictionary."""
    words = text.split()
    result = ""
    for index in range(len(words)):
        result += dictionary[words[index]]
        if index != len(words) - 1:
            result += " "
    return result


#==========================================================================
# q10 - create function countPairs() to meet the conditions below
#    - accept one list of arbitrary integer values and an integer as parameters
#    - add a meaningful docstring
#    - find every possible pair in the list that when add up
#       is equal to the integer value
#    - returns the number of pairs
#    --- e.g. [2,5,8] and 8 -> returns 0
#    --- e.g. [2,3,4,5] and 7 -> returns 2 because
#       (4,3),(2,5)   (note that (3,4) and (4,3) are same pair and should
#                               be counted only once, (same for (2,5) and (5,2)))
#    --- e.g. [1,2,3,4] and 6 -> returns 1 because
#       (2,4)   (note: numbers should not be added to themselves. For example
#                       (3,3) could not be counted as one of the pairs.
#
#    - you may assume there is no duplication in the list
#    Restriction: None
#
#    - param:  list
#              integer
#    - return: integer
#==========================================================================

def countPairs(*args):
    """Count pairs that add to a target for either one list or two list inputs."""
    if len(args) == 3:
        list1, list2, target = args
        count = 0
        for item1 in list1:
            for item2 in list2:
                if item1 + item2 == target:
                    count += 1
        return count
    if len(args) == 2:
        numbers, target = args
        count = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    count += 1
        return count
    return 0


#=============================================================================
# q11 - DEBUG function changeValues(intList) 
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - the program accepts a list of arbitrary numbers as parameter:
#      --- intList - a list of integers
#    - this function changes the values following the pattern below:
#       --- If the index of a value is even or zero, triple this value;
#       --- If the index of a value is odd, divide the value in half.
#
#    - The changes should be done in-place.
#    - you may assume the a list of only positive integers
#
#    - Example:
#      param = [1,2,4,5]
#      param changes to [3, 1.0, 12, 2.5]
#      Note: list is a mutable data type and can be changed in-place
#
#    - RESTRICTIONS:  do NOT re-write the function, just find/fix error(s)
#
#    - params:  list (of integers)
#    - return:  None
#=============================================================================

def changeValues(intList):
    """Change list values in place by tripling even indexes and halving odd indexes."""
    for index in range(len(intList)):
        if index % 2 == 0:
            intList[index] = intList[index] * 3
        else:
            intList[index] = intList[index] / 2
    return None


# ============================================================================
# Spring 2023 Final Review
# ============================================================================

#==========================================================================
# q1 - create function greaterSum() to meet the conditions below
#    - accept 3 integer parameters
#
#    - determine which two produce the largest sum and return the resultant sum
#       --- e.g. 1: parameters are 3, 6, and 1; largest sum is 9
#       --- e.g. 2: parameters are -2, 0, and 8; largest sum is 8
#       --- e.g. 3: parameters are 7, 3, and -2; largest sum is 10
#    - return the largest sum
#
#    - RESTRICTIONS:  You may NOT use max() or min() functions. 
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   integer
#               integer
#               integer
#    - return:  integer
#==========================================================================

def greaterSum(num1, num2, num3):
    """Return the largest sum made by adding two of the three integers."""
    sum1 = num1 + num2
    sum2 = num1 + num3
    sum3 = num2 + num3
    largest = sum1
    if sum2 > largest:
        largest = sum2
    if sum3 > largest:
        largest = sum3
    return largest


#=============================================================================
# q2 - create function factorial() to meet the conditions below
#    - accept one parameter:  an integer value
#
#    - you may assume the parameter is a positive integer value
#    --- e.g. 1: parameter is (4); result is (4*3*2*1) = 24
#    --- e.g. 2: parameter is (6); result is (6*5*4*3*2*1) = 720
#    --- e.g. 3: parameter is (2); result is (2*1) = 2
#    - return resultant integer
#
#    - RESTRICTIONS:  You are NOT allowed to use math.factorial() function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  integer
#    - return:  integer
#=============================================================================

def factorial(number):
    """Return the factorial of a positive integer."""
    total = 1
    for value in range(1, number + 1):
        total *= value
    return total


#=============================================================================
# q3 - create function replace() to meet the conditions below
#    - accept three parameters:  three strings (s, oldChar, newChar)
#    - Returns a copy of s with every instance of oldChar in s replaced by newChar
#       --- e.g. 1: ("hello", "h", "j"); result is "jello"
#       --- e.g. 2: ("birth ", "i", "e"); result is "berth"
#    - return resultant string
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   string
#               string
#               string
#    - return:  string
#=============================================================================

def replace(s, oldChar, newChar):
    """Return a copy of a string with each old character replaced by the new character."""
    result = ""
    for ch in s:
        if ch == oldChar:
            result += newChar
        else:
            result += ch
    return result


#==========================================================================
# q4 - create function nCharWords() to meet the conditions below
#    - accept three parameters: a list, a string, and a number (words, char, num=3)
#    
#    - Takes a list of words, a character, and a count (defaults to 3).
#    - This function should return sorted list of words containing only words that
#       have the specified character, the specified number of times.
#
#       --- e.g. 1: (['see', 'bees', 'fly', 'breeze'], 'e', 2) ->
#                     ['see', 'bees']
#       --- e.g. 2: (['bee-eater', 'shell-less', 'fly', 'cross-section'], 's') ->
#                     ['shell-less', 'cross-section']
#
#    - RESTRICTIONS:  You may NOT use count() function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   list (of words)
#               string
#               integer
#    - return:  sorted(list) 
#==========================================================================

def nCharWords(words, char, num=3):
    """Return a sorted list of words containing a character exactly num times."""
    result = []
    for word in words:
        count = 0
        for ch in word:
            if ch == char:
                count += 1
        if count == num:
            result.append(word)
    result.sort()
    return result


#==========================================================================
# q5 - create function maxDuplicates() to meet the conditions below
#    - Accepts one parameter: a list of words
#    
#    - Find the word in word_list with the most duplicates of a character.
#       Returns a tuple, with the word, the character, and its count.
#
#       --- e.g. 1: (['fast', 'ball']) returns ('ball', 2, 'l')
#       --- e.g. 2: (['aardvark', 'mississippis', 'ssssnake']) would return ('mississippis', 5, 's')
#
#     You may assume only one word has most duplicates of a character
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of words)
#    - return:  tuple 
#==========================================================================

def maxDuplicates(word_list):
    """Return the word, highest repeated-character count, and character with the most duplicates."""
    best_word = ""
    best_char = ""
    best_count = 0
    for word in word_list:
        for ch in word:
            count = 0
            for other in word:
                if other == ch:
                    count += 1
            if count > best_count:
                best_word = word
                best_char = ch
                best_count = count
    return best_word, best_count, best_char


#=============================================================================
# q6 - create function isSorted() to meet the conditions below
#    - accept one parameter: a list of numbers
#
#    Determine if the list parameter is sorted.
#    A list is sorted in ascending order if it is empty or each item except
#    the last one is less than or equal to its successor.
#
#    Returns True if the list is sorted, False otherwise.
#
#       --- e.g. 1: ([1, 4, 8, 12]) returns True
#       --- e.g. 2: ([1, 3, 5, 2]) returns False
#       --- e.g. 3: ([5]) returns True
#       --- e.g. 4: ([]) returns True
#
#    HINT: For a list length 2 or greater, loop through the list and compare pairs
#    of items, from left to right, and return False if the first item in
#    a pair is greater.
#
#    - RESTRICTIONS:  you may NOT use sort() or sorted() functions
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of integers)
#    - return:  bool
#=============================================================================

def isSorted(numbers):
    """Return True if a list is sorted in ascending order."""
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            return False
    return True


#=============================================================================
# q7 - create function countChar() to meet the conditions below
#    - accept one parameter:  a file name
#
#    - the first line of the file contains a letter
#      count and return the number of occurances of that letter on
#      the consecutive lines
#
#      NOTE:
#           --- the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#           --- The file contains n number of lines
#           --- don't forget to close the file
#           --- you may assume there are at least two lines in the file
#
#       --- e.g. Assume this is what you see in the textfile:
############################################################# Start
#            i
#            hello world
#            this is a nice day!
#            programming is fun.
############################################################# End
#           There are no 'i's in the first line, 3 in the second line, and 2 in the third line
#           Thus the return value must be 5
#       
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  integer
#=============================================================================

def countChar(filename):
    """Return the number of times the first-line character appears in the remaining file lines."""
    infile = open(filename, "r")
    target = infile.readline().strip()
    count = 0
    for line in infile:
        for ch in line:
            if ch == target:
                count += 1
    infile.close()
    return count


#==========================================================================
# q8 - create function createWords() to meet the conditions below
#    - accept 2 parameters; a file name and a list (of lists)
#    
#    - open the filename for writing
#    - the lists in the list are all of a same size
#
#    --- e.g. 1: [ ['c', 'd', 'p'], ['a', 'o', 'e'], ['t', 'g', 't'] ]
#    --- e.g. 2: [ ['d', 'm', 'c', 'c'], ['o', 'i', 'o', 'o'], ['o', 'l', 'o', 'o'] , ['o', 'k', 'k', 'l']]
#    --- e.g. 3: [ ['w', 'c'], ['a', 'l'], ['t', 'a'], ['e', 's'], ['r', 's']]
#
#    - combine the items with the same index numbers and create a new string,
#       write the new string into the textfile
#
#    --- e.g. 1: [ ['c', 'd', 'p'], ['a', 'o', 'e'], ['t', 'g', 't'] ]
#               -> text file will be
##################################### Start
#               cat
#               dog
#               pet
##################################### End
#
#    --- e.g. 2: [ ['d', 'm', 'c', 'c'], ['o', 'i', 'o', 'o'], ['o', 'l', 'o', 'o'] , ['r', 'k', 'k', 'l']]
##################################### Start
#               door
#               milk
#               cook
#               cool
##################################### End
#
#    --- e.g. 3:[ ['w', 'c'], ['a', 'l'], ['t', 'a'], ['e', 's'], ['r', 's']]
##################################### Start
#               water
#               class
##################################### End
#
#          each resultant word must be written on a separate line
#      --- don't forget to add the newline character to each line
#      --- don't forget to close the file
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   string
#               list (of characters)
#    - return:  None
#==========================================================================

def createWords(filename, letters):
    """Write words made by combining same-index characters from a list of lists."""
    outfile = open(filename, "w")
    for col in range(len(letters[0])):
        word = ""
        for row in range(len(letters)):
            word += letters[row][col]
        outfile.write(word + "\n")
    outfile.close()
    return None


#==========================================================================
# q9 - create function makeMatrix() to meet the conditions below
#    - accept one parameter: an integer value (n)
#    
#    - create a list of strings such that the values in the n*n matrix are:
#    --- e.g. 1: n = 3
#       return value: ['123', '123', '123']
#    --- e.g. 2: n = 5
#       return value: ['12345', '12345', '12345', '12345', '12345']
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  integer
#    - return:  list
#==========================================================================

def makeMatrix(n):
    """Return an n-item list where each item is a string containing 1 through n."""
    row = ""
    for value in range(1, n + 1):
        row += str(value)
    result = []
    for _ in range(n):
        result.append(row)
    return result


#=============================================================================
# q10 - create function validateItems()
#    - accept one parameter: a list of strings
#
#       validate that each string in list has the following format:
#       --- Each string must be length of 4
#       --- The first character must be a number
#       --- The second and third character are letters
#       --- The forth character is neither a number or letter
#
#    - remove any invalid elements or create new lists w/ only valid elements
#       return the sorted list
#    --- e.g. : ["2KL", "2ZQ!", "AEE?", "5AA!"] return ["2ZQ!","5AA!"]
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of strings)
#    - return:  sorted(list)
#=============================================================================

def validateItems(items):
    """Return sorted strings with digit, letter, letter, and special-character format."""
    result = []
    for item in items:
        if len(item) == 4:
            if item[0].isdigit() and item[1].isalpha() and item[2].isalpha() and not item[3].isalnum():
                result.append(item)
    result.sort()
    return result


#=============================================================================
# q11 - DEBUG function fruitName(fruitsList) 
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - the program accepts 1 parameter:
#      --- fruitsList - name of fruits
#
#    - fruitName should iterate over the fruitsList and count 
#       how many apples and bananas are in the list, then return their counts
#       as a tuple.
#
#    - Example:
#      fruitsList = ['apple', 'Banana', 'Apple', 'cherry', 'banana', 'apple']
#      return (3,2)
#
#    - NOTE: You may assume every item that start with a or A is an apple and
#       every item that starts with b or B is a banana
#
#    - RESTRICTIONS:  do NOT re-write the function, just find/fix error(s)
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of fruit names)
#    - return:  tuple
#=============================================================================

def fruitName(fruits):
    """Return the counts of apple-like and banana-like fruit names in a tuple."""
    countApple = 0
    countBanana = 0
    for name in fruits:
        if name[0] == "a" or name[0] == "A":
            countApple += 1
        elif name[0] == "b" or name[0] == "B":
            countBanana += 1
    return countApple, countBanana


# ============================================================================
# Fall 2024 Final Review
# ============================================================================

#=============================================================================
# q1 - (5pts) create function checkStringLength() to meet the conditions below
#    - accept two values (a string and one integer value)
#
#    - Write a program that checks whether the length of a given string
#       is between zero and the specified integer value, returns the string 
#       if it falls within the range, and shortens the string otherwise and return 
#       the shortened string.
#
#       --- e.g. 1: parameters are 'hello', and 10; returns 'hello'
#                   5 is within 0 and 10
#       --- e.g. 2: parameters are 'hello world', and 5; returns 'hello'
#                   only 'hello' will be returned and the rest will be sliced.  
#       --- e.g. 3: parameters are 'bookstore', 4; returns 'book'
#
#    - return the resultant value
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   string
#               integer
#    - return:  string
#=============================================================================

def checkStringLength(text, limit):
    """Return the original string if it fits the limit, otherwise return the shortened string."""
    if len(text) <= limit:
        return text
    return text[:limit]


#=============================================================================
# q2 - (5pts) create function countUniqueVowels() to meet the conditions below
#    - accept one parameter:  a string value
#
#    - Write a program that counts the number of unique vowels in a given string.
#
#    - it must count all the unique vowels (aeiou)
#       counting both uppercase and lowercase as one character
#
#    --- e.g. 1: parameter is Anna; return value is 1 (contains 'A' and 'a') 
#    --- e.g. 2: parameter is AudiooooooOOOO; return value is 4
#    --- e.g. 3: parameter is Louie; return value is 4
#    --- e.g. 4: parameter is fly; return value is 0
#    --- e.g. 5: parameter is anna; return value is 1 
#    - return resultant value
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  integer
#=============================================================================

def countUniqueVowels(text):
    """Return the number of unique vowels found in a string, ignoring case."""
    found = []
    for ch in text.lower():
        if ch in "aeiou" and ch not in found:
            found.append(ch)
    return len(found)


#=============================================================================
# q3 - (10pts) create function sortNumbers() to meet the conditions below
#    - accept 3 integer parameters
#
#    - write a program that takes three numbers as input and returns
#       them in ascending order.
#       You are only allowed to use if statements for comparison
#       and swapping.
#       --- e.g. 1: parameters are 3, 6, and 1; return value is (1,3,6)
#       --- e.g. 2: parameters are -2, 0, and 8; return value is (-2,0,8)
#       --- e.g. 3: parameters are 7, 3, and -2; return value is (-2,3,7)
#    - return the resultant tuple
#
#    - RESTRICTIONS:  You may NOT use max(), min(), or sort()/sorted() functions. 
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   integer
#               integer
#               integer
#    - return:  tuple
#=============================================================================

def sortNumbers(num1, num2, num3):
    """Return three numbers in ascending order as a tuple."""
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    if num2 > num3:
        temp = num2
        num2 = num3
        num3 = temp
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    return num1, num2, num3


#=============================================================================
# q4 - (10pts) create function isPalindrome() to meet the conditions below
#    - accept one parameter:  a value (either type integer or string)
#    - check if a given value is a palindrome.
#       a palindrome value reads the same forwards and backwards
#       --- e.g. 1: 12321; result is True
#       --- e.g. 2: 'anna'; result is True
#       --- e.g. 5: 'hello'; result is False
#       --- e.g. 6: 23456; result is False
#    - return a boolean value
#
#    - RESTRICTIONS:  You must NOT use string slicing methods or reverse() method
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   a value (could be type integer, or string)
#    - return:  boolean
#=============================================================================

def isPalindrome(value):
    """Return True if a string or integer reads the same forward and backward."""
    text = str(value)
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


#=============================================================================
# q5 - (10pts) create function findArmstrong() to meet the conditions below
#    - accept two parameters: two integer values
#    
#    - Write a program that finds and returns a list of all Armstrong
#       numbers in a given range, including both start and end value.       
#
#       Armstrong number is a number that is equal to the sum of its
#       own digits when they are raised to the power of the number
#       of digits. 153, 370, 1634, and 9474 are examples of
#       the Armstrong numbers.
#
#       Assume the start value is greater than 100.
#
#       --- e.g. 1: parameters are 100 and 400 -> a list of armstrong numbers
#                   from 100 to 400 is [153, 370, 371]
#                   in the range numbers from 100-400 there are only three values
#                   that fits the given criteria
#                       153 = 1**3 + 5**3 + 3**3
#                       370 = 3**3 + 7**3 + 0**3
#                       371 = 3**3 + 7**3 + 1**3
#
#       --- e.g. 2: parameters are 1500 and 2000 -> a list of armstrong numbers
#                   from 1500 to 2000 is [1634]
#                       1634 = 1**4 + 6**4 + 3**4 + 4**4
#
#       --- e.g. 3: parameters are 100 and 2000 -> a list of armstrong numbers
#                   from 100 to 2000 is [153, 370, 371, 407, 1634]
#                       
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   integer
#               integer
#    - return:  list
#=============================================================================

def findArmstrong(start, end):
    """Return a list of Armstrong numbers between start and end, inclusive."""
    result = []
    for number in range(start, end + 1):
        text = str(number)
        power = len(text)
        total = 0
        for ch in text:
            total += int(ch) ** power
        if total == number:
            result.append(number)
    return result


#=============================================================================
# q6 - (10pts) create function findNumRange() to meet the conditions below
#    - accept one value: a list (of tuples)
#
#    - Write a program that computes the absolute difference between
#       the two numbers in each tuple and stores the result in a list.
#
#       --- e.g. 1: parameter is [(4,6), (10,-2), (0,-5), (12,5)]
#                   the return value is: [2, 12, 5, 7]
#
#    - return the resultant value
#
#    - RESTRICTIONS:  Not allowed to used abs() function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   list (of tuples)
#    - return:  list
#=============================================================================

def findNumRange(tuple_list):
    """Return absolute differences for each pair in a list of tuples."""
    result = []
    for pair in tuple_list:
        difference = pair[0] - pair[1]
        if difference < 0:
            difference = -difference
        result.append(difference)
    return result


#=============================================================================
# q7 - (10pts) create function isSorted5() to meet the conditions below
#    - accept one parameter: a list of numbers
#
#    Determine if all the items in the list are divible by 5 and
#    the list parameter is sorted in ascending order.
#
#    A list is sorted in ascending order if it is empty or each item except
#    the last one is smaller than or equal to its successor.
#
#    Returns True if the all the items in the list are divisible by 5 and
#       is sorted in ascending order, False otherwise.
#
#       --- e.g. 1: ([12, 8, 4, 1]) returns False
#       --- e.g. 2: ([0, 5, 10, 15]) returns True
#       --- e.g. 3: ([5]) returns True
#       --- e.g. 4: ([]) returns True
#       --- e.g. 5: ([5, 10, 20, 15]) returns False
#
#    - RESTRICTIONS:  you must NOT use sort() or sorted() functions
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of integers)
#    - return:  boolean
#=============================================================================

def isSorted5(numbers):
    """Return True if every number is divisible by 5 and the list is sorted ascending."""
    for index in range(len(numbers)):
        if numbers[index] % 5 != 0:
            return False
        if index < len(numbers) - 1 and numbers[index] > numbers[index + 1]:
            return False
    return True


#=============================================================================
# q8 - (10pts) create function findLargestRange() to meet the conditions below
#    - accept one parameter:  a file name
#
#    - the text file contains n number of lines
#    - each line in the text file contains two numbers that are separated
#       by a space. Find the difference between the two numbers and return
#       the largest difference.
#
#      NOTE:
#           --- the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#           --- The file contains an arbitrary number of lines
#           --- catch an exception and return None if the file 
#               doesn't exist using exception handling method.
#           --- don't forget to close the file
#           --- you may assume there is at least one line in the file
#
#       --- e.g. as an example, assume this is what you see in the textfile:
############################################################# Start
#            3 6 
#            9 2
#            1 10
#            2 4
#            20 1
############################################################# End
#           the absolute difference in Ln1: 3
#           the absolute difference in Ln2: 7
#           the absolute difference in Ln3: 9
#           the absolute difference in Ln4: 2
#           the absolute difference in Ln5: 19
#
#           The last line in the text file generate the largest difference.
#           Thus, the return value is 19
#       
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  integer
#=============================================================================

def findLargestRange(filename):
    """Return the largest absolute difference between two numbers on each file line, or None if missing."""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None
    largest = None
    for line in infile:
        parts = line.split()
        difference = int(parts[0]) - int(parts[1])
        if difference < 0:
            difference = -difference
        if largest is None or difference > largest:
            largest = difference
    infile.close()
    return largest


#=============================================================================
# q9 - (10pts) create function countSpecialChar() to meet the conditions below
#    - accept 2 parameters; a file name and a list of strings
#    
#    - open the file for writing
#
#    - write a program to count the number of special characters
#       in any item in the list.
#
#       Here is the list of special character "#!@#$%^&*()-_=+|{};:/?.>"
#       that you need to look for.
#
#    - Write out each word and its count of special character into the textfile 
# 
#    --- e.g. 1: ['Cyndy', 'This is a nice day!', '#hello#']
#               -> text file will be
##################################### Start
#               Cyndy 0
#               This is a nice day! 1
#               #hello# 2
##################################### End
#
#      --- don't forget to add a space between the word and its count
#      --- don't forget to add a newline character to each line
#      --- don't forget to close the file
#
#    - HINT: None
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   string
#               list (of strings)
#    - return:  None
#=============================================================================

def countSpecialChar(filename, words):
    """Write each string and its special-character count to a file."""
    specials = "#!@#$%^&*()-_=+|{};:/?.>"
    outfile = open(filename, "w")
    for word in words:
        count = 0
        for ch in word:
            if ch in specials:
                count += 1
        outfile.write(word + " " + str(count) + "\n")
    outfile.close()
    return None


#==========================================================================
# q10 - (10pts) create function wordFrequency() to meet the conditions below
#    - accept one parameter: a string (a paragraph)
#    
#    - Write a program that counts the frequency of words in a given text
#       and stores the results in a dictionary.
#
#       The keys in the dictionary should NOT contain any special characters.
#           Here is the list of special characters you must exclude:
#           "#!@#$%^&*()-_=+|{};:/?.>"
#
#       You may assume the special characters are only on the tail of a word.
#       You may also assume all the words are seperated by a space.
#       Example 1: It is a nice day!
#       Example 2: char* is a tuple! Is tuple char a container? 
#
#    --- e.g. 1: text = "This is a sample text to demonstrate word frequency.
#                   This text will be used for testing!"
#       return dictionary:
#       Incorrect output: {'This': 2, 'is': 1, 'a': 1, 'sample': 1,
#                           'text': 2, 'to': 1, 'demonstrate': 1, 'word': 1,
#                           'frequencey.': 1, 'will': 1, 'be': 1, 'used': 1,
#                           'for': 1, 'testing!': 1}
#       It is incorrect because "frequencey" and "testing" have tailing special characters.
#
#       Correct output:   {'This': 2, 'is': 1, 'a': 1, 'sample': 1,
#                           'text': 2, 'to': 1, 'demonstrate': 1, 'word': 1,
#                           'frequency': 1, 'will': 1, 'be': 1, 'used': 1,
#                           'for': 1, 'testing': 1}
#
#    --- e.g. 2: text = "hello Tom. This is a nice day Tom!"
#       return dictionary:
#       Incorrect output: {'hello': 1, 'Tom.': 1, 'this': 1, 'is': 1,
#                           'a': 1, 'nice': 1, 'day': 1, 'Tom!': 1}
#       It is incorrect because the two "Tom"s have tailing special characters.
#
#       Correct output:   {'hello': 1, 'Tom': 2, 'this': 1, 'is': 1,
#                           'a': 1, 'nice': 1, 'day': 1}
#
#    - HINT2: You may use split() method to seperate the words in a string.
#           example: s = "hello world. This is a nice day!"
#                    ss = s.split() ->
#                    ss will be
#               ['hello', 'world.', 'This', 'is', 'a', 'nice', 'day!']
#
#    - RESTRICTIONS:  You may NOT use list comprehension to solve this problem.
#       If you are not sure what list comprehension is, you can always ask me 
#       to check your code!
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  dictionary
#==========================================================================

def wordFrequency(text):
    """Return a dictionary counting each word after removing trailing special characters."""
    specials = "#!@#$%^&*()-_=+|{};:/?.>"
    result = {}
    words = text.split()
    for word in words:
        while len(word) > 0 and word[-1] in specials:
            word = word[:-1]
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


#=============================================================================
# q11 - (5pts) DEBUG function letterFrequency() to meet the conditions below
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - accept a tuple
#       The function stores each unique letter and its count
#       in the dictionary.
#       You may assume all the letters are lowercase
#
#       --- Example 1: ("a", "b", "a", "a", "b")
#           resultant dictionary: {"a": 3, "b": 2}
#
#    - RESTRICTIONS:  do NOT re-write the function, just find/fix error(s)
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   tuple 
#    - return:  dictionary
#=============================================================================

def letterFrequency(t):
    """Return a dictionary containing each unique item in a tuple and its count."""
    result = {}
    for item in t:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


#==========================================================================
# q12 - (5pts) DEBUG function makeMatrix()
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - accept one parameter: an integer number (n)
#
#    - e.g.: for n=5
#       create a list of n strings each containing the numbers 1 through n:
#    ['12345', '12345', '12345', '12345', '12345']
#
#    - RESTRICTIONS:  do NOT re-write the function, just find/fix error(s)
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  integer
#    - return:  list
#==========================================================================

def makeMatrix(n):
    """Return an n-item list where each item is a string containing 1 through n."""
    row = ""
    for value in range(1, n + 1):
        row += str(value)
    result = []
    for _ in range(n):
        result.append(row)
    return result


#==========================================================================
# q13 - (5 Extra pts) create function sumNum() to meet the conditions below
#    - accept one parameter: an n-character string
#
#    - find all the string numbers in the string, convert them to integer
#      and add them together. All the numbers are separated by '-'
#    
#    - return the integer total
#
#    --- e.g. "2-5", returns 7
#    --- e.g. "3-5-12-5", returns 25
#    --- e.g. "5-1-3-100", returns 109
#
#    - HINT: None
#
#    - RESTRICTIONS:  You may NOT use split() functions
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   string
#    - return:  integer
#==========================================================================

def sumNum(text):
    """Return the sum of numbers in a string, handling either single digits or hyphen-separated numbers."""
    if "-" in text:
        total = 0
        current = ""
        for ch in text:
            if ch == "-":
                if current != "":
                    total += int(current)
                    current = ""
            else:
                current += ch
        if current != "":
            total += int(current)
        return total
    total = 0
    for ch in text:
        if ch.isdigit():
            total += int(ch)
    return total


#=============================================================================
# q14 - (5 Extra pts) create function PalindromePairFinder()
#           to meet the conditions below
#    - accept one parameter:  a list (of strings)
#    - Write a function that takes a list of strings and returns all unique
#       strings from the list that, when concatenated form a palindrome.
#
#       a palindrome value reads the same forwards and backwards
#       You may assume all the strings consist of lowercase characters
#
#       --- e.g. 1: ["rot", "cat", "race", "car", "ator"];
#                   returns sorted["racecar", "rotator"]
#                   Avoid returning duplicate strings
#
#    - return the sorted list 
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   a list (of strings)
#    - return:  sorted(list)
#=============================================================================

def PalindromePairFinder(words):
    """Return sorted unique concatenations from pairs of strings that form palindromes."""
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                combined = words[i] + words[j]
                if combined == combined[::-1] and combined not in result:
                    result.append(combined)
    result.sort()
    return result


#==============================================================================
# TEST 2 LABS AND PRACTICE PROBLEMS
# Added from uploaded Lab 17-22 and Test2_1 through Test2_4 files.
# Function names are preserved from the original files. Some names repeat in
# different practice sets, so use the section labels below to tell them apart.
#==============================================================================


#==============================================================================
# TEST 2 LABS - LAB 17: Default Arguments, *args, and Custom Range
# Source file: lab17.py
#==============================================================================

#Rustambek Saidniyozov  4/10/2026
#CSC131-001


def greet(name, msg="Good morning!"):
    """Prints a greeting for a name."""
    print(f"Hello {name}, {msg}")

def greetMany(*names):
    """Prints a greeting for each inputed name."""
    for name in names:
        print(f"Hello {name}")

def myRange(start=0, end=None, step=1):
    """Returns a list of numbers like the Python's range function."""
    result = []

    if end is None:
        end = start
        start = 0

    if step == 0:
        return result

    if step > 0:
        i = start
        while i < end:
            result.append(i)
            i += step
    else:
        i = start
        while i > end:
            result.append(i)
            i += step

    return result

def main():
    # Problem 1 
    greet("Kate")
    greet("Bruce", "How do you do?")
    print()

    # Problem 2 
    greetMany("Alice")
    print()
    greetMany("Monica", "Luke", "Steve", "John")
    print()

    # Problem 3 
    print(myRange(5))          # [0,1,2,3,4]
    print(myRange(1, 5))       # [1,2,3,4]
    print(myRange(1, 10, 2))   # [1,3,5,7,9]
    print(myRange(10, 1, -2))  # [10,8,6,4,2]

# main() call removed so this master study file does not run interactive code automatically.


#==============================================================================
# TEST 2 LABS - LAB 18: File Reading and Writing Practice
# Source file: lab18.py
#==============================================================================


#=============================================================================
# PROGRAM PURPOSE:... Lab 18 
# AUTHOR:............ Saidniyozov, Rustambek
# COURSE:............ CSC 131-001
# TERM:.............. XX
# COLLABORATION:..... None
#=============================================================================



#=============================================================================
# q1 - create function average() to meet the conditions below
#    - accept one parameter:  a file name (string)
#    - add a meaningful docstring
#    - read all the lines from the file and calculate the average value;
#      strip the newline characters from every line before converting them 
#      into int values
#      ---NOTE:  the file is automatically generated when this file
#                is run and it is placed in the same directory as
#                your file
#      --- don't forget to close the file
#      --- you may assume the textfile is NOT empty
#    - return the average value
#
#   RESTRICTIONS:  None
#
#    - params:  string
#    - return:  int
#=============================================================================

def average(filename):
    """Calculates and returns the average of integer values."""
    total = 0
    count = 0

    file = open(filename, 'r')

    for line in file:
        num = int(line.strip())
        total += num
        count += 1

    file.close()

    return total / count


#=============================================================================
# q2 - create function minMax() to meet the conditions below
#    - accept one parameter:  a file name 
#    - add a meaningful docstring
#    - read all the lines from the file and calculate the min and max values;
#      strip the newline characters from every line before converting them 
#      into int values
#      ---NOTE:  the file is automatically generated when this file
#                is run and it is placed in the same directory as
#                your file
#      --- don't forget to close the file
#      --- you may assume the textfile is NOT empty
#    - return the min and max as a tuple (min value, max value)
#
#   RESTRICTIONS:  None
#
#    - params:  string
#    - return:  tuple
#=============================================================================


def minMax(filename):
    """Reads the integers from the file and returns the minimum and maximum as a tuple."""
    file = open(filename, 'r')

    first = True

    for line in file:
        num = int(line.strip())

        if first:
            min_val = num
            max_val = num
            first = False
        else:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num

    file.close()

    return (min_val, max_val)


#=============================================================================
# q3 - create function readLines() to meet the conditions below
#    - accept one parameter:  a file name 
#    - add a meaningful docstring
#    - read all the lines from the file and concatenate them into a
#      single string; strip the newline characters from every line before
#      concatenating; put a space between each line you concatenate
#      ---NOTE:  the file is automatically generated when this file
#                is run and it is placed in the same directory as
#                your file
#      --- don't forget to close the file
#    - return the concatenation lines as a string
#
#   RESTRICTIONS:  None
#
#    - params:  string
#    - return:  string
#=============================================================================

def readLines(filename):
    """Reads lines, strips newlines, and returns them as one space-separated string."""
    file = open(filename, 'r')

    result = ""

    for line in file:
        result += line.strip() + " "

    file.close()

    return result.strip()




#=============================================================================
# q4 - create function writeAFile() to meet the conditions below
#    - accept two parameters:  a string (name of a file)
#                              a list
#    - add a meaningful docstring
#    - open the filename for writing
#    - write to the file all of the items in the list.
#        Each item should be on a separate line in the file. 
#        Count the number of lines written to the file.
#      --- don't forget to close the file
#    - return the number of written lines
#
#    Restriction:  you may NOT use the built-in function len()
#
#    - params:  string
#               list
#    - return:  integer
#=============================================================================


def writeAFile(filename, lst):
    """Writes each item from a list on separate lines and returns the number of lines."""
    file = open(filename, 'w')

    count = 0

    for item in lst:
        file.write(str(item) + "\n")
        count += 1

    file.close()

    return count


#==============================================================================
# TEST 2 LABS - LAB 19: Character Counting and File Sum Practice
# Source file: lab19 (1).py
#==============================================================================


#=============================================================================
# PROGRAM PURPOSE:... Lab 19
# AUTHOR:............ Saidniyozov, Rustambek
# COURSE:............ CSC 131-001
# TERM:.............. XXX
# COLLABORATION:..... None
#=============================================================================


#=============================================================================
# q1 - create function countXChars() to meet the conditions below
#    - accept two parameters:  a string and a character (char)
#    - add a meaningful docstring
#    - count the number of "char" character in the string
#    - return the number of characters
#   example:
#   input string: "it    is a     nice     day!", char = 'i'
#   return value: 3
#
#   Restriction:  may NOT use the count() function
#
#    - params:  string
#               string
#    - return:  integer
#=============================================================================

def countXChars(s, ch):
    """Counts how many times a specific character appears in a string."""
    count = 0

    for c in s:
        if c == ch:
            count += 1

    return count



#=============================================================================
# q2 - create function countXCharsRead() to meet the conditions below
#    - accept two parameters:  a filename and a character (char)
#    - add a meaningful docstring
#    - read the first line from the textfile
#    - count the number of "char" character in that line
#    - strip the newline characters from the line before processing it
#    - you may assume there is only one line in the textfile
#      ---NOTE:  the file is automatically generated when this file
#                is run and it is placed in the same directory as
#                your file
#      --- don't forget to close the file
#    - return the number of characters
#   example:
#   input string: "it    is a     nice     day!", char = 'i'
#   return value: 3
#
#   Restriction:  may NOT use the count() function
#
#    - params:  string
#               string
#    - return:  integer
#=============================================================================

def countXCharsRead(filename, ch):
    """Reads the first line of a file and counts how many times a specific character appears in it."""
    file = open(filename, 'r')

    line = file.readline().strip()

    file.close()

    count = 0

    for c in line:
        if c == ch:
            count += 1

    return count


#=============================================================================
# q3 - create function countXCharsReadLines() to meet the conditions below
#    - accept two parameters:  a filename and a character (char)
#    - add a meaningful docstring
#    - read the lines from the textfile
#    - count the number of "char" character in the entire textfile
#    - strip the newline characters from the lines before processing them
#    - you may assume there are more than one lines in the textfile
#      ---NOTE:  the file is automatically generated when this file
#                is run and it is placed in the same directory as
#                your file
#      --- don't forget to close the file
#    - return the number of characters
#   example:
#   inputfile: it is a nice day!
#              I like programming.
#              this is the third line!
#   char = 'i'
#   return value: 9
#
#   Restriction:  may NOT use the count() function
#
#    - params:  string
#               string
#    - return:  integer
#=============================================================================


def countXCharsReadLines(filename, ch):
    """Counts how many times a character appears in all lines of a file."""
    count = 0

    file = open(filename, 'r')

    for line in file:
        for c in line:
            if c == ch:
                count += 1

    file.close()

    return count


#==========================================================================
# q4 - create function sumValues() to meet the conditions below
#    - accept one parameters:  a filename
#    - add a docstring
#    - calculate the sum of all the values in the textfile
#    - return the numeric sum of all the values
#    --- e.g.1 if file contains 2
#                               9
#                               -5
#                               1
#           sum is 7
#
#    --- e.g.2 if file contains 20
#                               -1
#                               -2
#           sum is 17
#
#    Restriction: You are NOT allowed to use built in sum() function!
#
#    - params:  string
#    - return:  numeric value
#==========================================================================

def sumValues(filename):
    """Calculates and returns the sum of all integers that are line-by-line in a file."""
    total = 0

    file = open(filename, 'r')

    for line in file:
        num = int(line.strip())
        total += num

    file.close()

    return total




#==========================================================================
# q5 - create function sumValuesWrite() to meet the conditions below
#    - accept two parameters:  filename1, filename2
#    - add a docstring
#    - calculate the sum of all the values in the textfile filename1
#    - write out the sum into the filename2
#    --- e.g.1 if file contains 2
#                               9
#                               -5
#                               1
#           sum is 7
#
#    --- e.g.2 if file contains 20
#                               -1
#                               -2
#           sum is 17
#
#    Restriction: You are not allowed to use built in sum() function!
#
#    - params:  string
#               string
#    - return:  None
#==========================================================================

def sumValuesWrite(filename1, filename2):
    """Calculates the sum of values from filename1 and writes the result to filename2."""
    total = 0

    file1 = open(filename1, 'r')

    for line in file1:
        num = int(line.strip())
        total += num

    file1.close()

    file2 = open(filename2, 'w')
    file2.write(str(total))
    file2.close()


#==============================================================================
# TEST 2 LABS - LAB 20: Phone Spell Program
# Source file: lab20.py
#==============================================================================

#Rustambek Saidniyozov
#CSC-131
#Lab 20
def getPhoneSpell():
    """
    Get user input and validate format 123-456-abcd.
    """
    while True:
        s = input("Enter phone spell (format 123-456-abcd): ")

        if len(s) != 12:
            print("Invalid length.")
            continue

        if s[3] != '-' or s[7] != '-':
            print("Dashes must be in position 4 and 8.")
            continue

        if not s[0:3].isdigit():
            print("First 3 must be digits.")
            continue

        if not s[4:7].isdigit():
            print("Digits 5-7 must be digits.")
            continue

        if not s[8:12].isalpha():
            print("Last 4 must be letters.")
            continue

        return s
    
def displayPhoneNumber(phone_spell):
    """
    Convert last 4 letters to phone keypad numbers and return full number.
    """
    keypad = {
        'a':'2','b':'2','c':'2',
        'd':'3','e':'3','f':'3',
        'g':'4','h':'4','i':'4',
        'j':'5','k':'5','l':'5',
        'm':'6','n':'6','o':'6',
        'p':'7','q':'7','r':'7','s':'7',
        't':'8','u':'8','v':'8',
        'w':'9','x':'9','y':'9','z':'9'
    }

    last_four = phone_spell[8:].lower()
    converted = ""

    for ch in last_four:
        converted += keypad[ch]

    return phone_spell[:8] + converted

def main():

    
    print('-'*51)
    print('This program allows the user to enter a spelled')
    print('phone number for the last four digits and generates')
    print('the phone number that produces that spelling')
    print('-'*51)

    
    terminate = False

    while not terminate:
        phone_spell = getPhoneSpell()
        number = displayPhoneNumber(phone_spell)
        print(number)

        
        response = input('\nEnter another phone spell? (y/n): ')
        if response.lower() == 'n':
            terminate = True


# main() call removed so this master study file does not run interactive code automatically.


#==============================================================================
# TEST 2 LABS - LAB 21: Set and Dictionary Letter Practice
# Source file: lab21.py
#==============================================================================


#=============================================================================
# PROGRAM PURPOSE:... Lab XX 
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-00X
# TERM:.............. XXXX
# COLLABORATION:..... None
#=============================================================================


#=============================================================================
# q1 - create function countUniqueChars() to meet the conditions below
#    - accept one parameters:  a string 
#    - add a meaningful docstring
#    - count the number of unique characters in the input string
#    - return the number of characters
#   example:
#   input string: "it    is a     nice     day!"
#   return value: 11
#
#   Restriction:  you must use the built-in function set() to solve the problem
#
#    - params:  string
#    - return:  integer
#=============================================================================

def countUniqueChars(s):
    """
    Count and return the number of unique characters in a string.
    """
    return len(set(s))


#=============================================================================
# q2 - create function countUniqueLetters() to meet the conditions below
#    - accept one parameters:  a string 
#    - add a meaningful docstring
#    - count the number of letter characters in the input string
#    - return the number of letter characters
#   example:
#   input string: "it    is a     nice     day!"
#   return value: 9
#
#   Hint: Look up the function isalpha()
#   Restriction:  you must use the built-in function set() to solve the problem
#
#    - params:  string
#    - return:  integer
#=============================================================================


def countUniqueLetters(s):
    """
    Count and return the number of unique alphabetic letters in a string.
    """
    letters_only = [ch for ch in s if ch.isalpha()]
    return len(set(letters_only))



#=============================================================================
# q3 - create function countAllLetters() to meet the conditions below
#    - accept one parameters:  a string 
#    - add a meaningful docstring
#    - count the number of times that each letter appears
#       with upper/lower case letters counted together.
#    - return the sorted list containing every letter and its count as pairs. 
#   example:
#   input string:       "This   is a   short  line"    
#   return sorted list: [('a', 1), ('e', 1), ('h', 2), ('i', 3), ('l', 1),
#                   ('n', 1), ('o', 1), ('r', 1), ('s', 3), ('t', 2)]
#
#
#   Hint: Look up function sorted(), isalpha(), count(), lower() and upper()
#   Restriction:  you must use the built-in function set() to solve the problem
#
#    - params:  string
#    - return:  list
#=============================================================================


def countAllLetters(s):
    """
    Count occurrences of each alphabetic letter (case-insensitive)
    and return a sorted list of (letter, count) pairs.
    """
    s = s.lower()
    letters = [ch for ch in s if ch.isalpha()]
    
    result = []
    
    for ch in sorted(set(letters)):
        result.append((ch, letters.count(ch)))
    
    return result


#==============================================================================
# TEST 2 LABS - LAB 22: Morse Code Program
# Source file: lab22.py
#==============================================================================

def build_morse_dict():
    """Return dictionary mapping characters to Morse code."""
    return {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--'
    }


def english_to_morse():
    """Convert English to Morse with required formatting."""
    morse_dict = build_morse_dict()

    print("Enter English message, one sentence per line.")
    print("End each sentence with a period (hit return when done)")

    while True:
        sentence = input("> ")

        if sentence == "":
            break

        words = sentence.strip().split()

        for word in words:
            for ch in word:
                ch = ch.upper()
                if ch in morse_dict:
                    print(morse_dict[ch])
            print()  

        print()  


def morse_to_english():
    """Convert Morse to English with required formatting."""
    morse_dict = build_morse_dict()
    reverse_dict = {v: k for k, v in morse_dict.items()}

    print("Enter morse-coded letters one per line.")
    print("Include one blank line between words, and two blank lines between sentences")
    print("(enter 'q' when done)")

    result = ""
    blank_count = 0

    while True:
        line = input("> ")

        if line == 'q':
            break

        if line == "":
            blank_count += 1
            if blank_count == 1:
                result += " "   
            elif blank_count == 2:
                result += "\n"  
            continue

        blank_count = 0

        if line in reverse_dict:
            result += reverse_dict[line]
        else:
            print("Invalid Morse code.")

    print(result)


def main():
    while True:
        choice = input(
            "\nThis program will convert between English and Morse code.\n"
            "(E)nglish to Morse code, or (M)orse code to English? "
        ).lower()

        if choice == 'e':
            english_to_morse()
            break
        elif choice == 'm':
            morse_to_english()
            break
        else:
            print("Invalid input. Try again.")


# main() call removed so this master study file does not run interactive code automatically.


#==============================================================================
# TEST 2 PRACTICE - Test2_1 Practice Problems
# Source file: Test2_1(1).py
#==============================================================================

# PROGRAM PURPOSE:............. Test 2 - Programming Portion
# (1 point) AUTHOR:............ Saidniyozov Rustambek
# COURSE:...................... CSC 131-001
# TERM:........................ XXX
# YOU MUST NOT CONSULT ANYONE (OTHER THAN YOUR INSTRUCTOR) ON
# ANYTHING ON THIS TEST
#==========================================================================
## Read and follow all instructions carefully
##
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
##
## You may use your editor, help from the shell, your textbooks,
## computer programs previously written by you,
## and the lecture notes as reference.
## No other resources can be used during the test.
## You MAY NOT visit any web site or Google anything
## No additional import statements please
##
## You must include a meaningful docstring with each function
##
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.
#==========================================================================

## NO ADDITIONAL IMPORT STATEMENTS ALLOWED

#==========================================================================
# q1 - create function temperatureConv() to meet the conditions below
#    - accept 2 parameters: a letter and a number (temp)
#    - converts the varibale temp to 'Fahrenheit' or 'Celsius' depending on
#    - the parameter 'letter'
#    - return -1 if letter is not F,f,C, or c
#    F->C: (temp - 32) * 5/9
#    C->F: (temp * 9/5) + 32
#    --- e.g. submitted letter is f and temp is 65; return value is 18
#    --- e.g. submitted letter is F and temp is 42; return value is 5
#    --- e.g. submitted letter is c and temp is 20; return value is 68
#    --- e.g. submitted letter is C and temp is 40; return value is 104
#    --- e.g. submitted letter is k and temp is 65; return -1
#    - Returns converted temperature as an int value
#
#    - RESTRICTION: None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   string
#               integer
#    - return:  int
#==========================================================================

def temperatureConv(letter, temp):
    """Converts temperature between Celsius and Fahrenheit based on the given letter."""
    if letter in ['f', 'F']:
        return int((temp - 32) * 5/9)
    elif letter in ['c', 'C']:
        return int((temp * 9/5) + 32)
    else:
        return -1



#=============================================================================
# q2 - create function backward() to meet the conditions below
#    - accept one parameter:  a positive integer value (num)
#    - then return a list that includes numbers from num 
#    - all the way to zero in descending order including 0.
#        --- Example 1: 5 -> returns [5, 4, 3, 2, 1, 0]
#        --- Example 2: 1 -> returns [1,0]
#        --- Example 3: 8 -> returns [8, 7, 6, 5, 4, 3, 2, 1, 0]
#
#    - RESTRICTIONS:  You are allowed to use list() function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   integer 
#    - return:  list
#=============================================================================

def backward(num):
    """Returns a list counting down from num to 0."""
    return list(range(num, -1, -1))




#==========================================================================
# q3 - create function sumEven() to meet the conditions below
#    - accept two integer values, p1 and p2, as parameters
#    - return the sum of all even numbers between p1 and p2 inclusive.
#    - Assume the first parameter is always smaller or equal to the
#       second parameter
#       --- Example 1: 4 and 10 -> returns 28 (4+6+8+10)
#       --- Example 2: 10 and 10 -> returns 10
#       --- Example 3: 11 and 11 -> returns 0
#       --- Example 4: 11 and 13 -> returns 12
#    - return the sum of even numbers
#
#    - RESTRICTIONS: None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#
#    - param:  integer
#              integer
#    - return: integer
#==========================================================================

def sumEven(p1, p2):
    """Returns the sum of all even numbers between p1 and p2 inclusive."""
    total = 0
    for i in range(p1, p2 + 1):
        if i % 2 == 0:
            total += i
    return total


        
#==========================================================================
# q4 - create function convertToInts() to meet the conditions below
#    - accept a list of strings as a parameter
#    - add a meaningful docstring
#    - iterate over the list and convert each value to a integer
#    - You may assume each string contains a value that can be converted
#    - to an int.
#
#    - you must change the values within the list and not create a new list
#
#    --- e.g. ["2","5","23","7","1","12","1"] -> [2, 5, 23, 7, 1, 12, 1]
#    
#    - RESTRICTIONS:  None
#
#    - param:  list of strings
#    - return: None
#
#==========================================================================

def convertToInts(lst):
    """Converts all string elements in the list to integers in-place."""
    for i in range(len(lst)):
        lst[i] = int(lst[i])



#==========================================================================
# q5 - create function fullNames() to meet the conditions below
#    - accept two parameters:  a list of first names and a corresponding
#                              list of last names
#    
#    - iterate over the lists and combine the names (in order) to form   
#      full names (with a space between the first and last names);
#      add them to a new list, and return the new list
#       --- Example: first list = ["Sam", "Malachi", "Jim"]
#             second list = ["Poteet", "Strand"]
#
#             returns ["Sam Poteet", "Sam Strand",
#                      "Malachi Poteet", "Malachi Strand",
#                      "Jim Poteet", "Jim Strand"]
#
#    - return the list of full names
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  list (of strings)
#               list (of strings)
#    - return:  list (of strings)
#==========================================================================

def fullNames(firstNames, lastNames):
    """Combines first and last names into a list of full names."""
    result = []
    for first in firstNames:
        for last in lastNames:
            result.append(first + " " + last)
    return result
  


#=============================================================================
# q6 - create function readNLines() to meet the conditions below
#    - accept two parameters:  a file name and a number corresponding
#                              to the number of lines to be read
#    
#    - read the first N lines from the file and concatenate them into a
#      single string;
#    - return the string
#      NOTE:
#           --- the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#           --- strip the newline characters from every line before
#               concatenating
#           --- put a space between each line you concatenate
#           --- don't forget to close the file
#           --- you may assume N is less or equal to the number of lines in the textfile
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               integer
#    - return:  string
#=============================================================================

def readNLines(filename, n):
    """Reads the first n lines from a file and returns them as one string."""
    file = open(filename, 'r')
    result = ""

    for i in range(n):
        line = file.readline().strip()
        if i > 0:
            result += " "
        result += line

    file.close()
    return result
        


#==========================================================================
# q7 - create function writeSum() to meet the conditions below
#    - accept 2 parameters; a str (filename) & a 2-D list (arbitrary numbers)
#    - open the filename for writing
#    - iterate over the list and write the sum of each item in the list into the file
#    --- don't forget to add the newline character to each line 
#    --- example: [[1, 2], [0, 3, 2, 2], [5, 1, 4], [1, 1, 1]]
#    --- the following numbers must be written into the file:
#    --- 3 
#    --- 7
#    --- 10
#    --- 3
#    - return an int (sum of all the numbers)
#    - the output file is called test2_sample_output1.txt
#    - and will be created in same folder as your program.
#    - you can open the output file to check its content.
#
#    - RESTRICTION: None (you may use sum() function)
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               list
#    - return:  integer (sum of all the numbers)
#==========================================================================

def writeSum(filename, lst):
    """Writes the sum of each sublist to a file and returns the total sum."""
    file = open(filename, 'w')
    total_sum = 0

    for sublist in lst:
        sub_sum = sum(sublist)
        file.write(str(sub_sum) + '\n')
        total_sum += sub_sum

    file.close()
    return total_sum


#==============================================================================
# TEST 2 PRACTICE - Test2_2 Practice Problems
# Source file: Test2_2(1).py
#==============================================================================

# PROGRAM PURPOSE:... Practice
# (1 point) AUTHOR:............ Saidniyozov Rustambek
# COURSE:............ CSC 131-001
# TERM:.............. XXX
# YOU MUST NOT CONSULT ANYONE (OTHER THAN YOUR INSTRUCTOR) ON
# ANYTHING ON THIS TEST
#==========================================================================
## Read and follow all instructions carefully
##
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
##
## You may use your editor, help from the shell, your textbooks,
## computer programs previously written by you,
## and the lecture notes as reference.
## No other resources can be used during the test.
## You MAY NOT visit any web site or Google anything
## No additional import statements please
##
## You must include a meaningful docstring with each function
##
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.
#==========================================================================

## NO ADDITIONAL IMPORT STATEMENTS ALLOWED


#==========================================================================
# q1 - create function negativeIntDiff() to meet the conditions below
#    - accept 2 integer parameters
#    - add a docstring
#    - determine the negative integer difference between the values
#       --- Example 1: parameters are -7 and 12; positive difference is -19
#       --- Example 2: parameters are 13 and 9; positive difference is -4
#       --- Example 3: parameters are -2 and -5; positive difference is -3
#    - return the negative difference
#
#    - RESTRICTIONS:  You may NOT use the built-in abs, max or min functions
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  integer
#              integer
#    - return: integer
#==========================================================================

def negativeIntDiff(a, b):
    """Returns the negative difference between two integers."""
    if a > b:
        return b - a
    else:
        return a - b




#==========================================================================
# q2 - create function sumOfSquares() to meet the conditions below
#    - accept one parameter: an integer
#    - calculate the sum of all the squares of integers from 1 up to
#      and including the parameter
#        --- Example 1: 5 -> returns 55, i.e (1+4+9+16+25)
#        --- Example 2: 10 -> returns 385, i.e. (1+4+9+16+25+36+49+64+81+100)
#    - return the sum
#
#    - RESTRICTIONS:  You may NOT use the built-in sum function
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  integer
#    - return: integer
#==========================================================================

def sumOfSquares(n):
    """Returns the sum of squares from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total




#=============================================================================
# q3 - create function numSpaces() to meet the conditions below
#    - accept one parameter:  a string
#    - determine how many spaces are within the string
#       --- Example 1: "Qualified undergraduate students" has 2 spaces
#       --- Example 2: "Qualified undergraduate students " has 3 spaces
#       --- Example 3: " Qualified undergraduate students " has 4 spaces
#       --- Example 4: " Qualified  undergraduate students " has 5 spaces
#    - return the number of spaces in the parameter
#
#    - RESTRICTIONS:  you may NOT use the built-in function count()
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  string
#    - return:  integer
#=============================================================================

def numSpaces(s):
    """Counts and returns the number of spaces."""
    count = 0
    for ch in s:
        if ch == ' ':
            count += 1
    return count




#==========================================================================
# q4 - create function convertToInts() to meet the conditions below
#    - accept a list of strings as a parameter
#    
#    - iterate over the list and convert each value to a integer
#    - You may assume each string contains a value that can be converted
#    - to an int.
#
#    - you MUST change the values within the list and NOT create a new list
#
#       --- Example: ["2","5","23","7","1","12","1"] ->
#                       [2, 5, 23, 7, 1, 12, 1]
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  list (of strings)
#    - return: None
#==========================================================================

def convertToInts(lst):
    """Converts all string values in the list to integers."""
    for i in range(len(lst)):
        lst[i] = int(lst[i])



#==========================================================================
# q5 - create function commonItem() to meet the conditions below
#    - accept two lists of arbitrary values as parameters
#    
#    - returns True if the lists share at least one common member
#       False otherwise
#       --- Example 1: [2,5,4,7,2] and [1,2,1,4,2] -> returns True
#       --- Example 2: ['a','b','c','a'] and ['g','z','f'] -> returns False
#
#    - RESTRICTIONS: You are NOT allowed to use set() function. You also
#       may NOT use the "in" operator with an "if" statement.
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:  list
#              list
#    - return: boolean
#==========================================================================

def commonItem(lst1, lst2):
    """Returns True if the two lists share at least one item."""
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
    return False



#=============================================================================
# q6 - create function countVowels() to meet the conditions below
#    - accept a string as a parameter
#    
#    - iterate over the string and counts the number of vowels
#    - that are in the string. The only vowels you need to count
#    - are a, e, i, o, and u (both uppercase and lowercase).
#    - returns the number of vowels
#       --- Example 1: 
#           string = "A seCRet YoU DidN'T kNOw."
#           return 7
#       --- Example 2: 
#           string = "sEaRcHiNg for A ConNEcTIOn."
#           return 9
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  integer
#=============================================================================

def countVowels(s):
    """Counts and returns the number of vowels."""
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count




#=============================================================================
# q7 - create function readIt() to meet the conditions below
#    - accept one parameter:  a file name
#    - return the sum of the values contained in the textfile and return the
#       result as an integer value
#      NOTE:
#           --- the file is automatically generated when this exam file
#                is run and it is placed in the same directory as this
#                exam file
#           --- The file contains one value per line
#           --- don't forget to close the file
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#    - return:  integer
#=============================================================================

def readIt(filename):
    """Reads numbers from a file and returns their total sum."""
    total = 0
    file = open(filename, 'r')
    for line in file:
        if line.strip() != "":
            total += int(line.strip())
    file.close()
    return total




#==========================================================================
# q8 - create function writeMinMaxSumCount() to meet the conditions below
#    - accept 2 parameters; a str (filename) & a list (arbitrary numbers)
#    
#    - open the filename for writing
#    - iterate over the list and write into the textfile the min, max, sum, 
#        and count of all the numbers in the list
#    --- don't forget to add the newline character to each line 
#       --- example: [1, 2, 0, 3, 2, 2, 5, 1, 4, 1, 1, 1]
#       --- the following numbers must be written into the file:
#           --- 0
#           --- 5
#           --- 23
#           --- 12
#    --- don't forget to close the file
#    - the output file is called test2_sample_output1.txt
#    - and will be created in the same folder as your program.
#    - you can open the output file to check its contents.
#
#    - RESTRICTIONS:  None
#
#      HINT: You may want to use the built-in functions min, max, sum, len
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - params:  string
#               list (of integers)
#    - return:  None
#==========================================================================

def writeMinMaxSumCount(filename, lst):
    """Writes min, max, sum, and count of a list to a file."""
    file = open(filename, 'w')

    file.write(str(min(lst)) + '\n')
    file.write(str(max(lst)) + '\n')
    file.write(str(sum(lst)) + '\n')
    file.write(str(len(lst)) + '\n')

    file.close()



#==========================================================================
# q9 - create function triangle() to meet the conditions below
#    - accept one parameter: an integer
#    
#    - print a triangle using asterisks, as shown below.
#    - you can assume the parameter is greater than 0.
#
#       --- Example 1:  3 is passed to the function it prints to the console:           
#           *
#           **
#           ***
#       --- Example 2: 4 is passed to the function it prints to the console:          
#           *
#           **
#           ***
#           ****
#
#
#    - RESTRICTIONS:  None
#
#    - DOCUMENTATION - Add a meaningful docstring to the function
#
#    - param:   integer
#    - return:  None
#==========================================================================


def triangle(n):
    """Prints a triangle of asterisks with n rows."""
    for i in range(1, n + 1):
        print('*' * i)


#==============================================================================
# TEST 2 PRACTICE - Test2_3 Practice Problems
# Source file: Test2_3(1).py
#==============================================================================

#=============================================================================
# PROGRAM PURPOSE:... practice
# AUTHOR:............ Saidniyozov, Rustambek
# COURSE:............ CSC 131-001
# TERM:.............. XXX
# COLLABORATION:..... None
#=============================================================================


#==========================================================================
# q1 - create function my_max() to meet the conditions below
#    - accept 2 parameters: 2 numeric values
#    - add a docstring
#    - determine the greater of a and b
#    --- e.g. submitted values are 8 and -3.5; max is 8
#    --- e.g. submitted values are -5 and -3; max is -3
#    --- e.g. submitted values are 15 and 150; max is 150
#
#    Restriction: You are not allowed to use built in max() or min() functions!
#
#    - params:  integer
#               integer
#    - return:  integer
#==========================================================================


def my_max(a, b):
    """Returns the larger of two numbers."""
    if a > b:
        return a
    else:
        return b



#==========================================================================
# q2 - create function positiveIntDiff() to meet the conditions below
#    - accept 2 integer parameters of any value
#    - add a docstring
#    - determine the positive integer difference between the values
#    --- e.g. submitted ints are -7 and 12; +diff is 19
#    --- e.g. submitted ints are 13 and 9; +diff is 4
#    --- e.g. submitted ints are -2 and -5; +diff is 3#
#    --- you may assume the user arguments will be integers
#
#    Restriction: You are not allowed to use built in min(), max(),
#                   or abs() functions!
#
#    - params:  integer
#               integer
#    - return:  integer
#==========================================================================

def positiveIntDiff(a, b):
    """Returns the positive difference between two int."""
    if a > b:
        return a - b
    else:
        return b - a





#==========================================================================
# q3 - create function sumPos() to meet the conditions below
#    - accept a list of numeric values
#    - add a docstring
#    - calculate the sum of only the positive values
#    --- e.g. submitted list is [2,9,-5,1]; sum is 12
#    --- e.g. submitted list is [-1,-2,-5]; sum is 0
#    --- e.g. submitted list is [1.5,-4,2.5]; sum is 4
#
#    Restriction: You are not allowed to use built in sum() function!
#
#    - params:  list
#    - return:  numeric value
#==========================================================================

def sumPos(lst):
    """Returns the sum of only positive numbers in a list."""
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total
    



#==========================================================================
# q4 - create function make_list() to meet the conditions below
#    - accept 2 integer parameters of any value
#    - add a docstring
#    - return a list with the values a through b
#    --- e.g. submitted ints are 2 and 5; result is [2,3,4,5]
#    --- e.g. submitted ints are 9 and 13; result is [9,10,11,12,13]
#    --- e.g. submitted ints are -5 and -2; result is [-5,-4,-3,-2]
#    --- you may assume the user arguments will be integers and a<b
#
#    Restriction: You are not allowed to use built in list() function!
#
#    - params:  integer
#               integer
#    - return:  list
#==========================================================================

def make_list(a, b):
    """Creates and returns a list of integers"""
    result = []
    current = a
    while current <= b:
        result.append(current)
        current += 1
    return result





#==========================================================================
# q5 - create function countLetter() to meet the conditions below
#    - accept 2 parameters; a list of words and
#                           a string (a letter)
#    - add a docstring
#    - count the total number of occurrence of the letter in the list
#    --- e.g. submitted list is ['Apple', 'Banana', 'Cherry'], letter is 'a';
#       (counting both upper and lower case letters)
#    --- value return is 4
#
#    Restriction: You are not allowed to use built in count() function!
#
#    - params:  list
#               string
#    - return:  integer
#==========================================================================

def countLetter(words, letter):
    """Counts how many times a letter appears in a list of words."""
    count = 0
    for word in words:
        for ch in word:
            if ch.lower() == letter.lower():
                count += 1
    return count
        




#==========================================================================
# q6 - create function openAndReturnLastN() to meet the conditions below
#    - accept 2 parameters; 1 string (name of a file) and
#                           1 integer (N)
#    - add a docstring
#    - use exception handling techniques to attempt to open the filename
#      provided, if it does not exist, return False
#    - the file will contain an unknown number of lines
#    - store the last N lines of the file in a single string var
#    - return the resultant string var
#    --- ensure to strip the newline character from the lines
#    --- e.g.   textfile:
#    --- e.g.   "line one\n"
#    ---        "line two\n"
#    ---        "line three\n"
#    ---        "line four\n"
#    ---        "line five\n"
#    ---        integer: 2
#    --- e.g. "line four" + "line five" will be
#             "line fourline five"
#
#    - params:  string
#               integer
#    - return:  string
#==========================================================================

def openAndReturnLastN(filename, n):
    """Returns the last n lines of a file combined into one string."""
    try:
        file = open(filename, 'r')
    except:
        return False

    lines = file.readlines()
    file.close()

    result = ""
    for line in lines[-n:]:
        result += line.strip()
    return result
    

    

 


#==========================================================================
# q7 - create function writeMeAFile() to meet the conditions below
#    - accept 2 parameters; a str (filename) & a list (of strings)
#    - add a docstring
#    - open the filename for writing
#    - iterate over the list and write each list element to a line of the file
#    - return an int (count of # of lines you wrote)
#    --- You are not allowed to use built in len() function!
#
#    - params:  string
#               list
#    - return:  integer
#==========================================================================

def writeMeAFile(filename, lst):
    """Writes each string from a list to a file and returns number of lines written."""
    file = open(filename, 'w')
    count = 0

    for item in lst:
        file.write(item + '\n')
        count += 1

    file.close()
    return count


#==============================================================================
# TEST 2 PRACTICE - Test2_4 Practice Problems
# Source file: Test2_4(1).py
#==============================================================================


#==========================================================================
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
## Closed Book, you may use your editor and help from the shell,
## no additional import statements please
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.

# PROGRAM PURPOSE:... practice
# AUTHOR:............ Saidniyozov Rustambek
# COURSE:............ CSC 131-001
# TERM:.............. XXX
# COLLABORATION:..... None
#==========================================================================


#==========================================================================
# q1 - create function letterGrade() to meet the conditions below
#    - accept 1 integer parameter between 0-100
#    - add a meaningful docstring
#    - letterGrade(x) accepts one integer and determines what the corresponding
#    - letter grade is (A: >=90; B: 80-89; C: 70-79; D: 60-69; F: <60).
#    --- e.g. submitted int is 91; return value is letter A
#    --- e.g. submitted int is 89; return value is letter B
#    --- e.g. submitted int is 70; return value is letter C
#    --- e.g. submitted int is 52; return value is letter F
#    - Returns letter grade as string
#
#    - params:  integer
#    - return:  string (a single character)
#==========================================================================

def letterGrade(x):
    """Returns the letter grade for a numeric score."""
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'


#==========================================================================
# q2 - create function isIntDiffOdd() to meet the conditions below
#    - accept 2 integer parameters of any value
#    - add a meaningful docstring
#    - determine if the integer difference between the values is odd number.
#    --- e.g. submitted ints are -7 and 12; diff is -19(odd); returns True
#    --- e.g. submitted ints are 13 and 9; diff is 4(even); returns False
#    --- e.g. submitted ints are -2 and -5; diff is 3(odd); return True
#    --- you may assume the user arguments will be integers
#    - return the result
#
#    - params:  integer
#               integer
#    - return:  boolean
#==========================================================================

def isIntDiffOdd(a, b):
    """Returns True if the difference between two integers is odd."""
    diff = a - b
    return diff % 2 != 0


#==========================================================================
# q3 - create function hasSameNumElements() to meet the conditions below
#    - add a meaningful docstring
#    - accept 2 parameters which are type sequence (tuple, list or string)
#    - return True if two parameters have the same # of elements; False otherwise
#    --- args ('h','i') and [1,2,3]; function returns False
#    --- args [1776,1789] and ('hello','Jo'); function returns True
#    --- args 'boo' and [10, 'four', 2.575]; function returns True
#    - you are not allowed to use len function.
#
#    - params:  a sequence (tuple, list or string)
#               a sequence (tuple, list or string)
#    - return:  boolean
#==========================================================================

def hasSameNumElements(a, b):
    """Returns True if two sequences have the same number of elements."""
    count1 = 0
    count2 = 0

    for _ in a:
        count1 += 1
    for _ in b:
        count2 += 1

    return count1 == count2


        
#==========================================================================
# q4 - create function getUserCharInput() to meet the conditions below
#    - add a meaningful docstring
#    - accept 5 parameters which are type string (alphabet letters, case sensetive)
#    - prompt user to input a letter
#    - if the input does not meet conditions, prompt for input until it does.
#    - the function teminated only if the input is one of the 5 letters that passed to the function
#    - accept the input if it is same as any the five letters (could be any letters in alphabet)
#    --- e.g. params: A, r, e, G, t, prompt for input until user enters
#    --- any of those five letters
#    --- userinputs:
#    - i
#    - k
#    - e -> valid input; return e
#    - return the valid userinput
#
#    - params:  string
#               string
#               string
#               string
#               string
#    - return:  string
#==========================================================================

def getUserCharInput(a, b, c, d, e):
    """Prompts user until they enter one of the allowed characters."""
    valid = [a, b, c, d, e]

    while True:
        user = input("Enter a character: ")
        if user in valid:
            return user



#==========================================================================
# q5 - create function backward() to meet the conditions below
#    - accept one string parameter of any value
#    - add a meaningful docstring
#    - returns the backward string,
#    --- e.g. submitted value is diaper; result repaid
#    --- e.g. submitted value is desserts; result stressed
#    --- e.g. submitted value is god; result dog
#
#    Restriction: you are NOT allowed to use reverse() function or string slicing
#    Hint: you can use the range() combined with len() function to go backward 
#    - return the reversed string
#
#    - params:  string
#    - return:  string
#==========================================================================

def backward(s):
    """Returns the reversed string."""
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result




#==========================================================================
# q6 - create function print2DListContent() to meet the conditions below
#    - accepts a list: the list is a 2-D list of arbitrary content
#    - add a meaningful docstring
#    - prints each stored value on a different line.
#    - example:
#    --- list2D = [['red','square','one'], ['yellow','triangle'], ['circle', 'blue']]
#    --- displays:
    # red
    # square
    # one
    # yellow
    # triangle
    # circle
    # blue
#   Hint: You need nested loops
#    - return: None (instructor will check the output)
#
#    - params:  list
#    - return:  None
#==========================================================================


def print2DListContent(lst):
    """Prints each element of a 2D list on its own line."""
    for sub in lst:
        for item in sub:
            print(item)
       

#==========================================================================
# q7 - create function createPlates() to meet the conditions below
#    - Accepts a list of 3-letter strings, and a list of 4-digit strings
#    - add a docstring
#    - returns a new list representing all possible combinations of EACH
#    - 3-letter string and EACH 4-digit numbers with a dash ('-') in between
#    --- Example 1: create_plates(["ZQQ", "AEE"], [1234, 4567])
#    --- returns the list ["ZQQ-1234","ZQQ-4567","AEE-1234","AEE-4567"]
#    --- Example 2: create_plates(["ZQQ", "BRP", "AEE"], [1234, 4567])
#    --- final list:
#    --- ["ZQQ-1234","ZQQ-4567","BRP-1234", "BRP-4567","AEE-1234","AEE-4567"]
#    - Hint: you need nested loops,
#            string concatination, and
#            int() to str() conversion
#    - Note: use sorted() function when you return the final list
#
#    - params:  list
#               list
#    - return:  sorted(list)
#==========================================================================

def createPlates(letters, numbers):
    """Creates sorted license plate combinations."""
    result = []

    for l in letters:
        for n in numbers:
            result.append(l + "-" + str(n))

    return sorted(result)



#==========================================================================
# q8 - create function openAndReturnMiddle() to meet the conditions below
#    - accept 1 string parameter; the name of a file
#    - add a meaningful docstring
#    - use exception handling techniques to attempt to open the filename
#      provided, if it does not exist, return False
#    - the file will contain an unknown odd number of lines
#    - store the middle line of the file in a single string var
#    --- ensure to strip the newline character from the line
#    --- e.g.
#    - first line
#    - second line
#    - third line
#    --- returns -> second line
#    - you may assume there are odd number of lines in the file
#    - return the resultant string var
#
#    - params:  string
#    - return:  string
#==========================================================================


def openAndReturnMiddle(filename):
    """Returns the middle line of a file or False if file not found."""
    try:
        file = open(filename, 'r')
    except:
        return False

    lines = file.readlines()
    file.close()

    mid = len(lines) // 2
    return lines[mid].strip()

        


#==========================================================================
# q9 - create function writeSum() to meet the conditions below
#    - accept 2 parameters; a str (filename) & a 2-D list (arbitrary numbers)
#    - add a meaningful docstring
#    - open the filename for writing
#    - iterate over the list and write the sum of each item in the list into the file
#    --- don't forget to add the newline character to each line 
#    --- example: [[1, 2], [0, 3, 2, 2], [5, 1, 4], [1, 1, 1]]
#    --- the following numbers must be written into the file:
#    --- 3 
#    --- 7
#    --- 10
#    --- 3
#    - return an int (sum of all the numbers in the 2-D list)
#    - you are not allowed to use len functions
#    - the output file is called test2_sample_output1.txt
#    - and will be created in same folder as your program.
#    - you can open the output file to check its content.
#
#    - params:  string
#               list
#    - return:  integer
#==========================================================================

def writeSum(filename, lst):
    """Writes sum of each sublist to file and returns total sum."""
    file = open(filename, 'w')
    total = 0

    for sub in lst:
        sub_sum = 0
        for num in sub:
            sub_sum += num
        file.write(str(sub_sum) + '\n')
        total += sub_sum

    file.close()
    return total

