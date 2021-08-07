#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

if (__name__ == "__main__"):
    import MySQLdb
    from sys import argv

    USER = argv[1]
    PASSWRD = argv[2]
    DATABASE = argv[3]
    connect = MySQLdb.Connect(host="localhost", user=USER,
                              passwd=PASSWRD, db=DATABASE, port=3306,
                              charset="utf8")
    cursor = connect.cursor()
    text = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    cursor.execute(text)
    querry = cursor.fetchall()
    for line in querry:
        print(line)
    cursor.close()
    connect.close()
