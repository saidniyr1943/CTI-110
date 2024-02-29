#Saidniyozov Rustambek
#02/29/2024
#P2LAB2
#Trip/fuel calculator depending on your car

car_dict = {
  "Camaro": 18.21,
  "Prius": 52.36,
  "Model S": 110,
  "Silverado": 26
  }
car_list=car_dict
print("The keys in the dictionary are: ")
print(*car_list,sep=",")
print()
vehicle=input("Enter a vehicle to see it mpg: ")
print()
mpg=car_dict[vehicle]
print("The",vehicle,"gets","",mpg,"mpg.")
miles=float(input("How many miles will you drive the " + vehicle + "?"))
gallons=miles/mpg
print(f"{gallons:.2f}gallons(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")


