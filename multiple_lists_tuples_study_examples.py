#=============================================================================
# PROGRAM PURPOSE:
# This file is a study guide for problems that use multiple lists, tuples,
# numbers, letters, matching indexes, every second item, and nested collections.
#
# These are common CSC 131 test patterns:
# - Add numbers from matching positions
# - Add every second number
# - Compare matching indexes
# - Join letters from tuples/lists to make words
# - Build words from columns
# - Work with lists of tuples
# - Work with lists of lists
# - Return lists, tuples, strings, or numbers
#=============================================================================


#=============================================================================
# 1. SUM MATCHING INDEXES FROM TWO LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes two lists of numbers that have the same length.
# It adds the numbers in matching positions and returns a new list.
#
# Example:
# [1, 2, 3] and [10, 20, 30]
# returns [11, 22, 33]

def sumMatchingIndexes(list1, list2):
    """Returns a list containing the sum of values at matching indexes."""

    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result


#=============================================================================
# 2. SUM MATCHING INDEXES FROM THREE LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes three lists of numbers that have the same length.
# It adds the numbers in matching positions and returns a new list.
#
# Example:
# [1, 2, 3], [10, 20, 30], [100, 200, 300]
# returns [111, 222, 333]

def sumThreeMatchingIndexes(list1, list2, list3):
    """Returns a list containing the sum of values at matching indexes from three lists."""

    result = []

    for i in range(len(list1)):
        total = list1[i] + list2[i] + list3[i]
        result.append(total)

    return result


#=============================================================================
# 3. SUM MATCHING INDEXES FROM A LIST OF LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of lists where all inside lists are the same length.
# It adds the values by column/matching index and returns a new list.
#
# Example:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# returns [12, 15, 18]

def sumColumns(list_of_lists):
    """Returns a list of sums from matching indexes in a list of lists."""

    result = []

    for col in range(len(list_of_lists[0])):
        total = 0

        for row in range(len(list_of_lists)):
            total += list_of_lists[row][col]

        result.append(total)

    return result


#=============================================================================
# 4. SUM EVERY SECOND NUMBER FROM A LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program adds every second value in a list.
# In this example, every second value means indexes 1, 3, 5, 7, and so on.
#
# Example:
# [10, 20, 30, 40, 50, 60]
# returns 120 because 20 + 40 + 60 = 120

def sumEverySecondNumber(numbers):
    """Returns the sum of every second number in a list."""

    total = 0

    for i in range(1, len(numbers), 2):
        total += numbers[i]

    return total


#=============================================================================
# 5. SUM EVERY SECOND NUMBER FROM A TUPLE
#=============================================================================
# PROGRAM PURPOSE:
# This program adds every second value in a tuple.
# In this example, every second value means indexes 1, 3, 5, 7, and so on.
#
# Example:
# (5, 10, 15, 20, 25)
# returns 30 because 10 + 20 = 30

def sumEverySecondNumberTuple(numbers):
    """Returns the sum of every second number in a tuple."""

    total = 0

    for i in range(1, len(numbers), 2):
        total += numbers[i]

    return total


#=============================================================================
# 6. SUM EVERY EVEN INDEX FROM A LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program adds values stored at even indexes.
# Even indexes are 0, 2, 4, 6, and so on.
#
# Example:
# [10, 20, 30, 40, 50]
# returns 90 because index 0 + index 2 + index 4 = 10 + 30 + 50

def sumEvenIndexes(numbers):
    """Returns the sum of values stored at even indexes."""

    total = 0

    for i in range(0, len(numbers), 2):
        total += numbers[i]

    return total


#=============================================================================
# 7. SUM EVERY ODD INDEX FROM A LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program adds values stored at odd indexes.
# Odd indexes are 1, 3, 5, 7, and so on.
#
# Example:
# [10, 20, 30, 40, 50]
# returns 60 because index 1 + index 3 = 20 + 40

def sumOddIndexes(numbers):
    """Returns the sum of values stored at odd indexes."""

    total = 0

    for i in range(1, len(numbers), 2):
        total += numbers[i]

    return total


