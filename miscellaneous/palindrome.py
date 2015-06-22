import os, sys
os.environ['PYTHONINSPECT'] = 'True'

def isPalindrome(input):
    """
    This is extended slice syntax. It works by doing [begin:end:step] - 
    by leaving begin and end off and specifying a step of -1, it reverses a string.
    """
    return True if input == input[::-1] else False

if __name__ == "__main__":
    input = sys.argv[1]
    if isPalindrome(input):
        # '!r' (apply repr())
        print '{!r} is Palindrome'.format(input)
    else:
        print '{!r} is NOT Palindrome'.format(input)
