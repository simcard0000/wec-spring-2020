import sys
from search import SearchHandler 

query = ''
from_sites = tuple()
ignore_sites = tuple()

# Parse system arguments
for i, x in enumerate(sys.argv):
    if i == 1:
        query = x
    if x.startswith('from_sites'):
        from_sites = tuple(x.split(':')[:-1])
    if x.startswith('ignore_sites'):
        ignore_sites = tuple(x.split(':')[:-1])

# Call search function
handler = SearchHandler()
results = handler.search(query, from_sites=from_sites, ignore_sites=ignore_sites)

print(results)