#=============================================================================
# 8. SUM ONLY MATCHING NUMBERS FROM TWO LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program compares two lists at the same indexes.
# If the numbers match, it adds that number to the total.
#
# Example:
# [1, 2, 3, 4] and [1, 9, 3, 8]
# returns 4 because 1 and 3 match in the same positions.

def sumMatchingNumbersOnly(list1, list2):
    """Returns the sum of numbers that match at the same indexes."""

    total = 0

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            total += list1[i]

    return total


#=============================================================================
# 9. RETURN MATCHING NUMBERS FROM TWO LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program compares two lists at the same indexes.
# If the numbers match, it adds that number to a new list.
#
# Example:
# [1, 2, 3, 4] and [1, 9, 3, 8]
# returns [1, 3]

def returnMatchingNumbers(list1, list2):
    """Returns a list of numbers that match at the same indexes."""

    result = []

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            result.append(list1[i])

    return result


#=============================================================================
# 10. RETURN DIFFERENCES FROM MATCHING INDEXES
#=============================================================================
# PROGRAM PURPOSE:
# This program takes two lists of numbers that have the same length.
# It subtracts the second list value from the first list value at each index.
#
# Example:
# [10, 20, 30] and [1, 2, 3]
# returns [9, 18, 27]

def subtractMatchingIndexes(list1, list2):
    """Returns a list of differences from matching indexes."""

    result = []

    for i in range(len(list1)):
        result.append(list1[i] - list2[i])

    return result


#=============================================================================
# 11. FIND BIGGER NUMBER AT EACH MATCHING INDEX
#=============================================================================
# PROGRAM PURPOSE:
# This program compares two lists of numbers at matching indexes.
# It returns a new list with the bigger number from each position.
#
# Example:
# [1, 20, 3] and [10, 2, 30]
# returns [10, 20, 30]

def biggerAtEachIndex(list1, list2):
    """Returns the bigger value from each matching index."""

    result = []

    for i in range(len(list1)):
        if list1[i] > list2[i]:
            result.append(list1[i])
        else:
            result.append(list2[i])

    return result


#=============================================================================
# 12. COUNT MATCHING INDEXES FROM TWO LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program counts how many times two lists have the same value
# at the same index.
#
# Example:
# [1, 2, 3, 4] and [1, 9, 3, 8]
# returns 2 because indexes 0 and 2 match.

def countMatchingIndexes(list1, list2):
    """Counts how many matching indexes have the same value."""

    count = 0

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1

    return count


#=============================================================================
# 13. JOIN MATCHING INDEX LETTERS FROM TWO LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes two lists of letters with the same length.
# It joins the matching index letters together and returns a list of strings.
#
# Example:
# ["c", "d", "p"] and ["a", "o", "e"]
# returns ["ca", "do", "pe"]

def joinMatchingLetters(list1, list2):
    """Returns a list of combined letters from matching indexes."""

    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result


#=============================================================================
# 14. MAKE WORDS FROM COLUMNS IN A LIST OF LISTS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of lists of letters.
# It joins letters by matching indexes/columns to create words.
#
# Example:
# [["c", "d", "p"], ["a", "o", "e"], ["t", "g", "t"]]
# returns ["cat", "dog", "pet"]

def makeWordsFromColumns(letter_lists):
    """Returns words created by joining letters from each column."""

    result = []

    for col in range(len(letter_lists[0])):
        word = ""

        for row in range(len(letter_lists)):
            word += letter_lists[row][col]

        result.append(word)

    return result


#=============================================================================
# 15. MAKE ONE WORD FROM A LIST OF TUPLES USING FIRST LETTERS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples.
# It joins the first item from each tuple to create one word.
#
# Example:
# [("c", "x"), ("a", "y"), ("t", "z")]
# returns "cat"

def makeWordFromFirstLetters(tuple_list):
    """Returns one word made from the first item of each tuple."""

    word = ""

    for item in tuple_list:
        word += item[0]

    return word


