#Rustambek Saidniyozov
#3/7/2024
#P2HW2
#Grade Calculator

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
print(f'Sum Grade:         {sum1:.2f}')
print(f'Average Grade:     {ave:.2f}')

print("---------------------------")
