def balance(s):
    lst = list(s)
    count = 0
    n = len(lst)
    for i in range(n):
        if lst[i] == '(':
            count += 1
        elif lst[i] == ')':
            if count == 0:
                lst[i] = '#'
            else:
                count -= 1

    for i in range(n-1, -1, -1):
        if count == 0:
            break
        if lst[i] == '(':
            lst[i] = '#'
            count -= 1

    s = ''.join(lst)
    return s.replace('#', '')

print balance("()())()")
print balance("(a)(()()")