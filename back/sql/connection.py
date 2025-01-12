from contextlib import contextmanager
import mysql.connector

@contextmanager
def getDataBaseConnection():
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'epikodi',
        'connection_timeout': 300,
        'autocommit': True
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        yield cnx, cursor
    finally:
        cursor.close()
        cnx.close()
