#Creaing our own functions

seq=[4,7,8,7,5,10]
result=sum(seq)
print(result)

#########################################
def happyBirthdayempty():
    print("Happy birthday to you.")
    print("Happy birthday to you.")
    print("Happy birthday,dear....")
    print("Happy birthday to you.")
happyBirthdayempty()

print()

############################
#f string or can you + to elimimate the space after the name
def happyBirthday(name):
    print("Happy birthday to you.")
    print("Happy birthday to you.")
    print(f"Happy birthday,dear {name}.")
    print("Happy birthday to you.")
def header(name):
    print(60*"*")
    print(f"{name:^60}")
    print(60*"*")


#add value function
def add(num1,num2):
    num=num1+num2
    return(num)
def main():
    header("happy Birthday")
    header("Tony")
    happyBirthday("Tony")
    happyBirthday("Anthony")
    happyBirthday("Antonio")
    header("add")
    n1=int(input("First value:"))
    n2=int(input("Second value:"))         
    print(add(n1,n2))
    
main()





