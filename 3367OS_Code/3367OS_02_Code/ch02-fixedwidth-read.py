import struct
import string

mask='9s14s5s'
parse = struct.Struct(mask).unpack_from
print 'formatstring {!r}, record size: {}'.format(\
                        mask, struct.calcsize(mask))

datafile = 'ch02-fixed-width-1M.data'

with open(datafile, 'r') as f:
    for line in f:
        fields = parse(line)
        print 'fields: ', [field.strip() for field in fields]

