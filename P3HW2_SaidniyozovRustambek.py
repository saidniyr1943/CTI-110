#Saidniyozov Rustambek
#P3HW2
# 3/21/2024
# This program calculates emplyee's gross pay.



employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))
if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
else:
        regular_hours = hours_worked
        overtime_hours = 0
        regular_pay = regular_hours * pay_rate
        overtime_pay = 0
        gross_pay = regular_pay
print("----------------------------------------")
print("\nEmployee Name:", employee_name)
print("----------------------------------------")
print("Pay Rate    Hours Worked    Overtime Hours   Overtime Pay   Pay for Regular Hours    Gross Pay")


print(f'{pay_rate:<15.2f}{hours_worked:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<26.2f}{gross_pay:<60.2f}')
     















