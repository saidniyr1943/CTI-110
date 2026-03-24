# PROGRAM PURPOSE:... Practice
# (1 point) AUTHOR:............ Last, First
# COURSE:............ CSC 131-YOUR SECTION NUMBER
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
from testing_test2_practice import test,test_file_content,test_LOM,testNoPrint,test_NoReturn
import sys
import random


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


#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
    
#q1==========================================================================
def test_negativeIntDiff():
    print("\n\t\t**** (10 points) - negativeIntDiff() ****")
    passed = 0
    attempted = 0
    values = [(-7,12,-19),(13,9,-4),(-2,-5,-3),(-1,1,-2), (10,10,0), (-10,10,-20)]
    random.shuffle(values)
    for i in range(6):
        attempted += 1
        if test(values[i][2], negativeIntDiff, values[i][0], values[i][1]):
            passed += 1
    return passed, attempted


#q2==========================================================================
def test_sumOfSquares():
    print("\n\t\t**** (10 points) - sumOfSquares() ****")
    passed = 0
    attempted = 0
    values = [(20,2870),(2,5),(5,55),(4,30), (10,385), (0,0)]
    random.shuffle(values)
    for i in range(6):        
        attempted += 1
        if test(values[i][1], sumOfSquares, values[i][0]):          
            passed += 1
    return passed, attempted




#q3 =========================================================================
def test_numSpaces():
    results = []
    # Note that the strings must also be put inside of single quotes
    # so that the "test" function will print the test case with the
    # double quotes.  But then we need to escape the apostrophes.
    sampleSentences = [
                    ("We have all seen movies", 4),
                    ("with traumatic break ins that filled us with horror. ", 9),
                    ("there is the worst nightmare of many. Fortunately, unlike movies, ", 10),
                    (" It\'s  still pretty terrifying, though, to wake up in ", 11),
                    (" the middle of the  night and realize someone else is in your ", 14),
                    ("house—and one can\'t exactly read a burglar\'s mind or know his or ", 12),
                    ("her intentions. Here\'s a pretty good overview if you ", 9),
                    ("", 0),
                    (" ", 1),
                    ("", 0),
                    (" ", 1)
                    ]

    print("\n\t\t**** (10 points) - numSpaces() ****")
    passed = 0
    attempted = 0

    for i in range(5):
        attempted += 1
        sentence = random.choice(sampleSentences)
        if test(sentence[1], numSpaces, sentence[0]):
            passed += 1
    return passed, attempted

#q4 =========================================================================
def test_convertToInts():
    print("\n\t\t**** (10 points) - convertToInts() ****")
    passed = 0
    attempted = 0

    nums = [i for i in range(100)]
    strings = [str(i) for i in range(100)]

    for i in range(5):
        nums1 = []
        nums2 = []
        for j in range(10):
            k = random.randint(0, 99)
            nums1.append(nums[k])
            nums2.append(strings[k])
        attempted += 1
        if test_NoReturn(nums1, convertToInts, nums2): passed += 1

    return passed, attempted

#q5==========================================================================
def test_commonItem():
    print("\n\t\t**** (10 points) - commonItem() ****")
    passed = 0
    attempted = 0

    lst1 = [2,5,4,7]
    lst2 = [1,2,1,4]  
    attempted += 1
    if test(True, commonItem, lst1, lst2):
        passed += 1

    lst1 = ['a','b','c','a']
    lst2 = ['g','a','c'] 
    attempted += 1
    if test(True, commonItem, lst1, lst2):
        passed += 1
    
    lst1 = ['sara', 'peter', 'alex', 'tom']
    lst2 = ['smith', 'brown', 'jones']    
    attempted += 1
    if test(False, commonItem, lst1, lst2):
        passed += 1

    return passed, attempted

#q6==========================================================================
def test_countVowels():
    print("\n\t\t**** (10 points) - countVowels() ****")
    passed = 0
    attempted = 0

    values = [["WiLL yOu sTilL hAve TO eNlArgE tHe PaRTITion?",15],
              ["ReDDiT uSErs fOUNd The pAREnt’S behAvIOR tO Be TrouBling.",18],
              ["To PUT tHIs TroublE BEHIND them ...", 9],
              ["they rElEasEd two NEW pORTraiTs To marK thEIr tEnth wEddIng aNNiveRsary.", 21],
              ["Her Husband oPTEd fOr A blUE shIrt", 10],
              ["She HAS GOT sUch PoIsE aNd eLeGAncE!", 12],
              ["Only A cERtAIn peRCenTAge HAd to BE sENiorS.", 15],
              ["The REnt WAs sIGNifICAntly cHEapER COmpaREd to wHEre I hAD moVED frOM.", 21],
              ["I sTARTed mEEting SoMe Of mY neIGhbORs.", 12]
             ]
    random.shuffle(values)
    for i in range(5):        
        attempted += 1
        if test(values[i][1], countVowels, values[i][0]):            
            passed += 1
    return passed, attempted



