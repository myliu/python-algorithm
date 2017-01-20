import re

inp = ['a2', '10a', 'a1b', '1b', 'a10b', 'a', '', 'b', 'a10', '1a', 'a1']

def comp(s):
    result = []
    for m in re.finditer(re.compile('([0-9]+)|([^0-9]+)'), s):
        result += ('s', m.group(2)) if m.group(1) is None else ('i', int(m.group(1))),
    return result

print sorted(inp, key=comp)

"""
[('s', 'a'), ('i', 2)]
[('i', 10), ('s', 'a')]
[('s', 'a'), ('i', 1), ('s', 'b')]
[('i', 1), ('s', 'b')]
[('s', 'a'), ('i', 10), ('s', 'b')]
[('s', 'a')]
[]
[('s', 'b')]
[('s', 'a'), ('i', 10)]
[('i', 1), ('s', 'a')]
[('s', 'a'), ('i', 1)]
['', '1a', '1b', '10a', 'a', 'a1', 'a1b', 'a2', 'a10', 'a10b', 'b']
"""