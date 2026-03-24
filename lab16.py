#Rustambek Saidniyozov  3/23/2026
#CSC131-001


def floor(num):
    """Returns the largest number that is less than or equal to the given number."""
    n = int(num)
    if num < 0 and num != n:
        return n - 1
    return n


def ceil(num):
    """Returns the smallest number greater than or equal to the given number."""
    n = int(num)
    if num > 0 and num != n:
        return n + 1
    return n


def minVal(lst):
    """Returns the smallest value in a list of numbers."""
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest


def maxVal(lst):
    """Returns the largest value in a list of numbers."""
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


def total(lst):
    """Returns the sum of all numbers in a list."""
    result = 0
    for num in lst:
        result += num
    return result


def mean(lst):
    """Returns the average value of numbers in a list."""
    return total(lst) / len(lst)


def sort(seq):
    """Returns a new list with the values sorted from smallest to largest."""
    numbers = list(seq)
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


def median(lst):
    """Returns the middle value of a sorted list of numbers."""
    numbers = sort(lst)
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]


def gcd(a, b):
    """Returns the greatest common divisor of two integers."""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a    