#q7==========================================================================
def test_readIt():
    results = []
    print("\n\t\t**** (10 points) - readIt() ****")    
    passed = 0
    attempted = 0
    
    # random float from 1 to 99.9
    list_Size = 10
    lst = random.sample(range(1, 100), list_Size)    
    total = sum(lst)
    output_file = open("sample_input1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()
    attempted += 1
    if test(total,readIt,"sample_input1.txt"):            
        passed += 1
        
    list_Size = 5
    lst = random.sample(range(1, 100), list_Size) 
    total = sum(lst)
    output_file = open("sample_input2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()     
    attempted += 1
    if test(total,readIt,"sample_input2.txt"):            
        passed += 1

    lst = []
    total = sum(lst)
    random.shuffle(lst)
    output_file = open("sample_input3.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(str(lst[i])+"\n")
    output_file.close()     
    attempted += 1
    if test(total,readIt,"sample_input3.txt"):            
        passed += 1

    return passed, attempted

#q8 =========================================================================
def test_writeMinMaxSumCount():
    results = []
    print("\n\t\t**** (10 points) - writeMinMaxSumCount() ****")

    attempted = 0
    passed = 0

    list_Size = 10
    for n in range(0,3):
        lst = random.sample(range(1, 100), list_Size)  
        random.shuffle(lst)
        
        attempted += 1
        filename = "sample_output"+str(n+1)+'.txt'
        returnVal = writeMinMaxSumCount(filename, lst)
        try:
            infile = open(filename, 'r')
        except:
            print("The output file hasn't be created correctly")
        finalList = [min(lst), max(lst), sum(lst), len(lst)]
        studentList = []
        for i in infile:
            studentList.append(int(i.strip()))
        
        if studentList == finalList and returnVal is None:
            passed += 1
        infile.close()
    

    return passed, attempted

#q9==========================================================================   
def test_triangle():
    results = []
    print("\n\t\t**** (10 points) - triangle() ****")
    
    passed = 0
    attempted = 0
    row = random.randint(2,9)
    triangle(row)
    row = random.randint(2,9)
    triangle(row)
    return passed, attempted 
        
#q10==========================================================================   

def test_changeValues():
    results = []
    print("\n\t\t**** (5 points) - changeValues() ****")
    passed = 0
    attempted = 0
    values = [([1,2,4,5],[3, 1.0, 12, 2.5]),
              ([2,25,15,3],[6, 12.5, 45, 1.5]),
              ([3,5,3],[9, 2.5, 9]),
              ([3],[9]),
              ([],[])]
    for i in range(len(values)):
        attempted += 1
        # changeValues(values[i][0])
        # print("Testing changeValues({})".format(values[i][0]))
        # if values[i][1]==values[i][0]:
            # passed += 1
        if test_NoReturn(values[i][1], changeValues, values[i][0]):
            passed += 1


    return passed, attempted    

#q10 =========================================================================
def test_numOdds():
    print("\n\n*******(5 points) - numOdds ********")
    attempted = 0
    passed = 0
    attempted += 1
    if test(4, numOdds, [1,3,3,1]): passed += 1
    attempted += 1
    if test(0, numOdds, []): passed += 1
    attempted += 1
    if test(2, numOdds, [-1,-2,-2,-2,-2,-2,-2,1]): passed += 1
    return passed, attempted

#q10 =========================================================================
def test_find():
    print("\n\n*******(5 points) - find ********")
    strList = ['apple', 'banana', 'cherry', 'orange', 'watermelon']
    chars = [['a', 6], ['b', 1], ['c',1], ['e', 5], ['n', 4], ['r', 4]]

    random.shuffle(chars)
    attempted = 0
    passed = 0
    for i in range(3):
        attempted += 1
        if test(chars[i][1], find, strList, chars[i][0]): passed += 1
    return passed, attempted

        
# Main =======================================================================
def main():

    testFunctionList = [test_negativeIntDiff,
                        test_sumOfSquares,
                        test_numSpaces, 
                        test_convertToInts, 
                        test_commonItem, 
                        test_countVowels,
                        test_readIt, 
                        test_writeMinMaxSumCount,
                        test_triangle]

    functionQuestionNo = [  1, 
                            2, 
                            3, 
                            4, 
                            5, 
                            6, 
                            7, 
                            8, 
                            9, 
                            10]
        
    functionNames = ["negativeIntDiff",
                     "sumOfSquares",  
                     "numSpaces", 
                     "convertToInts", 
                     "commonItem", 
                     "countVowels", 
                     "readIt",  
                     "writeMinMaxSumCount",
                     "triangle"]

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
    print("Summary of the Test Results")
    print("======================================")

    for i in range(len(testFunctionList)):
        #print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        print(format('q'+str(functionQuestionNo[i]),'<4'), format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))            
            if points[i] == totals[i] and points[i] in [0,1]:
                print("{}: Instructor will check the output manually".format(functionNames[i]))
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






















