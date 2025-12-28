import argparse
from api import fetch_movies


def display_movies(movies):
    for idx, movie in enumerate(movies[:10], start=1):
        print(f"{idx}. {movie['title']} ({movie['release_date']})")
        print(f"   Rating: {movie['vote_average']}")
        print("-" * 40)


def main():
    parser = argparse.ArgumentParser(description="TMDB CLI Tool")
    parser.add_argument(
        "--type",
        required=True,
        choices=["playing", "popular", "top", "upcoming"],
        help="Type of movies to display"
    )

    args = parser.parse_args()

    try:
        movies = fetch_movies(args.type)
        display_movies(movies)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
