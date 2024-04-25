def main():
    #displayInfo()
    num=getNumber()
    tot=getTotalGrades(num)
    ave=caclAverage(num,tot)
    letter=getLetterAverage(ave)
    DusplayResults(num,tot,ave,letter)




def displayInfo():
    print("RUSTY")
    print("21/20/2021")
    print("This program will calculate the grade")
    print



def getNumber():
    number=int(input('Eneter number of grades to average: '))
    return number
def getTotalGrades(n):
    total=0
    for i in range(n):
        grade=int(input("Enter the grade: "))
        total+=grade
    return total


def caclAverage(number, total):
    return total//number



def getLetterAverage(ave):
    if ave>=89.5:
        letter="A"
    elif ave >=79.5:
        letter="B"
    elif ave >=69.5:
        letter="C"
    elif ave >=59.5:
        letter="D"
    else:
        letter="F"
    return letter    
    
def DusplayResults(n,t,a,l):
    print("Number of grades: ",n)
    print("Grade Total: ",t)
    print("Grade Average: ",a)
    print("Letter Grade: ",l)









main()
