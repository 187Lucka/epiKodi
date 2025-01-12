from fastapi import APIRouter, HTTPException
from sql.connection import getDataBaseConnection

router = APIRouter()

@router.get("/api/home")
async def home():
    keys = ["id", "title", "year", "rating", "genres", "duration", "synopsis", "poster", "banner", "trailer", "actors", "created_at", "updated_at"]

    with getDataBaseConnection() as (cnx, cursor):
        cursor.execute("SELECT * FROM movies ORDER BY RAND() LIMIT 1")
        random_movie = dict(zip(keys, cursor.fetchone()))

        cursor.execute("SELECT * FROM movies ORDER BY rating DESC LIMIT 10")
        top_rated_movies = [dict(zip(keys, movie)) for movie in cursor.fetchall()]

        cursor.execute("SELECT * FROM movies WHERE genres LIKE '%Action%' ORDER BY RAND() LIMIT 10")
        action_movies = [dict(zip(keys, movie)) for movie in cursor.fetchall()]

        cursor.execute("SELECT * FROM movies WHERE genres LIKE '%Comedy%' ORDER BY RAND() LIMIT 10")
        comedy_movies = [dict(zip(keys, movie)) for movie in cursor.fetchall()]

        cursor.execute("SELECT * FROM movies WHERE genres LIKE '%Horror%' ORDER BY RAND() LIMIT 10")
        horror_movies = [dict(zip(keys, movie)) for movie in cursor.fetchall()]

    return {
        "random": random_movie,
        "top_rated": top_rated_movies,
        "action": action_movies,
        "comedy": comedy_movies,
        "horror": horror_movies
    }