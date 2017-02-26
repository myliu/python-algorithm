def hilbertCurve(x, y, iter):
    if iter == 0:
        return 1

    len = 1 << (iter - 1)
    num = 1 << (2 * (iter - 1))

    if x >= len and y >= len:
        # 3 Shape is identical with previous iteration
        return 2 * num + hilbertCurve(x - len, y - len, iter - 1)
    elif x < len and y >= len:
        # 2 Shape is identical with previous iteration
        return num + hilbertCurve(x, y - len, iter - 1)
    elif x < len and y < len:
        # 1 Flip diagonally
        return hilbertCurve(y, x, iter - 1)
    else:
        # 4 Flip diagonally
        return 3 * num + hilbertCurve(len - 1 - y, 2 * len - 1 - x, iter - 1)

print hilbertCurve(1, 1, 2) # 3
print hilbertCurve(0, 1, 1) # 2
print hilbertCurve(2, 2, 2) # 9
print hilbertCurve(1, 0, 2) # 2
print hilbertCurve(2, 0, 2) 