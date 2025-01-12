import requests
from datetime import datetime, timedelta

BASE_URL = "https://api.themoviedb.org/3"

def get_top_movies(api_key, days=30, max_results=50, min_rating=7.0, min_votes=500):
    """
    Récupère les plus gros films récents sur une période donnée.
    
    :param api_key: Votre clé API TMDb
    :param days: Nombre de jours dans le passé pour chercher des films (défaut: 30 jours)
    :param max_results: Nombre maximum de films à récupérer (défaut: 50)
    :param min_rating: Note minimale (défaut: 7.0)
    :param min_votes: Nombre minimum de votes (défaut: 500)
    :return: Liste des plus gros films avec leurs détails
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    movies = []
    page = 1

    while len(movies) < max_results:
        url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": api_key,
            "sort_by": "popularity.desc",
            "release_date.gte": start_date.strftime("%Y-%m-%d"),
            "release_date.lte": end_date.strftime("%Y-%m-%d"),
            "vote_average.gte": min_rating,
            "vote_count.gte": min_votes,
            "with_original_language": "en",
            "page": page,
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Erreur: {response.status_code} - {response.json().get('status_message')}")
            break

        data = response.json()
        results = data.get("results", [])

        for movie in results:
            if len(movies) >= max_results:
                break

            movie_id = movie.get("id")
            movie_details = get_movie_details(api_key, movie_id)
            if movie_details:
                movies.append(movie_details)

        if not data.get("total_pages") or page >= data["total_pages"]:
            break

        page += 1

    return movies


def get_movie_details(api_key, movie_id):
    """
    Récupère les détails d'un film par son ID.
    
    :param api_key: Votre clé API TMDb
    :param movie_id: ID du film
    :return: Dictionnaire contenant les détails du film
    """
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Erreur lors de la récupération des détails du film {movie_id}")
        return None

    movie_data = response.json()

    trailer = get_movie_trailer(api_key, movie_id)

    actors = get_movie_actors(api_key, movie_id)

    return {
        "title": movie_data.get("title"),
        "year": movie_data.get("release_date", "").split("-")[0],
        "rating": movie_data.get("vote_average"),
        "genres": [genre["name"] for genre in movie_data.get("genres", [])],
        "duration": movie_data.get("runtime"),
        "synopsis": movie_data.get("overview"),
        "poster": f"https://image.tmdb.org/t/p/original{movie_data.get('poster_path')}" if movie_data.get("poster_path") else None,
        "banner": f"https://image.tmdb.org/t/p/original{movie_data.get('backdrop_path')}" if movie_data.get("backdrop_path") else None,
        "trailer": trailer,
        "actors": actors,
    }


def get_movie_trailer(api_key, movie_id):
    """
    Récupère le trailer d'un film par son ID.
    
    :param api_key: Votre clé API TMDb
    :param movie_id: ID du film
    :return: URL du trailer YouTube (ou None si non disponible)
    """
    url = f"{BASE_URL}/movie/{movie_id}/videos"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    videos = response.json().get("results", [])
    for video in videos:
        if video["type"] == "Trailer" and video["site"] == "YouTube":
            return f"https://www.youtube.com/watch?v={video['key']}"

    return None


def get_movie_actors(api_key, movie_id):
    """
    Récupère la liste des acteurs d'un film par son ID.
    
    :param api_key: Votre clé API TMDb
    :param movie_id: ID du film
    :return: Liste des acteurs principaux
    """
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    cast = response.json().get("cast", [])
    return [actor["name"] for actor in cast[:10]]
