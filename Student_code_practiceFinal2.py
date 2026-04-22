
#==========================================================================
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
## you may use your editor, help from the shell, use your textbooks, 
## your previous codes, and the lecture notes as reference
## no other resources can be used during the test.
## no additional import statements please
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.

# PROGRAM PURPOSE:... Practice 2 
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-YOUR SECTION NUMBER
# TERM:.............. Fall 2021
# COLLABORATION:..... None
#==========================================================================

from testing_practice2 import test,test_file_content,test_LOM,testNoPrint
import sys
import random

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

def sumValues(lis,num):
    bucket=0
    for i in range(num):
        bucket+=lis[i]
    print(bucket)
    return bucket   

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
def countPairs(lst,lst1,num):
    bucket=0
    for i in lst:
        for j in lst1:
            total=i+j
            if total == num:
                bucket+=1
    return bucket

#also see how can we return pairs as tuples as well, maybe return a list that has touples of pairs inside
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


def createWord(lis):
    bucket=''
    for i in range(0,len(lis)):
        item=lis[i]
        bucket+=item[i]
    return bucket

        

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
#what if dictionary was reversed



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
    '''accept a list of integers; count how many are odd; return that value'''
    count = 0
    count1=0
    for i in intList:
        if i % 2 == '0':
            count =+ 1   

    return count

#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
    
#q1==========================================================================   
def test_isIntDiffEven():
    print("\n\t\t**** (10 points) - isIntDiffEven() ****")
    passed = 0
    attempted = 0
    for i in range(3):        
        a = random.randint(-30,5)
        b = random.randint(-5,30)
        attempted += 1
        if test(not((a-b)%2), isIntDiffEven, a, b):
            passed += 1
    return passed, attempted

#q2==========================================================================
def test_numCount():
    print("\n\t\t**** (10 points) - numCount() ****")
    passed = 0
    attempted = 0
    nums = [20,2,5,4,54,24,24,25,2,5,10,10,2]
    values = ((nums,2,3),(nums,20,1),(nums,100,0),(nums,24,2))
    for i in range(4):        
        attempted += 1
        if test(values[i][2], numCount, values[i][0], values[i][1]):            
            passed += 1
    return passed, attempted
            
#q3==========================================================================
def test_sumValues():
    import string
    print("\n\t\t**** (10 points) - sumValues() ****")
    passed = 0
    attempted = 0
    nums = [20,2,5,4,54,24,24,25,2,5,10,10,2]
    values = ((nums,3,27),(nums,5,85),(nums,13,187),(nums,1,20))
    for i in range(4):        
        attempted += 1
        if test(values[i][2], sumValues, values[i][0], values[i][1]):            
            passed += 1
    return passed, attempted  

#q4==========================================================================
def test_countPairs():
    print("\n\t\t**** (10 points) - countPairs() ****")
    passed = 0
    attempted = 0
    values = (([2,5,4,7,2], [1,2,1,4,2], 8, 3),
              ([1,2,3,4], [2,3,4,5], 6, 4),
              ([2,5,4,7,2], [10,20,10], 1, 0),
              ([2,5,4,7,2], [10,20,10], 12, 4))
    for i in range(4):        
        attempted += 1
        if test(values[i][3], countPairs, values[i][0], values[i][1],values[i][2]):            
            passed += 1
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
def test_createWord():
    results = []
    print("\n\t\t**** (10 points) - createWord() ****")    
    passed = 0
    attempted = 0
    
    values = [(['case', 'poor', 'from', 'yellow'], 'cool'),
              (['red','you','return'], 'rot'),
              (['member', 'sara', 'pass', 'pass'],'mass')]
    random.shuffle(values)

    for i in range(3):
        attempted += 1
        if test(values[i][1], createWord, values[i][0]):            
            passed += 1
    
    return passed, attempted    
        
