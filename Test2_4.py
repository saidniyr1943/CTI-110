
#==========================================================================
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
## Closed Book, you may use your editor and help from the shell,
## no additional import statements please
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.

# PROGRAM PURPOSE:... practice
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-00X
# TERM:.............. XXX
# COLLABORATION:..... None
#==========================================================================

from testing_test2_practice import test,test_file_content,test_LOM,testNoPrint
import sys
import random

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
            


#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])

def test_letterGrade():
    print("\n\t\t**** (10 points) - letterGrade() ****")
    num1 = ('A', random.randint(90,100))
    num2 = ('B', random.randint(80,89))    
    num3 = ('C', random.randint(70,79))    
    num4 = ('D', random.randint(60,69))
    num5 = ('F', random.randint(0,59))
    nums = [num1, num2, num3, num4, num5]
    random.shuffle(nums)
    passed = 0
    attempted = 0
    for i in nums:
        attempted += 1
        if test(i[0], letterGrade, i[1]):
            passed += 1
    return passed, attempted
    
   
def test_isIntDiffOdd():
    results = []
    print("\n\t\t**** (10 points) - isIntDiffOdd() ****")
    passed = 0
    attempted = 0
    for i in range(3):        
        a = random.randint(-30,5)
        b = random.randint(-5,30)
        attempted += 1
        if test(bool((a-b)%2), isIntDiffOdd, a, b):
            passed += 1
    return passed, attempted


def test_hasSameNumElements():
    results = []
    print("\n\t\t**** (10 points) - hasSameNumElements() ****")
    lst = ['Tom', ('orange', 'apple', 'banana'), ['orange', 'apple', 'banana', 'cherry'],
           'book', [1, 2], [1, 2, 3], (5, 6, 7, 8)]
    passed = 0
    attempted = 0
    for i in range(3):        
        a = random.randint(0,6)
        b = random.randint(0,6)        
        attempted += 1
        if test(len(lst[a])==len(lst[b]), hasSameNumElements, lst[a], lst[b]):            
            passed += 1
    attempted += 1
    if test(True, hasSameNumElements, lst[a], lst[a]):
        passed += 1
    return passed, attempted
            

def test_getUserCharInput():
    import string
    print("\n\t\t**** (10 points) - getUserCharInput() ****")
    alpha = string.ascii_letters
    passed = 0
    attempted = 0
    a = random.choice(alpha)
    b = random.choice(alpha)
    c = random.choice(alpha)
    d = random.choice(alpha)
    e = random.choice(alpha)
    print('\nArguments passed to the functions are {}, {}, {}, {}, and {}'.format(a, b, c, d, e))
    ui = getUserCharInput(a, b, c, d, e)
    attempted += 1
    if ui in a+b+c+d+e:           
        passed += 1
    return passed, attempted      

def test_backward():
    results = []
    print("\n\t\t**** (10 points) - backward() ****")
    smd = ('yensid', 'harpo', 'nacirema', 'erewhon', 'yob', 'silopanna', 
        'retsof', 'llareggub', 'dog', 'diaper', 'repaid', 'desserts',
        'disney', 'oprah', 'american', 'nohwere', 'boy', 'annapolis', 
        'foster', 'buggerall', 'god', 'repaid', 'diaper', 'stressed')
    
    passed = 0
    attempted = 0
    for i in range(5):
        idx = random.randint(0,11)       
        attempted += 1
        if test(smd[idx+12], backward, smd[idx]):            
            passed += 1
    return passed, attempted    

def test_print2DListContent():
    print("\n\t\t**** (10 points) - print2DListContent() ****")
    print('Instructor will check the output in read-time')
    print2DListContent( [['red','square', 'one'], ['yellow','triangle'], ['blue','circle', 'three']] )
    print()
    print2DListContent( [[1,2], [3,4]] )
    print()
    print2DListContent( [[3.0, 'dogs', 2], [1, 2], ['cat', 'bird', 'banana']] )

    passed = 0
    attempted = 0
    return passed, attempted

