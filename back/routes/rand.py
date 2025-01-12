from fastapi import APIRouter, HTTPException
from sql.connection import getDataBaseConnection

router = APIRouter()

@router.get("/api/rand/{nbr}")
async def get_random_movies(nbr: int):
    keys = ["id", "title", "year", "rating", "genres", "duration", "synopsis", "poster", "banner", "trailer", "actors", "created_at", "updated_at"]

    with getDataBaseConnection() as (cnx, cursor):
        cursor.execute("SELECT * FROM movies ORDER BY RAND() LIMIT %s", (nbr,))
        random_movies = [dict(zip(keys, movie)) for movie in cursor.fetchall()]

    return random_movies