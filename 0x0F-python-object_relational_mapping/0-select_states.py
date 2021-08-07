#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

if (__name__ == "__main__"):
    import MySQLdb
    from sys import argv
    HOST = "localhost"
    USER = argv[1]
    PASSWRD = argv[2]
    DATABASE = argv[3]
    connect = MySQLdb.Connect(host=HOST, user=USER, passwd=PASSWRD, db=DATABASE, port=3306)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    querry = cursor.fetchall()
    for line in querry:
        print(line)
    cursor.close()
    connect.close()
