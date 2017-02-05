def max_seq_in_array(arr):
    length = len(arr)
    mem = []
    ret_max = min(length, 2)
    for i in range(0, length):
        iMem = {}
        mem += iMem,
        for j in range(0, i):
            jMem = mem[j]
            d = arr[i] - arr[j]
            new_len = jMem[d] + 1 if d in jMem else 2
            iMem[d] = new_len
            ret_max = max(ret_max, new_len)
    print mem
    return ret_max

print max_seq_in_array([1, 3, -20, 9, 5, 7])