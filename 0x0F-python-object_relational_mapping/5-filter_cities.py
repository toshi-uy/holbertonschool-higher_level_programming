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
    STATE = argv[4]
    connect = MySQLdb.Connect(host="localhost", user=USER,
                              passwd=PASSWRD, db=DATABASE, port=3306,
                              charset="utf8")
    cursor = connect.cursor()
    tx = ("SELECT cities.name FROM cities INNER JOIN " +
          "states ON cities.state_id = states.id WHERE " +
          "states.name = %s ORDER BY cities.id")
    cursor.execute(tx, (STATE,))
    querry = cursor.fetchall()
    result = []
    for line in querry:
        result.append(str(line)[2:-3])
    final = ", ".join(result)
    print(final)
    cursor.close()
    connect.close()
