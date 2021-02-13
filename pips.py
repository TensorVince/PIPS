#!usr/bin/env python3
import sqlite3

class PIPS:
    def __init__(self, dbPath = "./pipdb.sqlite"):
        self.DBPATH = dbPath

    def PrintTableFromResult(result):
        # iterate over the results to print them
        rows = cur.fetchall()
        for row in rows:
            print()

    def SELECT(self, searchValue, *fields):
        con = None
    
        with sqlite3.connect(self.DBPATH) as con:
            cur = con.cursor()

            # creating SELECT command 
            sqlCmd = f"SELECT package_name, current_version, short_description FROM pipdata WHERE {fields[0]} LIKE ?"
            for fieldIndex in range(1, len(fields)):
                sqlCmd += f" OR {fields[fieldIndex]} LIKE ?"

            # As we search every field for the same term, we
            # need to duplicate the searchterm until we have the same count
            # as sql-fields, to execute the sql-command correctly.
            cur.execute(sqlCmd, [searchValue] * len(fields))

            # determine lengths of columns to format the outputTable correctly
            rows = cur.fetchall()
            for row in rows:
                print(row)
            




import sys
p = PIPS()
p.SELECT(sys.argv[1], "short_description", "long_description")
