arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]


# TODO: Complete the linearSearchMultipleElements function below.
def linearSearchMultipleElements(array, element):
    elemIndexes = []

    # loop the array
    for index in range(len(array)):
        # check to see if the array is equal to the element
        if array[index] == element:
            elemIndexes.append(index)

            if len(elemIndexes) == 0:
                return "Not Found!"
            else:
                return elemIndexes

print(linearSearchMultipleElements(arr, 7))
