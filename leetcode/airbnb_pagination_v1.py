"""
Search result pagination
"""

def pagination(num, results):
    output = []

    while results:
        page = {}
        deferred = []
        i = 0
        while i < len(results):
            entry = results[i]
            tokens = entry.split(',')

            host_id, listing_id, score, city = tokens[0], tokens[1], float(tokens[2]), tokens[3]
            if host_id in page:
                deferred += entry,
            else:
                page[host_id] = (host_id, listing_id, score, city)

            if len(page) == num:
                break

            i += 1

        for host_id, listing_id, score, city in sorted(page.values(), key=lambda x:x[2], reverse=True):
            output += ','.join([host_id, listing_id, str(score), city]),

        results = deferred + results[i+1:]
        if len(page) < num:
            output += results[:num-len(page)]
            results = results[num-len(page):]

        output += '',

    return output

num = 5
results = [
    '1,28,100,SF',
    '4,5,99,SF',
    '20,7,98,SF',
    '6,8,97,SF',
    '6,10,96,SF',
    '1,16,95,SF',
    '7,20,94,SF',
    '2,18,93,SF',
    '3,76,92,SF',
    '6,29,91,SF',
    '2,30,90,SF',
    '2,14,89,SF',
    '6,21,88,SF'
]

print pagination(num, results)