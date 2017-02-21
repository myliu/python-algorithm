a = [2, 3, 4, 2, 3, 4, 5]
# a = [2, 2, 2, 2, 2]
n = 5
pos = range(1, n+1)
for i in a:
    print i, pos
    try:
        pos.remove(i)
    except:
        pass

    if len(pos) == 0:
        break

    pos = list(set([x + 1 for x in pos if x < n])
            .union(set([x - 1 for x in pos if x > 1])))

print pos