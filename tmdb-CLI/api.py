import requests
from config import TMDB_API_KEY, BASE_URL

ENDPOINTS = {
    "playing": "/movie/now_playing",
    "popular": "/movie/popular",
    "top": "/movie/top_rated",
    "upcoming": "/movie/upcoming"
}


def fetch_movies(movie_type):
    if movie_type not in ENDPOINTS:
        raise ValueError("Invalid movie type")

    url = f"{BASE_URL}{ENDPOINTS[movie_type]}"
    params = {"api_key": TMDB_API_KEY}

    response = requests.get(url, params=params, timeout=10)

    # response = requests.get(f"{BASE_URL}{ENDPOINTS[movie_type]}?api_key={TMDB_API_KEY}")

    if response.status_code != 200:
        raise Exception("Failed to fetch data from TMDB")

    return response.json()["results"]
