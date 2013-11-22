import time
import os
import sys

if len(sys.argv) != 2:
    print >> sys.stderr, "Please specify filename to read"

filename = sys.argv[1]

if not os.path.isfile(filename):
    print >> sys.stderr, "Given file: \"%s\" is not a file" % filename

with open(filename,'r') as file:
    # Move to the end of file
    filesize = os.stat(filename)[6]
    file.seek(filesize)

    # endlessly loop 
    while True:
        where = file.tell()
        # try reading a line
        line = file.readline()
        # if empty, go back
        if not line:
            time.sleep(1)
            file.seek(where)
        else:
            # , at the end prevents print to add newline, as readline() 
            # already read that.
            print line,
