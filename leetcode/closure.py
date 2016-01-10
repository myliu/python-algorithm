# http://www.shutupandship.com/2012/01/python-closures-explained.html

def generate_power_func(n):
    print "id(n): %X" % id(n)
    def nth_power(x):
        return x**n
    print "id(nth_power): %X" % id(nth_power)
    return nth_power

if __name__ == '__main__':
    raise_to_2 = generate_power_func(2)
    print raise_to_2.__closure__[0].cell_contents
    print raise_to_2(5)