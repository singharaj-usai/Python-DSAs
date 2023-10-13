arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]


# TODO: Complete the linearSearch function below.
def linearSearch(array, element):
    for index in range(len(array)):
        if array[index] == element:
            return index

    return -1


print(linearSearch(arr, 77))