#=============================================================================
# 16. MAKE ONE WORD FROM A LIST OF TUPLES USING SECOND LETTERS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples.
# It joins the second item from each tuple to create one word.
#
# Example:
# [("x", "d"), ("y", "o"), ("z", "g")]
# returns "dog"

def makeWordFromSecondLetters(tuple_list):
    """Returns one word made from the second item of each tuple."""

    word = ""

    for item in tuple_list:
        word += item[1]

    return word


#=============================================================================
# 17. MAKE WORDS FROM TUPLES BY INDEX
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples where all tuples are the same length.
# It joins matching indexes from the tuples to create words.
#
# Example:
# [("c", "d", "p"), ("a", "o", "e"), ("t", "g", "t")]
# returns ["cat", "dog", "pet"]

def makeWordsFromTupleColumns(tuple_list):
    """Returns words created by joining matching indexes from tuples."""

    result = []

    for col in range(len(tuple_list[0])):
        word = ""

        for row in range(len(tuple_list)):
            word += tuple_list[row][col]

        result.append(word)

    return result


#=============================================================================
# 18. MAKE A SENTENCE FROM A LIST OF TUPLES
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples.
# It joins the first item from each tuple into a sentence.
#
# Example:
# [("I", 1), ("love", 2), ("Python", 3)]
# returns "I love Python"

def makeSentenceFromFirstItems(tuple_list):
    """Returns a sentence made from the first item in each tuple."""

    sentence = ""

    for i in range(len(tuple_list)):
        sentence += tuple_list[i][0]

        if i != len(tuple_list) - 1:
            sentence += " "

    return sentence


#=============================================================================
# 19. MAKE A SENTENCE FROM SECOND ITEMS IN TUPLES
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples.
# It joins the second item from each tuple into a sentence.
#
# Example:
# [(1, "Python"), (2, "is"), (3, "fun")]
# returns "Python is fun"

def makeSentenceFromSecondItems(tuple_list):
    """Returns a sentence made from the second item in each tuple."""

    sentence = ""

    for i in range(len(tuple_list)):
        sentence += tuple_list[i][1]

        if i != len(tuple_list) - 1:
            sentence += " "

    return sentence


#=============================================================================
# 20. CREATE A WORD USING DIAGONAL LETTERS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of strings.
# It takes index 0 from the first string, index 1 from the second string,
# index 2 from the third string, and so on.
#
# Example:
# ["case", "poor", "from", "yellow"]
# returns "cool" because:
# case[0] = c
# poor[1] = o
# from[2] = o
# yellow[3] = l

def createWordDiagonal(words):
    """Returns a word made from diagonal letters in a list of strings."""

    result = ""

    for i in range(len(words)):
        result += words[i][i]

    return result


#=============================================================================
# 21. CREATE WORDS FROM FIRST, SECOND, AND THIRD LETTERS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of 3-letter strings.
# It creates three words:
# - one from all first letters
# - one from all second letters
# - one from all third letters
#
# Example:
# ["cat", "dog", "pen"]
# returns ["cdp", "aoe", "tgn"]

def createWordsByLetterPosition(words):
    """Returns words made from each letter position in same-length words."""

    result = []

    for col in range(len(words[0])):
        new_word = ""

        for row in range(len(words)):
            new_word += words[row][col]

        result.append(new_word)

    return result


#=============================================================================
# 22. ADD NUMBERS INSIDE EACH TUPLE
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of number tuples.
# It adds the numbers inside each tuple and returns a list of totals.
#
# Example:
# [(1, 2), (10, 20), (5, 5)]
# returns [3, 30, 10]

def sumEachTuple(tuple_list):
    """Returns a list containing the sum of each tuple."""

    result = []

    for pair in tuple_list:
        total = 0

        for number in pair:
            total += number

        result.append(total)

    return result


#=============================================================================
# 23. FIND DIFFERENCE INSIDE EACH TUPLE
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples with two numbers each.
# It subtracts the smaller number from the bigger number manually.
#
# Example:
# [(4, 6), (10, -2), (0, -5)]
# returns [2, 12, 5]

