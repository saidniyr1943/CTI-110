#Rustambek Saidniyozov  1/16/2026
#CSC131-001
#
#Purpose of the following programs are to complete basic calculation with users input
#Variables are result,a,b,x,y



#######################################
#Problem 1
print("Problem 1")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
result = a / b
print(format(result, ",.3f"))
#######################################
#Problem 2
print("Problem 2")
x = float(input("Enter first float: "))
y = float(input("Enter second float: "))
result = x / y
print(format(result, ",.5f"))
#######################################
#Problem 3
print("Problem 3")
x = float(input("Enter first float: "))
y = float(input("Enter second float: "))
result = x / y
print(format(result, ",.6e"))
#######################################
#Problem 4
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print(a, "+", b, "=", format(a + b, ","))
print(a, "-", b, "=", format(a - b, ","))
print(a, "*", b, "=", format(a * b, ","))
print(a, "/", b, "=", format(a / b, ",.3f"))
print(a, "//", b, "=", format(a // b, ","))
print(a, "%", b, "=", format(a % b, ","))
print(a, "**", b, "=", format(a ** b, ","))
#######################################
#Problem 5
# Wacthed some youtube videos on how to do it properly
print("Problem 5")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("operation |", a, "|", b)
print("----------------------------------")

print("add       |", a, "+", b, "=", format(a + b, ","))
print("sub       |", a, "-", b, "=", format(a - b, ","))
print("mult      |", a, "*", b, "=", format(a * b, ","))
print("div       |", a, "/", b, "=", format(a / b, ",.3f"))
print("int div   |", a, "//", b, "=", format(a // b, ","))
print("modula    |", a, "%", b, "=", format(a % b, ","))
print("exp       |", a, "**", b, "=", format(a ** b, ","))
