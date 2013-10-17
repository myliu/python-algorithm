import os, sys
os.environ['PYTHONINSPECT'] = 'True'

def fib(x):
    if (x == 0) or (x == 1):
	return x
    a = 0
    b = 1
    for i in range(x - 1):
	c = a + b
        a = b
        b = c
        print "b: {!r}".format(b)
    return b

if __name__ == '__main__':
    if (len(sys.argv) != 2):
	print "Print provide only 1 argument"
    else:
    	input = int(sys.argv[1])
    	print fib(input)
