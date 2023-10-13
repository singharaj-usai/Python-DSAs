import math

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binarySearch(array, element):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = math.floor((start + end) / 2)

        if array[mid] == element:
            return True
        elif array[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return False


print(binarySearch(arr, 7))
