from collections import defaultdict

def four_sum(A, B, C, D, target):
    two_sum = defaultdict(list)
    result = []

    for a in A:
        for b in B:
            two_sum[a+b] += (a, b),

    for c in C:
        for d in D:
            if target - c - d in two_sum:
                result += [_sum + (c, d) for _sum in two_sum[target - c - d]]

    return result

A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
target = 0
print four_sum(A, B, C, D, target)