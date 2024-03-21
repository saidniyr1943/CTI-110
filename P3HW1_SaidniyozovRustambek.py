# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

grade_list = []
grade = float(input('Enter grade for Module 1: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 2: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 3: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 4: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 5: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 6: '))
grade_list.append(grade)
print("----------Results----------")

lowest = min(grade_list)
highest = max(grade_list)
sum1 = sum(grade_list)
ave = sum(grade_list)/len(grade_list)


print(f'Lowest Grade:      {lowest:.2f}')
print(f'Highest Grade:     {highest:.2f}')
print(f'Sum of Grades:     {sum1:.2f}')
print(f'Average:           {ave:.2f}')

print("----------------------------")

if ave >= 90:
 print('Your grade is: A')
else:
     if ave >= 80:
        print('Your grade is: B')
     if ave >= 70:
        print('Your grade is: c')
     if ave >= 60:
        print('Your grade is: D')
     if ave >= 50:
        print('Your grade is: F')
     if ave <= 50:
        print('Your grade is: F')





