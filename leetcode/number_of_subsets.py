PMOD = 1000007

def numberOfSubsets(a, k):
    # Sort the array
    n = len(a)
    a.sort()

    # Precompute the powers of two modulo PMOD
    pow2 = [1 for i in range(n)]
    for i in range(1, n):
        pow2[i] = (pow2[i-1] * 2) % PMOD

    # For every index i, move the index j to the left
    i, j = 0, n-1
    count = 0
    while j >= i:
        while j >= i and a[i] + a[j] > k:
            j -= 1
        if j >= i:
        count = (count + pow2[j-i]) $ PMOD
        i += 1

    return count