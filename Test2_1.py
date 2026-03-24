# PROGRAM PURPOSE:............. Test 2 - Programming Portion
# (1 point) AUTHOR:............ Last, First
# COURSE:...................... CSC 131-XX
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
from testing_test2_practice import test,test_file_content,test_LOM,testNoPrint,test_NoReturn
import sys
import random

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
            


#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])

#q1 =========================================================================
def test_temperatureConv():
    print("\n\t\t**** (10 points) - temperatureConv() ****")
    temps = [(40,104), (50,122), (10,50), (15,59), (0,32), (50,122), (45,113)]
    random.shuffle(temps)
    invalid = ['r', 'g', 'D', 'e', 'W']
    random.shuffle(invalid)
    passed = 0
    attempted = 0    
    attempted += 1
    if test(temps[0][1], temperatureConv, 'c',temps[0][0]):
        passed += 1      
    attempted += 1
    if test(temps[0][0], temperatureConv, 'f',temps[0][1]):
        passed += 1
    attempted += 1
    if test(temps[1][1], temperatureConv, 'c',temps[1][0]):
        passed += 1      
    attempted += 1
    if test(temps[1][0], temperatureConv, 'f',temps[1][1]):
        passed += 1    
    attempted += 1
    if test(-1, temperatureConv, invalid[0], temps[2][1]):
        passed += 1
    return passed, attempted
    
#q2 =========================================================================
def test_backward():
    print("\n\t\t**** (10 points) - backward() ****")
    num1 = random.randint(1,5)
    num2 = random.randint(6,10)  
    num3 = random.randint(10,15) 
    nums = [num1, num2, num3]
    random.shuffle(nums)
    passed = 0
    attempted = 0
    for i in nums:
        attempted += 1
        if test(list(range(i,-1,-1)), backward, i):
            passed += 1
    return passed, attempted
    

#q3 =========================================================================   
def test_sumEven():
    import string
    print("\n\t\t**** (10 points) - sumEven() ****")
    passed = 0
    attempted = 0
    values = [(0,3,2),(4,14,54),(3,15,54),(12,15,26),(12,12,12), (13,13,0)]
    random.shuffle(values)
    for i in range(6):        
        attempted += 1
        if test(values[i][2], sumEven, values[i][0], values[i][1]):            
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
def test_fullNames():
    print("\n\t\t**** (10 points) - fullNames() ****")
    passed = 0
    attempted = 0

    firstNames = [['William', 'Whitney', 'Urmilla', 'Theresa'],
                  ['Stephanie', 'Stacy', 'Nicolas', 'Morgan', 'Deirdre'],
                  ['Mandy', 'Meredith', 'Amy', 'Hillary'],
                  ['Kristen', 'Mallory', 'Michelle'],
                  ['Julia', 'Courtney', 'Cierra', 'Caitlin', 'Alyssa']]
    lastNames = [['Brown', 'Justice', 'Nuckles', 'Pearce', 'Wilcox'],
                 ['Queen', 'Shepard'],
                 ['Haygood', 'Dominguez', 'Castillo', 'Blanchard'],
                 ['Foster', 'Edwards'],
                 ['Crider', 'Bello', 'Skelton', 'White', 'Wilson']]

    results = [['William Brown','William Justice','William Nuckles','William Pearce','William Wilcox',
                'Whitney Brown','Whitney Justice','Whitney Nuckles','Whitney Pearce','Whitney Wilcox',
                'Urmilla Brown','Urmilla Justice','Urmilla Nuckles','Urmilla Pearce','Urmilla Wilcox',
                'Theresa Brown','Theresa Justice','Theresa Nuckles','Theresa Pearce','Theresa Wilcox'],
               ['Stephanie Queen','Stephanie Shepard',
                'Stacy Queen','Stacy Shepard',
                'Nicolas Queen','Nicolas Shepard',
                'Morgan Queen','Morgan Shepard',
                'Deirdre Queen','Deirdre Shepard',],
               ['Mandy Haygood','Mandy Dominguez','Mandy Castillo','Mandy Blanchard',
                'Meredith Haygood','Meredith Dominguez','Meredith Castillo','Meredith Blanchard',
                'Amy Haygood','Amy Dominguez','Amy Castillo','Amy Blanchard',
                'Hillary Haygood','Hillary Dominguez','Hillary Castillo','Hillary Blanchard'],
               ['Kristen Foster','Kristen Edwards',
                'Mallory Foster','Mallory Edwards',
                'Michelle Foster','Michelle Edwards'],
               ['Julia Crider','Julia Bello','Julia Skelton','Julia White','Julia Wilson',
                'Courtney Crider','Courtney Bello','Courtney Skelton','Courtney White','Courtney Wilson',
                'Cierra Crider','Cierra Bello','Cierra Skelton','Cierra White','Cierra Wilson',
                'Caitlin Crider','Caitlin Bello','Caitlin Skelton','Caitlin White','Caitlin Wilson',
                'Alyssa Crider','Alyssa Bello','Alyssa Skelton','Alyssa White','Alyssa Wilson']]
    for i in range(len(firstNames)):
        attempted += 1
        if test(results[i], fullNames, firstNames[i], lastNames[i]): passed += 1

    return passed, attempted

