# 🎬 Movie Recommendation System

A content-based movie recommendation engine that suggests similar movies/TV shows based on genre and description similarity, along with a data preparation pipeline for building user-level genre preference profiles from the MovieLens dataset.

## 📌 Project Overview

This project explores two complementary approaches to movie recommendations:

1. **Content-Based Filtering** — recommends titles similar to a given movie/show using TF-IDF vectorization of combined genre and description text, ranked by cosine similarity.
2. **User Profiling Pipeline** — processes the MovieLens 100k dataset to build per-user watch history and genre preference profiles, laying the groundwork for collaborative/hybrid recommendation approaches.

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and merging |
| Scikit-learn | TF-IDF vectorization, cosine similarity |
| MovieLens 100k dataset | User ratings, movie metadata, genres |
| Netflix Titles dataset | Movie/show descriptions and genres |

## 📁 Project Structure

```
Movie-Recommendation-System/
├── CBP.py                      # Content-based filtering recommender
├── DataMining.py                # MovieLens data merging & user profile builder
├── ml-100k/                     # MovieLens 100k dataset (ratings, movies, users)
├── netflix_titles.csv            # Netflix titles dataset (genres, descriptions)
├── movielens100k_full.xlsx       # Merged ratings + movie + user data
├── user_genre_profile.xlsx       # Per-user genre preference profile
└── README.md
```

## ⚙️ How It Works

### Content-Based Recommender (`CBP.py`)
- Loads the Netflix titles dataset and combines each title's genre (`listed_in`) and description into a single text field.
- Builds a TF-IDF matrix over these combined text fields.
- Computes pairwise cosine similarity between all titles.
- Given a movie/show name, returns the top 10 most similar titles.

### Data Mining Pipeline (`DataMining.py`)
- Loads MovieLens 100k ratings, movie metadata, and user demographic data.
- Merges ratings with movie genres and user info into a single dataset.
- Aggregates genre counts per user to build a genre preference profile.
- Exports both the merged dataset and per-user genre profiles to Excel for further analysis.

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas scikit-learn openpyxl

# Run the content-based recommender
python CBP.py

# Run the data mining / user profiling pipeline
python DataMining.py
```

When running `CBP.py`, you'll be prompted to enter a movie/TV show name and it will print the top 10 similar titles.

## 🚀 Future Improvements

- Combine content-based and collaborative filtering into a hybrid recommender
- Build a simple Streamlit UI for interactive recommendations
- Add evaluation metrics (precision@k, recall@k) to benchmark recommendation quality
- Deploy as a lightweight API endpoint

## 👤 Author

**Syed Kashif Uddin**
B.Tech CSE | VNRVJIET, Hyderabad