def differenceEachTuple(tuple_list):
    """Returns the positive difference between the two numbers in each tuple."""

    result = []

    for pair in tuple_list:
        a = pair[0]
        b = pair[1]

        if a > b:
            result.append(a - b)
        else:
            result.append(b - a)

    return result


#=============================================================================
# 24. SUM FIRST NUMBER FROM EACH TUPLE
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples.
# It adds only the first number from each tuple.
#
# Example:
# [(1, 100), (2, 200), (3, 300)]
# returns 6

def sumFirstNumbers(tuple_list):
    """Returns the sum of the first number from each tuple."""

    total = 0

    for pair in tuple_list:
        total += pair[0]

    return total


#=============================================================================
# 25. SUM SECOND NUMBER FROM EACH TUPLE
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples.
# It adds only the second number from each tuple.
#
# Example:
# [(1, 100), (2, 200), (3, 300)]
# returns 600

def sumSecondNumbers(tuple_list):
    """Returns the sum of the second number from each tuple."""

    total = 0

    for pair in tuple_list:
        total += pair[1]

    return total


#=============================================================================
# 26. RETURN TUPLES WHERE FIRST NUMBER MATCHES TARGET
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples and a target number.
# It returns only tuples where the first number matches the target.
#
# Example:
# [(1, "a"), (2, "b"), (1, "c")] and target 1
# returns [(1, "a"), (1, "c")]

def tuplesWithFirstMatching(tuple_list, target):
    """Returns tuples where the first item matches the target."""

    result = []

    for item in tuple_list:
        if item[0] == target:
            result.append(item)

    return result


#=============================================================================
# 27. RETURN TUPLES WHERE SECOND ITEM MATCHES TARGET
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of tuples and a target value.
# It returns only tuples where the second item matches the target.
#
# Example:
# [("a", 1), ("b", 2), ("c", 1)] and target 1
# returns [("a", 1), ("c", 1)]

def tuplesWithSecondMatching(tuple_list, target):
    """Returns tuples where the second item matches the target."""

    result = []

    for item in tuple_list:
        if item[1] == target:
            result.append(item)

    return result


#=============================================================================
# 28. COUNT HOW MANY TUPLES HAVE A MATCHING VALUE
#=============================================================================
# PROGRAM PURPOSE:
# This program counts how many tuples contain the target value anywhere
# inside the tuple.
#
# Example:
# [(1, 2), (3, 4), (2, 5)] and target 2
# returns 2

def countTuplesWithValue(tuple_list, target):
    """Counts how many tuples contain the target value."""

    count = 0

    for item in tuple_list:
        for value in item:
            if value == target:
                count += 1
                break

    return count


#=============================================================================
# 29. FIND PAIRS FROM TWO LISTS THAT ADD TO TARGET
#=============================================================================
# PROGRAM PURPOSE:
# This program checks every number from list1 with every number from list2.
# It counts how many pairs add up to the target.
#
# Example:
# [2, 5, 4, 7, 2], [1, 2, 1, 4, 2], target 8
# returns 3 because (4,4), (7,1), and (7,1)

def countPairsFromTwoLists(list1, list2, target):
    """Counts pairs from two lists that add up to the target."""

    count = 0

    for num1 in list1:
        for num2 in list2:
            if num1 + num2 == target:
                count += 1

    return count


#=============================================================================
# 30. FIND PAIRS FROM ONE LIST THAT ADD TO TARGET
#=============================================================================
# PROGRAM PURPOSE:
# This program checks pairs from one list.
# It counts each pair only once.
#
# Example:
# [2, 3, 4, 5], target 7
# returns 2 because (2,5) and (3,4)

def countPairsFromOneList(numbers, target):
    """Counts unique pairs from one list that add up to the target."""

    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1

    return count


#=============================================================================
# 31. COMBINE ITEMS FROM TWO LISTS INTO STRINGS
#=============================================================================
# PROGRAM PURPOSE:
# This program combines each item from list1 with each item from list2.
#
# Example:
# ["Sam", "Jim"] and ["Smith", "Jones"]
# returns ["Sam Smith", "Sam Jones", "Jim Smith", "Jim Jones"]

