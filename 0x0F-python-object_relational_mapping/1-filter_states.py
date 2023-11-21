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
        try:
            cur = conn.cursor()
            quary = "SELECT id, name FROM states WHERE CONVERT(name USING Latin1)"
            quary += " COLLATE Latin1_General_CS LIKE 'N%'"
            quary += "ORDER BY id ASC"
            cur.execute(quary)

            rows = cur.fetchall()

            for row in rows:
                print(row)
        finally:
            cur.close()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
