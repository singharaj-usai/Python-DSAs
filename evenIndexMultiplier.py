arrayIndex = [1, 52, 35, 6, 72, 7, 3, 19, 32, 54, 78, 95, 97]


def evenIndexMultiplier(arr):
    result = []
    for index, number in enumerate(arr):
        if index % 2 == 0:
            result.append(number * 10)
        else:
            result.append(number)
    return result


evenIndexes = evenIndexMultiplier(arrayIndex)
print(evenIndexes)
