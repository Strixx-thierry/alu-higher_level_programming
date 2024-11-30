#!/usr/bin/python3
""" displaying all of the cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ starts a connection to the database"""
    with MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )as s:
        cur = s.cursor()
        cur.execute(
                "SELECT * FROM states ORDER BY id ASC"
            )
        all_states = cur.fetchall()
        for each_state in all_states:
            print(each_state)
        cur.close()
        