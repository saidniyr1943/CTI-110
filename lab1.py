#Rustambek Saidniyozov  1/16/2026
#CSC131-001
#
#Purpose of the following 3 programs are to help with basic calculation with exponents
#Variables are power, base and result







########################################################
print("Problem A")
print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print(2 ** 5)
print(2 ** 6)
print(2 ** 7)
########################################################
print("Problem B")
power=int(input("what power of two?"))
result=2**power
print("Two to the power of ", power, "is",result)
########################################################
print("Problem C")
base=int(input("what base?"))
power=int(input("what power of " + str(base)+"?"))
result=base**power
print(base, "raised to the power of ",power,"is",result)
print("End")
########################################################
