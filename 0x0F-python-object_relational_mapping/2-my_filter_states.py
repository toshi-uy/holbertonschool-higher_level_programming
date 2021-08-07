#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

if (__name__ == "__main__"):
    import MySQLdb
    from sys import argv

    USER = argv[1]
    PASSWRD = argv[2]
    DATABASE = argv[3]
    SEARCH = argv[4]
    connect = MySQLdb.Connect(host="localhost", user=USER,
                              passwd=PASSWRD, db=DATABASE, port=3306,
                              charset="utf8")
    cursor = connect.cursor()
    tx = "SELECT * FROM states WHERE BINARY\
 name = '{}' ORDER BY id".format(SEARCH)
    cursor.execute(tx)
    querry = cursor.fetchall()
    for line in querry:
        print(line)
    cursor.close()
    connect.close()
