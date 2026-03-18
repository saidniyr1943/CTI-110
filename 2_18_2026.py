#Saidniyozov   #CSC-131     #2/18/2026

#Problem 1 : Program is to determine  the integer difference between two integers


first=input("Please enter first number : ")
second=input("Please enter second number : ")
diff=int(first)-int(second)
if diff==0:
    print("zero")
elif diff%2==0:
    print("even")
elif diff%2!=0:
    print("odd")   






#Problem 2 : Program is to calculate the given formula

k = int(input("Please enter the first whole number: "))
m = int(input("Please enter the second whole number: "))
bucket = 0
#while k <= m:
#    bucket+= k/(k+1)
#    k+=1



for n in range (k,m+1):
    bucket+=n/(n+1)
print(f"{bucket:.2f}")




#Problem 3


myList = ['123','546','321','11112']
sumValue = 6
bucket=[]
for item in myList:
    lst=[]
    for i in range(0,len(item), 1):
        lst.append(int(item[i]))
    if sum(lst)== sumValue:
        bucket.append(item)
        
print(bucket)




