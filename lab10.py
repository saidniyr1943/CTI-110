#Rustambek Saidniyozov  2/9/2026
#CSC131-001

#Problem 1 and 2: Calculates and displays a teacher’s yearly salary schedule based on a starting salary, percentage increase, and number of years.
#Problem 1
#while loop
start = float(input("Please enter the start Salary: $"))
increase = float(input("Please enter the % increase: %"))
years = int(input("Please enter the number of years in the schedule: #"))

print("Year #   Salary")
print("------   --------")

salary = start
year = 1

while year <= years:
    print(f"{year:<8} {salary:.2f}")
    
    if year < 10:  
        salary = salary * (1 + increase / 100)
    
    year += 1
print()

#Problem 2
#for loop
start = float(input("Please enter the start Salary: $"))
increase = float(input("Please enter the % increase: %"))
years = int(input("Please enter the number of years in the schedule: #"))

print("Year #   Salary")
print("------   --------")

salary = start

for year in range(1, years + 1):
    print(f"{year:<8} {salary:.2f}")
    
    if year < 10:  
        salary = salary * (1 + increase / 100)
print()

#Problem 3 and 4: Approximates the value of π/4 using the Leibniz series for a user-specified number of iterations.
#Problem 3
#while loop
iterations = int(input("Please the number of iteration: "))

total = 0.0
i = 0
denominator = 1
sign = 1

while i < iterations:
    total += sign * (1 / denominator)
    denominator += 2
    sign *= -1
    i += 1

print(f"{total:.5f}")
print()

#Problem 4
#For loop
iterations = int(input("Please the number of iteration: "))

total = 0.0
denominator = 1
sign = 1

for i in range(iterations):
    total += sign * (1 / denominator)
    denominator += 2
    sign *= -1

print(f"{total:.5f}")
print("finish")
