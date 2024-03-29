#!/usr/bin/python3
"""
ORM model
"""
from sys import argv
import MySQLdb


def main():
    """
    Main function
    """
    user = argv[1]
    password = argv[2]
    db = argv[3]

    try:

        conn = MySQLdb.connect(host="localhost",
                               port=3306, user=user,
                               passwd=password, db=db)
        cur = conn.cursor()

        cur.execute("SELECT id, name FROM states ORDER BY id ASC")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()
    except e:
        pass


if __name__ == "__main__":
    main()
