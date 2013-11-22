#!/usr/bin/env python

import csv

filename = 'ch02-data-write.csv'

# we open file with 'b' flag 
# for compatibility with non-linux users
with open(filename,'wb') as f:
    writer = csv.writer(f)
    for row in range(10):
        writer.writerow([row + 1, '2012-01-%s' % (19 + row)]) 
