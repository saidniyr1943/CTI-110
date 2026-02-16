#Rustambek Saidniyozov  2/16/2026
#CSC131-001

#Problem 1:Program uses nested for loops to print a multiplication table from 1 to 10.
print("Problem 1")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()


#Problem 2:program uses nested while loops to print a multiplication table from 1 to 10.
print("Problem 2")
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i*j:4}", end=" ")
        j += 1
    print()
    i += 1

#Problem 3:program uses nested for loops to print a growing star pattern based on user input.
print("Problem 3")
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

#Problem 4:Program uses nested while loops to print a growing star pattern based on user input
print("Problem 4")
rows = int(input("Enter number of rows: "))

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
print()
#Problem 5:Program uses nested loops to print each name in a list five times
print("Problem 5")
names = ["Kelly", "Jessa", "Emma"]

for name in names:          
    for i in range(5):      
        print(name, end=" ")
    print()
print()
#Problem 6:Program uses nested loops to add every number in one list to every number in another list and store all the results.
print("Problem 6")
first = [2, 3, 4]
second = [20, 30, 40, 50]

f_list = []

for i in first:
    for j in second:
        f_list.append(i + j)

print(f_list)
print("Finish")
