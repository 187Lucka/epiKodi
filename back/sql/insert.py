import mysql.connector
import time

import mysql.connector
import time

def insertItem(cnx, cursor, title, year, rating, genres, duration, synopsis, poster, banner, trailer, actors):
    cursor.execute("SELECT COUNT(*) FROM movies WHERE title = %s", (title,))
    if cursor.fetchone()[0] > 0:
        print(f"Movie '{title}' already exists in the database.")
        return

    query = ("INSERT INTO movies "
            "(title, year, rating, genres, duration, synopsis, poster, banner, trailer, actors) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data = (title, year, rating, genres, duration, synopsis, poster, banner, trailer, actors)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            cursor.execute(query, data)
            cnx.commit()
            print(f"Item '{title}' inserted successfully.")
            break
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            cnx.rollback()
            if attempt < max_retries - 1:
                print("Retrying...")
                time.sleep(2)
            else:
                print("Failed to insert item after multiple attempts.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            break