#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

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
    tx = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN\
 states ON cities.state_id = states.id"
    cursor.execute(tx)
    querry = cursor.fetchall()
    for line in querry:
        print(line)
    cursor.close()
    connect.close()
