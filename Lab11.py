#Rustambek Saidniyozov  2/16/2026
#CSC131-001
#

#Problem 1
#This program goes through each word in a list and prints every letter in each word on its own line.
S = ['Apple', 'Banana', 'Cherry']

for word in S:
    for letter in word:
        print(letter, end=" ")
    print()   

#Problem 2
#This program uses nested loops to print a table of stars based on the number of rows and columns entered by the user.
row = int(input("row: "))
column = int(input("column: "))

for i in range(row):
    for j in range(column):
        print("*", end=" ")
    print()

#Problem 3
#This program uses nested loops to print the numbers 1 through 100 in a grid with 10 numbers per row and aligned columns.
number = 1

for i in range(10):          
    for j in range(10):
        print(f"{number:3}", end=" ")
        number += 1
    print()    
