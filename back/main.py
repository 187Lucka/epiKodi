from fastapi import FastAPI

from middlewares.middleware import setupMiddlewares
from routes.default import router as default_router
from scraper.movies import get_top_movies
from sql.setup import setupDatabase
from sql.insert import insertItem
from sql.connection import getDataBaseConnection

from routes.home import router as home_router
from routes.id import router as id_router
from routes.rand import router as rand_router
from routes.movies import router as movies_router
from routes.resolution import router as resolution_router 

app = FastAPI()

setupMiddlewares(app)

app.include_router(default_router)
app.include_router(home_router)
app.include_router(id_router)
app.include_router(rand_router)
app.include_router(movies_router)
app.include_router(resolution_router)

setupDatabase()

@app.on_event("startup")
def startup_event():
    print("Starting up...")
    top_movies = get_top_movies("API-KEY", days=365, max_results=200, min_rating=7.0, min_votes=500)
    for movie in top_movies:
        print(
            f"Title: {movie['title']}\n"
            f"Year: {movie['year']}\n"
            f"Rating: {movie['rating']}\n"
            f"Genres: {', '.join(movie['genres'])}\n"
            f"Duration: {movie['duration']} minutes\n"
            f"Synopsis: {movie['synopsis']}\n"
            f"Poster: {movie['poster']}\n"
            f"Banner: {movie['banner']}\n"
            f"Trailer: {movie['trailer']}\n"
            f"Actors: {', '.join(movie['actors'])}\n"
            "-----------------------\n"
        )

        with getDataBaseConnection() as (cnx, cursor):
            insertItem(
                cnx,
                cursor,
                movie['title'],
                movie['year'],
                movie['rating'],
                ', '.join(movie['genres']),
                movie['duration'],
                movie['synopsis'],
                movie['poster'],
                movie['banner'],
                movie['trailer'],
                ', '.join(movie['actors'])
            )
    print("Inserted successfully.")

