class Contact(object):
    def __init__(self, name, emails):
        self.name = name
        self.emails = emails

from collections import defaultdict

def dfs(edges, contact, seen, found=None):
    found = found or []
    if contact not in seen:
        seen.add(contact)
        found += contact,
        for email in contact.emails:
            for other in edges[email]:
                dfs(edges, other, seen, found)
    return found

def deduplicate(contacts):
    edges = defaultdict(list)
    for contact in contacts:
        for email in contact.emails:
            edges[email] += contact,
    seen = set()
    return filter(None, [dfs(edges, contact, seen) for contact in contacts])

a = Contact('a', ['a@qc.com', 'a@gmail.com'])
b = Contact('b', ['b@qc.com'])
c = Contact('c', ['a@qc.com', 'a@yahoo.com'])

results = deduplicate([a, b, c])
for result in results:
    print 'Contact:'
    for c in result:
        print c.name

"""
Contact:
a
c
Contact:
b
"""