#q7 ======================================================================
def test_readNLines():
    print("\n\t\t**** (10 points) - readNLines() ****")
    passed = 0
    attempted = 0

##    attempted += 1
##    if test(None, readNLines, "nofile.txt",10): passed += 1
    
    cars = ["Small Cars", "Mid-Size Cars", "Large Cars", "SUVs", "Trucks",
     "Wagons", "Luxury", "Sports Cars", "Convertibles", "Vans"]
    random.shuffle(cars)
    f = open("testfile.txt", "w")
    for i in cars:
        f.write(i+'\n')
    f.close()
    result = ' '.join(cars[0:4])
    attempted += 1
    if test(result, readNLines, 'testfile.txt',4) or \
         testNoPrint(" " + result, readNLines, 'testfile.txt',4) or \
         testNoPrint(result + " ", readNLines, 'testfile.txt', 4):
        passed += 1
    
    f = open("testfile.txt", "w")
    f.write("apple\napple\nfruit\nfruit\ncarrot\ncarrot\n")
    f.close()
    result = "apple apple"    
    attempted += 1
    if test(result, readNLines, 'testfile.txt',2) or \
         testNoPrint(" " + result, readNLines, 'testfile.txt',2) or \
         testNoPrint(result + " ", readNLines, 'testfile.txt', 2):
        passed += 1   
    
    attempted += 1
    if test("", readNLines, "testfile.txt",0) or \
       testNoPrint(" ", readNLines, "testfile.txt",0):
        passed += 1
    
    return passed, attempted
           
#q7==========================================================================
def test_writeSum():
    results = []
    print("\n\t\t**** (10 points) - writeSum() ****")
    numbers = list(range(1,5))
    ms = ""
    lst1 = []
    
    passed = 0
    attempted = 0
    total = 0
    for r in range(random.randint(1,5)):
        item = []
        for x in range(random.randint(1,4)):
            num = random.choice(numbers)
            item.append(num)
            total += num
        lst1.append(item)
          
    results.append(test(total,writeSum,"test2_sample_output1.txt",lst1))
    attempted += 1
    if test(total,writeSum,"test2_sample_output1.txt",lst1):            
        passed += 1

    return passed, attempted                 
        
# Main =======================================================================
def main():

    testFunctionList = [test_temperatureConv, test_backward,
                        test_sumEven, test_convertToInts,
                        test_fullNames, test_readNLines,
                        test_writeSum]
    functionQuestionNo = [  1, 2, 3, 4,
                            5, 6, 7, 8, 9]
    functionNames = ["temperatureConv", "backward", 
                     "sumEven", "convertToInts",
                     "fullNames", "readNLines",
                     "writeSum"]
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






##    points = [-1 for i in range(len(testFunctionList))]
##    totals = [0 for i in range(len(testFunctionList))]
##
##    for i in range(len(testFunctionList)):
##        try:
##            points[i], totals[i] = testFunctionList[i]()
##                
##        except:
##            print("**Something is wrong with " + functionNames[i] + "()")
##            printErr()
##            points[i], totals[i] = -1, 0
##
##    print("\n\n")
##    print("Summray of the Test Results")
##    print("======================================")
##
##    for i in range(len(testFunctionList)):
##        print(format(functionNames[i], "27s"), end="")
##        if points[i] >= 0:
##            print("%2d out of %2d" % (points[i], totals[i]))            
##            if points[i] == totals[i] and points[i] in [0,1]:
##                print("{}: Instructor will check the output in read-time".format(functionNames[i]))
##        else:
##            print("Not defined or error in function")
###fail =========================================================================
##def countFailed(points, totals):
##    count = 0
##    for i in range(len(points)):
##        count += points[i] != totals[i]
##    return count
###call =========================================================================
##if __name__ == "__main__":
##    main()
##
##

