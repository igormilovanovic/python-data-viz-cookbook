datafile = 'ch02-data-dirty.tab'

with open(datafile, 'r') as f:
    for line in f:
        # remove next comment to see line before cleanup
        # print 'DIRTY: ', line.split('\t')

        # we remove any space in line start or end 
        line = line.strip() 
        # now we split the line by tab delimiter
        print line.split('\t')  
