"""
Generate a time heatmap for commits to the specified repo.
"""
from collections import Counter
from subprocess import check_output
import sys

repo = sys.argv[1]

counter = Counter()

output = check_output(['/usr/local/bin/git', 'log', '--format=format:%ad','--date=format:%w %H'], cwd=repo)

for line in output.splitlines():
    weekday0, hour23 = line.split(' ')
    data = int(weekday0)+1, int(hour23)+1
    counter.update([data])

keys = []
for d in range(1,8):
    keys.extend((d, h) for h in range(1, 25))
counter.update({k: 0 for k in keys})
with open('data.tsv', 'wb') as outf:
    outf.write("day\thour\tvalue\n")
    for weekday1, hour24 in keys:
        outf.write("%s\t%s\t%s\n" % (weekday1, hour24, counter[(weekday1, hour24)]))
