#=============================================================================
# PROGRAM PURPOSE:... practice
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-00X
# TERM:.............. XXX
# COLLABORATION:..... None
#=============================================================================

from testing_test2_practice import test,test_file_content,test_LOM,testNoPrint
import sys
import random

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
    """Returns the positive difference between two integers."""
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
    """Creates and returns a list of integers from a to b inclusive."""
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
    """Counts how many times a letter appears in a list of words (case-insensitive)."""
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




#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])


def test_my_max():
    results = []
    print("\n\t\t**** (10 points) - my_max ****")
    passed = 0
    attempted = 0
    for i in range(3):
        attempted += 1
        a = random.randint(-5,1)
        b = random.randint(-1,5)
        c = max(a,b)
        if test(c, my_max, a,b):
            passed += 1
    return passed, attempted
    
    
def test_positiveIntDiff():
    results = []
    print("\n\t\t**** (10 points) - positiveIntDiff() ****")
    passed = 0
    attempted = 0
    for i in range(3):
        attempted += 1
        a = random.randint(-10,10)
        b = random.randint(9,30)
        c = max(a,b)-min(a,b)
        if test(c, positiveIntDiff, a,b):
            passed += 1
    return passed, attempted


def test_sumPos():
    results = []
    print("\n\t\t**** (10 points) - sumPos() ****")
    passed = 0
    attempted = 0
    for i in range(3):
        attempted += 1
        a = random.randint(-7,-2)
        b = random.randint(0,6)
        c = sum(list(range(0, b)))        
        d = list(range(a, b))
        random.shuffle(d)
        if test(c, sumPos, d):
            passed += 1
    return passed, attempted

        
def test_make_list():
    results = []
    print("\n\t\t**** (10 points) - make_list() ****")
    passed = 0
    attempted = 0
    for i in range(3):
        attempted += 1
        a = random.randint(-2,2)
        b = random.randint(3,5)
        c = list(range(a, b+1))  
        if test(c, make_list, a, b):
            passed += 1
    return passed, attempted

def test_countLetter():
    results = []
    print("\n\t\t**** (10 points) - countLetter() ****")
    passed = 0
    attempted = 0
    for i in range(2):
        a = ('apple', 'BanAna', 'CHERRY', 'ORANGE')
        b = ("House", "townhouse", "condo", "APARTMENT")
        c = chr(random.randint(65,90))
        d = chr(random.randint(97,122))
        aSum = 0
        bSum = 0
        for i,j in zip(a,b):
            aSum += i.lower().count(c.lower())
            bSum += j.lower().count(d.lower())
        attempted += 1
        if test(aSum, countLetter, a, c):
            passed += 1
        attempted += 1
        if test(bSum, countLetter, b, d):
            passed += 1
            
    return passed, attempted
    
def test_openAndReturnLastN():
    results = []
    print("\n\t\t**** (10 points) - openAndReturnLastN() ****")
    a = ('pretty', 'sick', 'warm', 'nice', 'tired')
    b = ('book', 'pillow', 'bedroom', 'car', 'sky')
    output_file = open("labX_sample.txt",'w')
    ms = ""
    ml = []
    passed = 0
    attempted = 0
    for r in range(random.randint(20,30)):
        ls = ""
        item = ""
        for x in range(5):
            ls += a[random.randint(0,4)] + ' '
        ls += b[random.randint(0,4)]
        ml.append(ls)
        ls += "\n"
        output_file.write(ls)
    output_file.close()
    res = ml[-4].strip()+ml[-3].strip()+ml[-2].strip()+ml[-1].strip()
    attempted += 1
    if test(res, openAndReturnLastN, "labX_sample.txt", 4):
        passed += 1
    res = ml[-3].strip()+ml[-2].strip()+ml[-1].strip()
    attempted += 1
    if test(res, openAndReturnLastN, "labX_sample.txt", 3):
        passed += 1
    attempted += 1
    if test(False, openAndReturnLastN, "sample.txt", 3):
        passed += 1

    return passed, attempted    

def test_writeMeAFile():
    results = []
    print("\n\t\t**** (10 points) - writeMeAFile() ****")
    fruits = ('apple', 'banana', 'cherry', 'orange', 'grape', 'pineapple','mango')
    ms = ""
    lst1 = []
    passed = 0
    attempted = 0
    for r in range(random.randint(10,20)):
        for x in range(5):
            lst1.append(fruits[random.randint(0,len(fruits)-1)])   
            
    attempted += 1
    if test(len(lst1), writeMeAFile, "labX_sample_output.txt",lst1):
        passed += 1
        
    return passed, attempted 

# Main =======================================================================
def main():

    testFunctionList = [test_my_max, test_positiveIntDiff,
                        test_sumPos, test_make_list,
                        test_countLetter, test_openAndReturnLastN,
                        test_writeMeAFile]
    
    functionNames = ["my_max", "positiveIntDiff", 
                     "sumPos", "make_list",
                     "countLetter", "openAndReturnLastN",
                     "writeMeAFile"]

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


    














