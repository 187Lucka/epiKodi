from fastapi import APIRouter, HTTPException
from sql.connection import getDataBaseConnection

router = APIRouter()

@router.get("/api/id/{movie_id}")
async def get_movie_by_id(movie_id: int):
    keys = ["id", "title", "year", "rating", "genres", "duration", "synopsis", "poster", "banner", "trailer", "actors", "created_at", "updated_at"]

    with getDataBaseConnection() as (cnx, cursor):
        cursor.execute("SELECT * FROM movies WHERE id = %s", (movie_id,))
        movie = cursor.fetchone()
        if movie is None:
            raise HTTPException(status_code=404, detail="Movie not found")
        movie_dict = dict(zip(keys, movie))

    return movie_dict