arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]


# TODO: Complete the linearSearch function below.
def linearSearch(array, element):
    # loop the array
    for index in range(len(array)):
        # check to see if the array is equal to the element
        if array[index] == element:
            # exit the search by returning the index
            return index

    # -1 when no matching element is found in the array
    return -1


print(linearSearch(arr, 77))
