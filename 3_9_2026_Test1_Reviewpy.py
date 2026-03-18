#Test 1 Review

#Problem 1
x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))


if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")    
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")    
else:
    print("Axes")    

#############################################################

#Problem 2

low = int(input("Enter the low value: "))
high = int(input("Enter the high value: "))
for i in range(low,high+1,1):
    if (i%3==0 or i%5==0) and not (i%3==0 and i%5==0):
        print(i)
    
##############################################################

#Problem 3

myList = ['$100','25%','#99','1-2-3','#25%']
newList=[]
for item in myList:
    print(item)
    temp=''
    for subitem in item:
        if subitem in '0123456789':
            temp+=(subitem)
    newList.append(temp)
print(newList)



##############################################################
#PROBLEM 4
str1 = "Listen"
str2 = "Silent"
str1= str1.lower()
str2= str2.lower()

if len(str1 != len(str2)
       print("FALSE")
else:
    for item in str1:
        if str1.count(item) != str2.count(item)):
            print("False")
            break
    print("True")    
       
