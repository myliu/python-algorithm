def three_sum(A, B, C, target):
    results = []
    for a in A:
        left, right = 0, len(C) - 1
        while left < len(B) and right >= 0:
            if a + B[left] + C[right] == target:
                results += (a, B[left], C[right]),
                left += 1
                right -= 1
            elif a + B[left] + C[right] > target:
                right -= 1
            else:
                left += 1
    return results

A = [0, 1, 2]
B = [-2,-1, 0]
C = [-1, 0, 2]
target = 0
print three_sum(A, B, C, target)