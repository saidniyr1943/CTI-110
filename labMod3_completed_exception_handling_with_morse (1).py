
#=============================================================================
# PROGRAM PURPOSE:... Lab XX
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-00X
# TERM:.............. XXX
# COLLABORATION:..... None
#=============================================================================

import random
from testing_Mod3 import test,test_file_content,test_LOM,testNoPrint
import sys

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
    """Reads the first line of a file and counts a specific character, returning None if the file is not found."""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    line = infile.readline().strip()
    infile.close()

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
    """Reads all lines of a file and counts a specific character, returning None if the file is not found."""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    count = 0
    for line in infile:
        line = line.strip()
        for c in line:
            if c == ch:
                count += 1

    infile.close()
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
    """Calculates the sum of all numbers in a file, returning None if the file is not found."""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    total = 0
    for line in infile:
        total += int(line.strip())

    infile.close()
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
    """Writes the sum of all numbers from one file into another file, returning None if the input file is not found."""
    try:
        infile = open(filename1, "r")
    except FileNotFoundError:
        return None

    total = 0
    for line in infile:
        total += int(line.strip())

    infile.close()

    outfile = open(filename2, "w")
    outfile.write(str(total))
    outfile.close()



#=============================================================================
# q6 - create function buildMorseDictionary() to meet the conditions below
#    - accept no parameters
#    - add a meaningful docstring
#    - create your own dictionary that translates English letters and numbers
#      into Morse code
#    - return the dictionary
#
#    - params:  none
#    - return:  dictionary
#=============================================================================


def buildMorseDictionary():
    """Returns a dictionary that maps English letters and numbers to Morse code."""
    morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
        "9": "----."
    }

    return morse


#=============================================================================
# q7 - create function englishToMorse() to meet the conditions below
#    - accept one parameter: a string containing English text
#    - add a meaningful docstring
#    - use your own Morse dictionary to translate English into Morse code
#    - ignore punctuation or symbols that are not in the Morse dictionary
#    - put one space between Morse letters
#    - put a slash / between words
#    - return the Morse code string
#
#    Example:
#    englishToMorse("hello world") returns
#    ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
#
#    - params:  string
#    - return:  string
#=============================================================================


def englishToMorse(text):
    """Translates English text into Morse code using a dictionary."""
    morse = buildMorseDictionary()
    result = ""
    words = text.split()

    for word_index in range(len(words)):
        word = words[word_index]

        for ch_index in range(len(word)):
            ch = word[ch_index].upper()

            if ch in morse:
                if result != "" and result[-1] != "/":
                    result += " "
                result += morse[ch]

        if word_index != len(words) - 1:
            result += " /"

    return result


#=============================================================================
# q8 - create function writeMorseTranslation() to meet the conditions below
#    - accept two parameters: a filename and English text
#    - add a meaningful docstring
#    - translate the English text into Morse code using your own dictionary
#    - write the original English text and Morse translation into the file
#    - if the English text is one string, write it as one translation
#    - if the English text is a list of strings, write each item in a numbered
#      column format
#    - use a comma between the original English text and the Morse translation
#    - close the file
#    - return None
#
#    Example with one string:
#    hello, .... . .-.. .-.. ---
#
#    Example with a list:
#    1. hello, .... . .-.. .-.. ---
#    2. world, .-- --- .-. .-.. -..
#
#    - params:  string
#               string or list
#    - return:  None
#=============================================================================


def writeMorseTranslation(filename, english_text):
    """Writes English-to-Morse translations to a file in comma-separated, numbered format for lists."""
    outfile = open(filename, "w")

    if type(english_text) == list:
        line_number = 1

        for item in english_text:
            morse_text = englishToMorse(item)
            outfile.write(str(line_number) + ". " + item + ", " + morse_text + "\n")
            line_number += 1
    else:
        morse_text = englishToMorse(english_text)
        outfile.write(english_text + ", " + morse_text + "\n")

    outfile.close()


#=============================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#=============================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
##q1 ======================================================================
def test_countXChars():
    print("\n\t\t**** (20 points) - countUniqueChars() ****")
    passed = 0
    attempted = 0
    sampleSentences = [
    ("we have all seen movies", 'm', 1),
    ("we   have  all    seen  movies", 'e', 5),
    ("we    have  all    seen    movies", ' ', 14),
    ("with traumatic break ins that filled us with horror.", 'i', 5),
    ("with   traumatic  break ins  that filled  us  with  horror!", 'a', 4)]

    for i in range(3):
        attempted += 1
        sentence = random.choice(sampleSentences)
        if test(sentence[2], countXChars, sentence[0], sentence[1]):
            passed += 1
    return passed, attempted





##q3 ======================================================================
def test_countXCharsRead():
    print("\n\t\t**** (20 points) - countXCharsRead() ****")
    passed = 0
    attempted = 0
    
    sampleSentences = [
    ("we have all seen movies", 'm', 1),
    ("we have all seen movies", 'e', 5),
    ("we have all seen movies", ' ', 4),
    ("with traumatic break ins that filled us with horror.", 'i', 5),
    ("with traumatic break ins that filled us with horror!", 'a', 4)]
    random.shuffle(sampleSentences)
    f = open("infile_Q2_a.txt", "w")
    f.write(sampleSentences[0][0]+'\n')
    f.close()
    
    result = sampleSentences[0][2]
    attempted += 1
    if test(sampleSentences[0][2], countXCharsRead, 'infile_Q2_a.txt', sampleSentences[0][1]):
        passed += 1
    
    f = open("infile_Q2_b.txt", "w")
    f.write(sampleSentences[1][0]+'\n')
    f.close()
    
    result = sampleSentences[1][2]
    attempted += 1
    if test(sampleSentences[1][2], countXCharsRead, 'infile_Q2_b.txt', sampleSentences[1][1]):
        passed += 1 
    
    return passed, attempted


