#Rustambek Saidniyozov  3/19/2026
#CSC131-001


def mySum(data):
    """Problem 1: Returns the sum of all values in a list or tuple."""
    total = 0
    for num in data:
        total = total + num
    return total


def myMin(data):
    """Problem 2: Returns the minimum value in a list or tuple."""
    first = True
    for num in data:
        if first:
            minimum = num
            first = False
        elif num < minimum:
            minimum = num
    return minimum


def myMax(data):
    """Problem 3: Returns the maximum value in a list or tuple."""
    first = True
    for num in data:
        if first:
            maximum = num
            first = False
        elif num > maximum:
            maximum = num
    return maximum


def myAvg(data):
    """Problem 4: Returns the average of all values in a list or tuple."""
    total = 0
    count = 0
    for num in data:
        total = total + num
        count = count + 1
    return total / count


def myMinMaxSumAvg(data):
    """Problem 5: Returns min, max, sum, and average of values using previous functions."""
    minimum = myMin(data)
    maximum = myMax(data)
    total = mySum(data)
    average = myAvg(data)
    return (minimum, maximum, total, average)


def modList(data, threshold):
    """Problem 6: Modifies the original list by setting values above threshold to 0."""
    index = 0
    for num in data:
        if num > threshold:
            data[index] = 0
        index = index + 1


def modList2(data, threshold):
    """Problem 7: Returns a new list with values above threshold replaced by 0 without changing original."""
    new_list = []
    for num in data:
        if num > threshold:
            new_list.append(0)
        else:
            new_list.append(num)
    return new_list


def main():
    """Main: Tests all functions with data."""
    
    nums = [3, 5, 7, 2, 9, 6, 2]
    print("Sum:", mySum(nums))
    print("Min:", myMin(nums))
    print("Max:", myMax(nums))
    print("Avg:", myAvg(nums))
    print("MinMaxSumAvg:", myMinMaxSumAvg(nums))

    # Test modList
    test1 = [10, 5, 2, 4, 4, 7, 3]
    modList(test1, 5)
    print("After modList:", test1)

    # Test modList2
    test2 = [21, 12, 4, 30, 48, 26, 111]
    new_test2 = modList2(test2, 9)
    print("Original:", test2)
    print("New list:", new_test2)


main()
    
