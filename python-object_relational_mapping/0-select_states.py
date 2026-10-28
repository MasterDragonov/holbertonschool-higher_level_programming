#!/usr/bin/env python3

import MySQLdb
import sys

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()