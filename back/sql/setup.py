import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'epikodi'

def setupDatabase():
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'connection_timeout': 300,
        'autocommit': True
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
        print(f"Database {DB_NAME} created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database {DB_NAME} already exists.")
        else:
            print(err)
            exit(1)

    cursor.execute(f"USE {DB_NAME}")

    tables = {}

    # MOVIES
    # id, title, year, rating, genres, duration, synopsis, poster, banner, trailer, actors, created_at, updated_at
    tables['movies'] = (
        "CREATE TABLE movies ("
        "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
        "title VARCHAR(255) DEFAULT NULL,"
        "year INT DEFAULT NULL,"
        "rating DECIMAL(3, 1) DEFAULT NULL,"
        "genres TEXT DEFAULT NULL,"
        "duration INT DEFAULT NULL,"
        "synopsis TEXT DEFAULT NULL,"
        "poster TEXT DEFAULT NULL,"
        "banner TEXT DEFAULT NULL,"
        "trailer TEXT DEFAULT NULL,"
        "actors TEXT DEFAULT NULL,"
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
        "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
        ") ENGINE=InnoDB"
    )

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Table {table_name} already exists.")
            else:
                print(err.msg)
        else:
            print("OK")