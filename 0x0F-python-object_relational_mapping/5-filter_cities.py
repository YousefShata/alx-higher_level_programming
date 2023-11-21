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
    search = argv[4]

    try:

        conn = MySQLdb.connect(host="localhost",
                               port=3306, user=user,
                               passwd=password, db=db)
        try:
            cur = conn.cursor()
            quary = "SELECT cities.name FROM cities"
            quary += " JOIN states ON states.id = cities.state_id"
            quary += " WHERE states.name = %s"
            quary += " ORDER BY cities.id"

            cur.execute(quary, (search,))

            rows = cur.fetchall()

            results = []

            for row in rows:
                results.append(row[0])
            print(", ".join(results))
        finally:
            cur.close()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