##q3 ======================================================================
def test_countXCharsReadLines():
    print("\n\t\t**** (20 points) - countXCharsReadLines() ****")
    passed = 0
    attempted = 0

    s = "it is a nice day!\nI like programming.\nthis is the third line!"
    
    sampleSentences = [
    (s, 'm', 2),
    (s, 'e', 4),
    (s, ' ', 10),
    (s, 'i', 9),
    (s, 'a', 3)]
    random.shuffle(sampleSentences)
    f = open("infile_Q3_a.txt", "w")
    f.write(sampleSentences[0][0])
    f.close()
    
    result = sampleSentences[0][2]
    attempted += 1
    if test(sampleSentences[0][2], countXCharsReadLines, 'infile_Q3_a.txt', sampleSentences[0][1]):
        passed += 1
    
    f = open("infile_Q3_b.txt", "w")
    f.write(sampleSentences[1][0])
    f.close()
    
    result = sampleSentences[1][2]
    attempted += 1
    if test(sampleSentences[1][2], countXCharsReadLines, 'infile_Q3_b.txt', sampleSentences[1][1]):
        passed += 1 
    
    return passed, attempted


##q4 ======================================================================
def test_sumValues():
    print("\n\t\t**** (20 points) - sumValues() ****")
    passed = 0
    attempted = 0
    
    list_Size = 3
    lst = random.sample(range(-100, 100), list_Size)  
    random.shuffle(lst)
    f = open("infile_Q4_a.txt", "w")
    for i in lst:
        f.write(str(i)+'\n')
    f.close()
    
    attempted += 1
    if test(sum(lst), sumValues, 'infile_Q4_a.txt'):
        passed += 1
    
    list_Size = 5
    lst = random.sample(range(-100, 100), list_Size)  
    random.shuffle(lst)
    
    f = open("infile_Q4_b.txt", "w")
    for i in lst:
        f.write(str(i)+'\n')
    f.close()
    
    attempted += 1
    if test(sum(lst), sumValues, 'infile_Q4_b.txt'):
        passed += 1 
    
    return passed, attempted

##q5 ======================================================================
def test_sumValuesWrite():
    print("\n\t\t**** (20 points) - sumValuesWrite() ****")
    passed = 0
    attempted = 0
    
    list_Size = 3
    lst = random.sample(range(-100, 100), list_Size)  
    random.shuffle(lst)
    f = open("infile_Q5_a.txt", "w")
    for i in lst:
        f.write(str(i)+'\n')
    f.close()
    
    attempted += 1
    sumValuesWrite('infile_Q5_a.txt', 'outfile_Q5_a.txt')
    f = open('outfile_Q5_a.txt', 'r')
    result = int(f.readline())
    print("Testing sumValuesWrite('infile_Q5_a.txt', 'outfile_Q5_a.txt')")
    if result == sum(lst):
            passed += 1
    
    list_Size = 5
    lst = random.sample(range(-100, 100), list_Size)  
    random.shuffle(lst)
    
    f = open("infile_Q5_b.txt", "w")
    for i in lst:
        f.write(str(i)+'\n')
    f.close()
    
    attempted += 1
    sumValuesWrite('infile_Q5_b.txt', 'outfile_Q5_b.txt')
    f = open('outfile_Q5_b.txt', 'r')
    result = int(f.readline())
    print("Testing sumValuesWrite('infile_Q5_b.txt', 'outfile_Q5_b.txt')")
    if result == sum(lst):
            passed += 1
    
    return passed, attempted
# Main =======================================================================
def main():

    testFunctionList = [test_countXChars,
                        test_countXCharsRead,
                        test_countXCharsReadLines,
                        test_sumValues,
                        test_sumValuesWrite]
    
    functionNames = ["countUniquechars",
                     "countXCharsRead",
                     "countXCharsReadLines",
                     "sumValues",
                     "sumValuesWrite"]

    points = [-1 for i in range(len(testFunctionList))]
    totals = [0 for i in range(len(testFunctionList))]

    for i in range(len(testFunctionList)):
        try:
            points[i], totals[i] = testFunctionList[i]()
        except:
            print("**Something is wrong with " + functionNames[i] + "()")
            printErr()
            points[i], totals[i] = -1, 0

    print("\n\n")
    if points == totals:
        print("All tests Passed!")
    elif countFailed(points, totals) == len(points):
        print("All  tests FAILED...\nThe number of test cases that PASSED are:")
    else:
        print("Some tests FAILED...\nThe number of test cases that PASSED are:")

    print("======================================")

    for i in range(len(testFunctionList)):
        print(format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))
        else:
            print("Not defined or error in function")
#fail =========================================================================
def countFailed(points, totals):
    count = 0
    for i in range(len(points)):
        count += points[i] != totals[i]
    return count
#call =========================================================================
if __name__ == "__main__":
    main()


    
