#=============================================================================
# PROGRAM PURPOSE:............. MOCK TEST 2, 11 QUESTIONS, ANSWER KEY
# AUTHOR:...................... Practice Solution
# COURSE:...................... CSC 131
# TERM:........................ Practice
#=============================================================================


#=============================================================================
# q1 - validStudentCode()
#=============================================================================

def validStudentCode(s):
    """Returns True if the student code meets all required rules."""

    if len(s) < 6 or len(s) > 10:
        return False

    if not s[0].isalpha():
        return False

    if not s[len(s) - 1].isdigit():
        return False

    has_upper = False
    has_lower = False

    for ch in s:
        if ch == " ":
            return False
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True

    return has_upper and has_lower


#=============================================================================
# q2 - sumEveryThirdOdd()
#=============================================================================

def sumEveryThirdOdd(numbers):
    """Returns the sum of odd values at indexes 2, 5, 8, and so on."""

    total = 0

    for i in range(2, len(numbers), 3):
        if numbers[i] % 2 != 0:
            total += numbers[i]

    return total


#=============================================================================
# q3 - matchingIndexProducts()
#=============================================================================

def matchingIndexProducts(list1, list2):
    """Returns products of numbers at matching indexes from two lists."""

    result = []

    for i in range(len(list1)):
        result.append(list1[i] * list2[i])

    return result


#=============================================================================
# q4 - buildColumnWords()
#=============================================================================

def buildColumnWords(tuple_list):
    """Returns words made from matching indexes in a list of tuples."""

    result = []

    for col in range(len(tuple_list[0])):
        word = ""

        for row in range(len(tuple_list)):
            word += tuple_list[row][col]

        result.append(word)

    return result


#=============================================================================
# q5 - countCleanWords()
#=============================================================================

def countCleanWords(sentence):
    """Returns a dictionary of cleaned word frequencies."""

    special = "#!@#$%^&*()-_=+|{};:/?.>"
    words = sentence.split()
    result = {}

    for word in words:
        clean_word = ""

        for ch in word:
            if ch not in special:
                clean_word += ch

        if clean_word in result:
            result[clean_word] += 1
        else:
            result[clean_word] = 1

    return result


#=============================================================================
# q6 - tupleRangeDiffs()
#=============================================================================

def tupleRangeDiffs(tuple_list):
    """Returns positive differences between two numbers inside each tuple."""

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
# q7 - readSafeAverage()
#=============================================================================

def readSafeAverage(filename):
    """Returns the average of integers in a file or None if the file is missing."""

    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    total = 0
    count = 0

    for line in infile:
        total += int(line.strip())
        count += 1

    infile.close()

    return total / count


#=============================================================================
# q8 - writeNumberReport()
#=============================================================================

def writeNumberReport(filename, numbers):
    """Writes min, max, sum, and count to a file without built-in shortcuts."""

    smallest = numbers[0]
    largest = numbers[0]
    total = 0
    count = 0

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

        total += number
        count += 1

    outfile = open(filename, "w")
    outfile.write(str(smallest) + "\n")
    outfile.write(str(largest) + "\n")
    outfile.write(str(total) + "\n")
    outfile.write(str(count) + "\n")
    outfile.close()


#=============================================================================
# q9 - diagonalSentence()
#=============================================================================

def diagonalSentence(words):
    """Returns a string made from diagonal characters in a list of strings."""

    result = ""

    for i in range(len(words)):
        result += words[i][i]

    return result


#=============================================================================
# q10 - translateCodes()
#=============================================================================

def translateCodes(dictionary, codes):
    """Translates tuple codes into one space-separated string."""

    result = ""

    for i in range(len(codes)):
        result += dictionary[codes[i]]

        if i != len(codes) - 1:
            result += " "

    return result


#=============================================================================
# q11 - sortedAndUniqueLetters()
#=============================================================================

def sortedAndUniqueLetters(s):
    """Returns True if letters are unique and alphabetically sorted."""

    letters = ""

    for ch in s:
        if ch.isalpha():
            letters += ch.lower()

    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[i] == letters[j]:
                return False

    for i in range(len(letters) - 1):
        if letters[i] > letters[i + 1]:
            return False

    return True


#=============================================================================
# QUICK SELF-TESTS
#=============================================================================

def main():
    """Runs quick self-tests for the mock test answer key."""

    print(validStudentCode("Abc123"))  # True
    print(sumEveryThirdOdd([1, 2, 3, 4, 5, 7, 8, 9, 11]))  # 21
    print(matchingIndexProducts([2, 3, 4], [10, 20, 30]))  # [20, 60, 120]
    print(buildColumnWords([('c', 'd', 'p'), ('a', 'o', 'e'), ('t', 'g', 't')]))  # ['cat', 'dog', 'pet']
    print(countCleanWords("cat dog! cat bird? dog"))  # {'cat': 2, 'dog': 2, 'bird': 1}
    print(tupleRangeDiffs([(4, 9), (10, -2), (3, 3)]))  # [5, 12, 0]
    print(diagonalSentence(["cat", "boat", "hello", "yellow"]))  # coll
    print(translateCodes({"1": "I", "2": "love", "3": "Python"}, ("1", "2", "3")))  # I love Python
    print(sortedAndUniqueLetters("a b c 123"))  # True


if __name__ == "__main__":
    main()