#q7==========================================================================
def test_openAndReturnFML():
    results = []
    print("\n\t\t**** (10 points) - openAndReturnFML() ****")    
    passed = 0
    attempted = 0
    
    lst = ['pretty', 'sick', 'warm', 'nice', 'tired', 'book',
           'pillow', 'bedroom', 'car', 'sky', 'wonderful']
    random.shuffle(lst)
    result = lst[0]+lst[len(lst)//2]+lst[-1]
    output_file = open("sample_input1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(lst[i]+"\n")
    output_file.close()
    attempted += 1
    if test(result,openAndReturnFML,"sample_input1.txt"):            
        passed += 1
        
    lst = ['hall', 'gallery', 'factory', 'depot', 'barn', 'airport',
           'garage', 'gym', 'hotel', 'cabin', 'mall', 'kiosk', 'yard']
    random.shuffle(lst)
    restul = lst[0]+lst[len(lst)//2]+lst[-1]
    output_file = open("sample_input2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst)):
        output_file.write(lst[i]+"\n")
    output_file.close()     
    attempted += 1
    if test(restul,openAndReturnFML,"sample_input2.txt"):            
        passed += 1

##         
##    attempted += 1
##    if test(False,openAndReturnFML,"dontExist.txt"):            
##        passed += 1

    return passed, attempted  

#q8 =========================================================================
def test_writeEvenNumbers():
    results = []
    print("\n\t\t**** (10 points) - writeEvenNumbers() ****")

    attempted = 0
    passed = 0

    icr = 2
    start = 2

    count = 0
    for n in [100, 11, 10]:
        attempted += 1
        count += 1
        filename = "sample_output"+str(count)+'.txt'
        writeEvenNumbers(filename, n)
        finalList = []
        for i in range(start, n+1, icr):
            finalList.append(str(i))
        try:
            infile = open(filename, 'r')
        except:
            print("The output file hasn't be created correctly")
        studentList = []
        for i in infile:
            studentList.append(i.strip())
        if studentList == finalList:
            passed += 1
        infile.close()
    return passed, attempted

#q9 =========================================================================
def test_translateMorse():
    print("\n\n*******(10 points) - translateMorse ********")
    attempted = 0
    passed = 0
    m2e = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
       '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
       '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
       '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
       '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
       '--..': 'z', '/' : ' '}
    mc = ('-.-.', '.-..', '.', '...-', '.', '.-.')
    mct = "clever"
    attempted += 1
    if test(mct, translateMorse, m2e, mc): passed += 1
    mc = ('-...', '.', '/', '...', '---', '/', '--.', '---', '---',
          '-..', '/', '-', '....', '.', '-.--', '/', '-.-.', '.-', '-.',
          '-.', '---', '-', '/', '..', '--.', '-.', '---', '.-.', '.',
          '/', '-.--', '---', '..-')
    mct = "be so good they cannot ignore you"    
    attempted += 1
    if test(mct, translateMorse, m2e, mc): passed += 1
    mc = ('.', '...-', '.', '.-.', '-.--', '/', '--', '---', '--',
          '.', '-.', '-', '/', '..', '...', '/', '.-', '/', '..-.',
          '.-.', '.', '...', '....', '/', '-...', '.', '--.', '..',
          '-.', '-.', '..', '-.', '--.')
    mct = "every moment is a fresh beginning"    
    attempted += 1
    if test(mct, translateMorse, m2e, mc): passed += 1
    
    return passed, attempted  
    
#q10=========================================================================
def test_dupWords():
    print("\n\n*******(5 points) - dupWords ********")
    attempted = 0
    passed = 0
    wt = ('yes','no','no','hi','bye','hi','hi')  
    attempted += 1
    if test_LOM(['hi','no'], dupWords, wt): passed += 1
    wt = ('smar', 'smar', 'gorp', 'ibex', 'doup', 'ibex', 'coif', 'smar',
          'coif', 'gorp', 'coif', 'doup')  
    attempted += 1
    if test_LOM(['coif', 'doup', 'gorp', 'ibex', 'smar'], dupWords, wt):
        passed += 1
    return passed, attempted
        
#q11==========================================================================   

def test_numOdds():
    results = []
    print("\n\t\t**** (5 points) - numOdds() ****")
    passed = 0
    attempted = 0
    values = [([1,1,4,66,-13,22,51],4),
              ([123,45,4,66,0,17,4],3),
              ([0,2,4,6,8],0),
              ([1,3,5,7,9],5)]
    for i in range(len(values)):
        attempted += 1
        if test(values[i][1],numOdds,values[i][0]):            
            passed += 1

    return passed, attempted    
        
# Main =======================================================================
def main():

    testFunctionList = [test_isIntDiffEven, test_numCount,
                        test_sumValues, test_countPairs,
                        test_commonItem, test_createWord,
                        test_openAndReturnFML, test_writeEvenNumbers, 
                        test_translateMorse, test_dupWords, 
                        test_numOdds]
    
    functionNames = ["isIntDiffEven", "numCount",
                     "sumValues", "countPairs",
                     "commonItem", "createWord",
                     "openAndReturnFML", "writeEvenNumbers",
                     "translateMorse", "dupWords",
                     "numOdds"]

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
        print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))            
            if points[i] == totals[i] and points[i] in [0,1]:
                print("{}: Instructor will check the output in read-time".format(functionNames[i]))
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





