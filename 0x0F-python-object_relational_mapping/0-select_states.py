#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    MY_H = "localhost"
    MY_U = argv[0]
    MY_PS = argv[1]
    MY_DB = argv[2]
    connect = MySQLdb.connect(host=MY_H, user=MY_U,
                              passwd=MY_PS, db=MY_DB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    querry = cursor.fetchall()
    for line in querry:
        print(line)
    cursor.close()
    connect.close()
