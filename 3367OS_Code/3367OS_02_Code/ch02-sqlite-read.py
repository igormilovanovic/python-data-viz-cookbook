import sqlite3
import sys

if len(sys.argv) != 2:
    print "Please specify database file."
    sys.exit(1)

db = sys.argv[1]

try:
    con = sqlite3.connect(db)
    with con:
        cur = con.cursor()
        query = 'SELECT ID, Name, Population FROM City ORDER BY Population DESC LIMIT 1000'

        con.text_factory = str
        cur.execute(query)

        resultset = cur.fetchall()

        # extract column names

        col_names = [cn[0] for cn in cur.description] 
        print "%10s %30s %10s" % tuple(col_names)
        print "="*(10+1+30+1+10)

        for row in resultset:
            print "%10s %30s %10s" % row
except sqlite3.Error as err:
    print "[ERROR]:", err
