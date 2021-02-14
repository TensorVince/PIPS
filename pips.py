#!usr/bin/env python3
import sqlite3

class PIPS:
    def __init__(self, dbPath = "./pipdb.sqlite"):
        self.DBPATH = dbPath

    def PrintTableFromResult(self, headers, rows):

        # iterate over the results to determine col-lengths
        maxLengths = [0] * len(headers)
        for row in rows:
            for col in range(0, len(headers)):
                colLen = len(row[col])
                maxLengths[col] = colLen if colLen > maxLengths[col] else maxLengths[col]

        # Create Table colFormatStrings
        colFormatStrings = []
        for maxLength in maxLengths:
            colFormatStrings.append("{:<" + str(maxLength) + "}")

        # print headers
        for i in range(0, len(colFormatStrings)):
            print(colFormatStrings[i].format(headers[i]), end = " | ")
        print("")
        
        # iterate over the results to print them
        for row in rows:
            for i in range(len(row)):
                print(colFormatStrings[i].format(), end=" | ")
            print("")

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
