#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    HOSTNAME = localhost
    USERNAME = argv[0]
    PASSWORD = argv[1]
    DATABASE = argv[2]
    connect = MySQLdb.connect(host=HOSTNAME, user=USERNAME,
                              passwd=PASSWORD, db=DATABASE, port=3306)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    querry = cursor.fetchall()
    for line in querry:
        print(line)
    cursor.close()
    connect.close()
