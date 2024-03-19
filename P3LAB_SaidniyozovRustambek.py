''' Type your code here. '''
#Rustambek Saidniyozov
#3/19/2024
#P3LAB
#Exact change calculator
change_amount = int(input())

if change_amount <= 0:
    print("No change")
else:
    dollars = change_amount // 100
    change_amount %= 100

    quarters = change_amount // 25
    change_amount %= 25

    dimes = change_amount // 10
    change_amount %= 10

    nickels = change_amount // 5
    change_amount %= 5

    pennies = change_amount

    if dollars > 0:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
    if quarters > 0:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
    if dimes > 0:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
    if nickels > 0:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
    if pennies > 0:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")