def combineEveryItem(list1, list2):
    """Returns all combinations of items from two lists."""

    result = []

    for item1 in list1:
        for item2 in list2:
            result.append(str(item1) + " " + str(item2))

    return result


#=============================================================================
# 32. COMBINE ITEMS FROM THREE LISTS INTO STRINGS
#=============================================================================
# PROGRAM PURPOSE:
# This program combines each item from three lists.
#
# Example:
# ["apple"], ["carrot", "pea"], ["water"]
# returns ["apple, carrot and water", "apple, pea and water"]

def combineThreeLists(list1, list2, list3):
    """Returns all combinations from three lists as strings."""

    result = []

    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                result.append(str(item1) + ", " + str(item2) + " and " + str(item3))

    return result


#=============================================================================
# 33. MERGE TWO SAME-LENGTH LISTS INTO A LIST OF TUPLES
#=============================================================================
# PROGRAM PURPOSE:
# This program takes two same-length lists.
# It pairs matching indexes into tuples.
#
# Example:
# ["a", "b", "c"] and [1, 2, 3]
# returns [("a", 1), ("b", 2), ("c", 3)]

def mergeListsIntoTuples(list1, list2):
    """Returns a list of tuples made from matching indexes."""

    result = []

    for i in range(len(list1)):
        result.append((list1[i], list2[i]))

    return result


#=============================================================================
# 34. MERGE TWO SAME-LENGTH LISTS INTO A DICTIONARY
#=============================================================================
# PROGRAM PURPOSE:
# This program takes two same-length lists.
# It uses list1 as keys and list2 as values.
#
# Example:
# ["a", "b", "c"] and [1, 2, 3]
# returns {"a": 1, "b": 2, "c": 3}

def mergeListsIntoDictionary(keys, values):
    """Returns a dictionary made from matching indexes of two lists."""

    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result


#=============================================================================
# 35. RETURN ITEMS THAT ARE IN THE SAME POSITION AND SAME TYPE
#=============================================================================
# PROGRAM PURPOSE:
# This program compares two lists at the same indexes.
# If both items are equal, they are added to the result.
#
# Example:
# ["a", 2, "c"] and ["a", 5, "c"]
# returns ["a", "c"]

def samePositionSameValue(list1, list2):
    """Returns items that are equal at matching indexes."""

    result = []

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            result.append(list1[i])

    return result


#=============================================================================
# 36. RETURN ONLY NUMBERS FROM A MIXED LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a mixed list.
# It returns only integer and float values.
#
# Example:
# [1, "a", 2.5, "hello", 3]
# returns [1, 2.5, 3]

def returnOnlyNumbers(items):
    """Returns only the numeric items from a mixed list."""

    result = []

    for item in items:
        if type(item) == int or type(item) == float:
            result.append(item)

    return result


#=============================================================================
# 37. RETURN ONLY LETTER STRINGS FROM A MIXED LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a mixed list.
# It returns only strings that contain alphabet letters only.
#
# Example:
# [1, "abc", "123", "hi", 5]
# returns ["abc", "hi"]

def returnOnlyLetterStrings(items):
    """Returns only strings that contain alphabet letters."""

    result = []

    for item in items:
        if type(item) == str and item.isalpha():
            result.append(item)

    return result


#=============================================================================
# 38. JOIN ONLY LETTER STRINGS FROM A MIXED LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a mixed list.
# It joins only the letter strings into one word.
#
# Example:
# ["h", 1, "e", 2, "l", "l", "o"]
# returns "hello"

def joinOnlyLetters(items):
    """Returns one string made from only the letter-string items."""

    result = ""

    for item in items:
        if type(item) == str and item.isalpha():
            result += item

    return result


#=============================================================================
# 39. SUM ONLY NUMBERS FROM A MIXED LIST
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a mixed list.
# It adds only integers and floats.
#
# Example:
# [1, "a", 2.5, "hello", 3]
# returns 6.5

