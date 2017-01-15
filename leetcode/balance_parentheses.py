def balance(s):
    count = 0
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            if count == 0:
                s[i] = '#'
            else:
                count -= 1

    for i in range(n-1, -1, -1):
        if count == 0:
            break
        if s[i] == '(':
            s[i] = '#'
            count -= 1

    return s.replace('#', '')