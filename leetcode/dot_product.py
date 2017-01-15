def dot_product(a, b):
    i = j = result = 0
    while i < len(a) and j < len(b):
        if a[i].index < b[j].index:
            i += 1
        elif a[i].index > b[j].index:
            j += 1
        else:
            result += a[i].value * b[j].value
            i += 1
            j += 1
    return result