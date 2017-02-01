def three_sum(A, B, C, target):
    results = []
    for a in A:
        left, right = 0, len(C) - 1
        while left < len(B) and right >= 0:
            _sum = B[left] + C[right]
            if a + _sum == target:
                results += (a, B[left], C[right]),
                left += 1
                right -= 1
            elif a + _sum > target:
                right -= 1
            else:
                left += 1
    return map(list, set(tuple(sorted(result)) for result in results))

A = [0, 1, 2]
B = [-2,-1, 0]
C = [-1, 0, 2]
target = 0
print three_sum(A, B, C, target)