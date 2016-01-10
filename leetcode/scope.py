count = [0]
# count cannot be int here

def c(x):
    count[0] += x
    return count[0]

if __name__ == '__main__':
    print map(c, range(5))
    # Output: [0, 1, 3, 6, 10]

'''
http://stackoverflow.com/questions/21456739/unboundlocalerror-local-variable-l-referenced-before-assignment-python

The minimal code to reproduce your bug is

x = 1
def foo():
    x += 1
foo()
This is happening for a number of reasons

First - because in python we have mutable and immutable classes. Ints are immutable, that is when you write x+=1 you actually create another object (which is not true for certain ints due to optimisations CPython does). What actually happens is x = x + 1.
Second - because python compiler checks every assignment made inside a scope and makes every variable assigned inside that scope local to it.
So as you see when you try to increment x compiler has to access a variable that's local to that scope, but was never assigned a value before.
'''