import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Keep only relevant columns
df = df[['title', 'listed_in', 'description']]

# Handle missing values
df.fillna('', inplace=True)

# Combine genre + description for better similarity
df['combined'] = df['listed_in'] + " " + df['description']

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index for proper lookup
df = df.reset_index()

# Function to get movie recommendations
def recommend_movie(title):
    title = title.lower()
    
    # Check if movie exists
    if title not in df['title'].str.lower().values:
        print("❌ Movie not found in dataset. Try another name.")
        return
    
    # Get index of movie
    idx = df[df['title'].str.lower() == title].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort based on similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 10 similar movies (excluding itself)
    sim_scores = sim_scores[1:11]
    
    print(f"\n🎥 Movies/TV Shows similar to '{df.loc[idx, 'title']}':\n")
    for i, score in sim_scores:
        print(f"- {df.loc[i, 'title']}")

# Run dynamic input loop
while True:
    movie_name = input("\nEnter a movie/TV show name (or type 'exit' to quit): ")
    if movie_name.lower() == 'exit':
        print("👋 Exiting Recommendation System.")
        break
    recommend_movie(movie_name)
