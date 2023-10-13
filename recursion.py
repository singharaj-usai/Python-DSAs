def countdown(value):
    if (value > 0):
        print(value)
        return countdown(value - 1)
    else:
        return value

countdown(10)