def test_createPlates():
    results = []
    print("\n\t\t**** (10 points) - createPlates() ****")
    Lo3L = ['TEK', 'EHU', 'OPB', 'THU', 'OXW']
    Lo4D = [5789, 2246, 2074, 8974, 3530, 7356]
    VLo7LD = ['EHU-2074', 'EHU-2246', 'EHU-3530', 'EHU-5789', 'EHU-7356', 'EHU-8974',
              'OPB-2074', 'OPB-2246', 'OPB-3530', 'OPB-5789', 'OPB-7356', 'OPB-8974',
              'OXW-2074', 'OXW-2246', 'OXW-3530', 'OXW-5789', 'OXW-7356', 'OXW-8974',
              'TEK-2074', 'TEK-2246', 'TEK-3530', 'TEK-5789', 'TEK-7356', 'TEK-8974',
              'THU-2074', 'THU-2246', 'THU-3530', 'THU-5789', 'THU-7356', 'THU-8974']

    Lo3L_B = ['XSH', 'VBO', 'SAJ', 'XED', 'UMA', 'ZOY', 'ZIA', 'LKW']
    Lo4D_B = [5992, 5497, 2954, 9971, 9562]
    VLo7LD_B = ['LKW-2954', 'LKW-5497', 'LKW-5992', 'LKW-9562', 'LKW-9971',
              'SAJ-2954', 'SAJ-5497', 'SAJ-5992', 'SAJ-9562', 'SAJ-9971',
              'UMA-2954', 'UMA-5497', 'UMA-5992', 'UMA-9562', 'UMA-9971',
              'VBO-2954', 'VBO-5497', 'VBO-5992', 'VBO-9562', 'VBO-9971',
              'XED-2954', 'XED-5497', 'XED-5992', 'XED-9562', 'XED-9971',
              'XSH-2954', 'XSH-5497', 'XSH-5992', 'XSH-9562', 'XSH-9971',
              'ZIA-2954', 'ZIA-5497', 'ZIA-5992', 'ZIA-9562', 'ZIA-9971',
              'ZOY-2954', 'ZOY-5497', 'ZOY-5992', 'ZOY-9562', 'ZOY-9971']
    
    passed = 0
    attempted = 0

    attempted += 1
    if test(sorted(VLo7LD), createPlates, Lo3L, Lo4D):            
        passed += 1
    attempted += 1
    if test(sorted(VLo7LD_B), createPlates, Lo3L_B, Lo4D_B):            
        passed += 1
    
    return passed, attempted    
        

def test_openAndReturnMiddle():
    results = []
    print("\n\t\t**** (10 points) - openAndReturnMiddle() ****")
    a = ('pretty', 'sick', 'warm', 'nice', 'tired')
    b = ('book', 'pillow', 'bedroom', 'car', 'sky')
    output_file = open("test2_sample.txt",'w')
    ms = ""
    ml = []
    num = list(range(11, 20, 2))
    for r in range(random.choice(num)):
        ls = ""
        item = ""
        for x in range(5):
            ls += a[random.randint(0,4)] + ' '
        ls += b[random.randint(0,4)]
        ml.append(ls)
        ls += "\n"
        output_file.write(ls)
    output_file.close()
    res = ml[r//2] 

    passed = 0
    attempted = 0

    attempted += 1
    if test(res,openAndReturnMiddle,"test2_sample.txt"):            
        passed += 1
    attempted += 1
    if test(False,openAndReturnMiddle,"sample.txt"):            
        passed += 1

    return passed, attempted  

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

    testFunctionList = [test_letterGrade, test_isIntDiffOdd,
                        test_hasSameNumElements, test_getUserCharInput,
                        test_backward, test_print2DListContent,
                        test_createPlates, test_openAndReturnMiddle,
                        test_writeSum]
    
    functionNames = ["letterGrade", "isIntDiffEven", 
                     "hasSameNumElements", "getUserCharInput",
                     "backward", "print2DListContent",
                     "createPlates", "openAndReturnMiddle",
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
    print("Summray of the Test Results")
    print("======================================")

    for i in range(len(testFunctionList)):
        print(format(functionNames[i], "27s"), end="")
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



