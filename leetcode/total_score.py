def totalScore(blocks, n):
    if not blocks:
        return 0

    if len(blocks) != n:
        return 0

    # stack is to keep track of the sequence of scores
    stack = []
    # count is to keep track of the total score
    count = 0
    for token in blocks:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            score = int(token)
            count += score
            stack += score,
        elif token == 'X':
            score = stack[-1] * 2
            count += score
            stack += score,
        elif token == '+':
            score = stack[-1] + stack[-2]
            count += score
            stack += score,
        elif token == 'Z':
            count -= stack[-1]
            stack.pop()
        else:
            raise Exception('Invalid Token: {}'.format(token))
        print token, count
    return count

print totalScore(['5', '-2', '4', 'Z', 'X', '9', '+', '+'], 8)