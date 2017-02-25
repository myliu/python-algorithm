from math import floor

def roundNumbers(input):
    output = map(lambda x: floor(x), input)
    print output
    remain = int(round(sum(input) - sum(output)))
    print remain

    it = sorted(enumerate(input), key=lambda i: i[1] - floor(i[1]))
    print it
    for _ in range(remain):
        output[it.pop()[0]] += 1

    return output

A = [1.2, 2.3, 3.4, 4.2]
print roundNumbers(A)