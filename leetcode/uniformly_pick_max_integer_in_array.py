import random

def get_index_of_max_value_from_array(A):
    max_value = A[0]
    max_count = 1
    j = 0 # saved index to return
    for i in range(1, len(A)):
        if A[i] > max_value:
            max_value = A[i]
            max_count = 1
            j = i
        elif A[i] == max_value:
            max_count += 1
            if random.randint(0, max_count) == 0:
                j = i # lucky winner
    return j

A = [0, -1, 6, 2, 6, 6]
print get_index_of_max_value_from_array(A)