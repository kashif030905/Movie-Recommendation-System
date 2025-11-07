import pandas as pd

# 1️⃣ Load Ratings
ratings = pd.read_csv('ml-100k/u.data', 
                      sep='\t', 
                      names=['user_id', 'movie_id', 'rating', 'timestamp'])

# 2️⃣ Load Movies + Genres
movies = pd.read_csv('ml-100k/u.item', 
                     sep='|', 
                     encoding='latin-1', 
                     names=[
                         'movie_id','title','release_date','video_release','IMDb_URL',
                         'unknown','Action','Adventure','Animation','Children','Comedy',
                         'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror',
                         'Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western'
                     ])

# Keep only relevant columns
movies = movies[['movie_id','title','Action','Adventure','Animation','Children','Comedy',
                 'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical',
                 'Mystery','Romance','Sci-Fi','Thriller','War','Western']]

# 3️⃣ Merge Ratings with Movies
data = pd.merge(ratings, movies, on='movie_id')

# 4️⃣ Load User Info (optional)
users = pd.read_csv('ml-100k/u.user', 
                    sep='|', 
                    names=['user_id','age','gender','occupation','zip_code'])

# 5️⃣ Merge User Info (optional)
data = pd.merge(data, users, on='user_id')

# 6️⃣ Create a per-user list of watched movies and favorite genres
# Example: Count genre preferences per user
genre_cols = ['Action','Adventure','Animation','Children','Comedy','Crime','Documentary',
              'Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance',
              'Sci-Fi','Thriller','War','Western']

# Calculate the sum of genre flags per user
user_genres = data.groupby('user_id')[genre_cols].sum()

# Create a list of movies watched per user
user_movies = data.groupby('user_id')['title'].apply(list)

# Merge movies list and genre preferences
user_profile = pd.merge(user_movies, user_genres, left_index=True, right_index=True)
user_profile.reset_index(inplace=True)

# 7️⃣ Save merged data and user profile to Excel
data.to_excel('movielens100k_full.xlsx', index=False)        # full dataset
user_profile.to_excel('user_genre_profile.xlsx', index=False) # per-user genre profile

print("✅ Excel files created: movielens100k_full.xlsx and user_genre_profile.xlsx")