def sumOnlyNumbers(items):
    """Returns the sum of only numeric items from a mixed list."""

    total = 0

    for item in items:
        if type(item) == int or type(item) == float:
            total += item

    return total


#=============================================================================
# 40. MAKE WORD FROM FIRST LETTER OF EACH WORD
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of words.
# It joins the first letter from each word into a new word.
#
# Example:
# ["cat", "apple", "tree"]
# returns "cat"

def firstLetterWord(words):
    """Returns a word made from the first letter of each word."""

    result = ""

    for word in words:
        result += word[0]

    return result


#=============================================================================
# 41. MAKE WORD FROM LAST LETTER OF EACH WORD
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of words.
# It joins the last letter from each word into a new word.
#
# Example:
# ["basic", "zebra", "goat"]
# returns "cat"

def lastLetterWord(words):
    """Returns a word made from the last letter of each word."""

    result = ""

    for word in words:
        result += word[len(word) - 1]

    return result


#=============================================================================
# 42. MAKE WORD FROM EVERY SECOND WORD'S FIRST LETTER
#=============================================================================
# PROGRAM PURPOSE:
# This program takes every second word from a list and joins its first letter.
# Every second word here means indexes 1, 3, 5, and so on.
#
# Example:
# ["xray", "cat", "yellow", "apple", "zero", "tree"]
# returns "cat"

def firstLetterEverySecondWord(words):
    """Returns a word from first letters of every second word."""

    result = ""

    for i in range(1, len(words), 2):
        result += words[i][0]

    return result


#=============================================================================
# 43. MAKE WORD FROM EVEN-INDEX WORDS
#=============================================================================
# PROGRAM PURPOSE:
# This program takes words at even indexes and joins their first letters.
# Even indexes are 0, 2, 4, and so on.
#
# Example:
# ["cat", "xray", "apple", "yellow", "tree"]
# returns "cat"

def firstLetterEvenIndexWords(words):
    """Returns a word from first letters of even-index words."""

    result = ""

    for i in range(0, len(words), 2):
        result += words[i][0]

    return result


#=============================================================================
# 44. QUICK PATTERN: SAME INDEX LOOP
#=============================================================================
# PROGRAM PURPOSE:
# Use this pattern when two lists/tuples are the same length and you need to
# compare, add, subtract, or combine matching positions.

def sameIndexPattern(list1, list2):
    """Shows the same-index loop pattern."""

    result = []

    for i in range(len(list1)):
        result.append((list1[i], list2[i]))

    return result


#=============================================================================
# 45. QUICK PATTERN: LIST OF LISTS COLUMN LOOP
#=============================================================================
# PROGRAM PURPOSE:
# Use this pattern when you have a list of lists and need to work by columns.

def columnPattern(list_of_lists):
    """Shows the column loop pattern for a list of lists."""

    result = []

    for col in range(len(list_of_lists[0])):
        column_items = []

        for row in range(len(list_of_lists)):
            column_items.append(list_of_lists[row][col])

        result.append(column_items)

    return result


#=============================================================================
# 46. QUICK PATTERN: LIST OF TUPLES LOOP
#=============================================================================
# PROGRAM PURPOSE:
# Use this pattern when you have a list of tuples and need to use tuple items.

def tuplePattern(tuple_list):
    """Shows the loop pattern for a list of tuples."""

    result = []

    for item in tuple_list:
        first = item[0]
        second = item[1]
        result.append((first, second))

    return result


#=============================================================================
# SAMPLE MAIN FOR TESTING ONLY
#=============================================================================
# You can delete or comment out main() if your teacher only wants functions.

def main():
    """Runs small examples from this file."""

    print(sumMatchingIndexes([1, 2, 3], [10, 20, 30]))
    print(sumColumns([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(makeWordsFromColumns([["c", "d", "p"], ["a", "o", "e"], ["t", "g", "t"]]))
    print(makeWordFromFirstLetters([("c", "x"), ("a", "y"), ("t", "z")]))
    print(createWordDiagonal(["case", "poor", "from", "yellow"]))


if __name__ == "__main__":
    main()
