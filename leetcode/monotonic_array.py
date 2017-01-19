def is_monotonic(array):
    if not array:
        return True

    n = len(array)
    is_increasing = (array[0] <= array[n-1])
    for i in range(0, n-1):
        if (array[i] != array[i+1]) and (array[i] < array[i+1]) != is_increasing:
            return False
    return True

array = [1, 2, 3, 5]
print is_monotonic(array)