# 🎬 TMDB CLI Tool
***

A simple and powerful Command Line Interface (CLI) application built using Python that fetches movie data from The Movie Database (TMDB) API and displays it directly in your terminal.

This project helps you practice:
* API integration
* CLI development
* JSON handling
* Error handling
* Clean project structuring

## 🚀 Features
***

* Fetch Now Playing movies
* Fetch Popular movies
* Fetch Top Rated movies
* Fetch Upcoming movies
* Clean terminal output
* Graceful error handling

## 📂 Project Structure
***
```
tmdb-cli/
│
├── tmdb_app.py        # Main CLI application
├── api.py             # API handling logic
├── config.py          # API key and base configuration
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

## 🧠 Prerequisites
***

* Python 3.8+
* TMDB API Key
* Basic terminal knowledge

## 🔑 Get TMDB API Key
***

1. Go to 👉 https://www.themoviedb.org/
2. Create an account
3. Navigate to Settings → API
4. Generate an API key

## 🔐 Set Environment Variable
***

### Linux / macOS
```bash
export TMDB_API_KEY="your_api_key_here"
```

### Windows (PowerShell)
```powershell
setx TMDB_API_KEY "your_api_key_here"
```

**Note:** Restart the terminal after setting it.

## 📦 Installation
***

Clone the repository:
```bash
git clone https://github.com/your-username/tmdb-cli.git
cd tmdb-cli
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Usage
***

Run the CLI using:
```bash
python tmdb_app.py --type <movie_type>
```

### Available movie types:
* `playing` → Now Playing
* `popular` → Popular Movies
* `top` → Top Rated
* `upcoming` → Upcoming Movies

### Examples:
```bash
python tmdb_app.py --type popular
python tmdb_app.py --type top
python tmdb_app.py --type playing
python tmdb_app.py --type upcoming
```

## 📺 Sample Output
***
```
1. Oppenheimer (2023-07-19)
   Rating: 8.4
----------------------------------------
2. Barbie (2023-07-21)
   Rating: 7.3
----------------------------------------
```

## ⚠️ Error Handling
***

The application handles:
* Invalid movie type
* Missing API key
* Network/API failures

You'll receive meaningful error messages instead of crashes.

## 📚 Technologies Used
***

* Python
* Requests library
* TMDB API
* argparse

## 📸 Screenshots
![WhatsApp Image 2025-12-28 at 9 11 15 PM](https://github.com/user-attachments/assets/2a04fd8d-6a6d-409d-beb8-2ce6737255a3)
![WhatsApp Image 2025-12-28 at 9 11 44 PM](https://github.com/user-attachments/assets/da716fc8-924b-4f85-a6ac-e95b4de9540f)
![WhatsApp Image 2025-12-28 at 9 12 16 PM](https://github.com/user-attachments/assets/e4d96f59-465e-4631-b835-db95e25f2efd)
![WhatsApp Image 2025-12-28 at 9 12 41 PM](https://github.com/user-attachments/assets/6f6282bb-beda-4cc0-865d-500e3cfb3a9d)





## 🧪 Future Improvements
***

* Search movies by name
* Pagination support
* Colored terminal output
* Export results to JSON
* Convert to installable CLI (`pip install`)
* Add unit tests


## ⭐ Support
***
If you like this project, consider giving it a ⭐ on GitHub and sharing it with others!

Happy coding 🚀
