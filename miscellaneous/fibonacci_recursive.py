import os, sys
os.environ['PYTHONINSPECT'] = 'True'

def fib(x):
    if (x == 0) or (x == 1):
	return x

    return fib(x - 1) + fib(x - 2)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
	print "Print provide only 1 argument"
    else:
    	input = int(sys.argv[1])
    	print fib(input)
