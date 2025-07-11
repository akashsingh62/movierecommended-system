import streamlit as st
import pandas as pd
import pickle
import requests
import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from similarity import download_and_load_similarity

similarity = download_and_load_similarity()


# Load .env file
load_dotenv()

# Get TMDB API key from environment variable
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Set page config
st.set_page_config(page_title="TMDB Movie Recommendation", layout="centered")

# Apply custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    }
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .movie-title {
        color: #ffcc00;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .movie-card {
        background-color: white;
        color: black;
        border-radius: 10px;
        padding: 10px;
        width: 200px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        text-align: center;
    }
    .movie-card img {
        width: 100%;
        height: 300px;
        border-radius: 8px;
    }
    .movie-card p {
        font-weight: bold;
        margin-top: 10px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
movies = pd.read_csv('movies.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch poster
def fetch_poster(movie_title):
    try:
        from requests.utils import quote
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={quote(movie_title)}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'results' in data and data['results']:
            for result in data['results']:
                poster_path = result.get('poster_path')
                print(f"🔍 Title: {movie_title}, Poster Path: {poster_path}")  # Debug print

                if poster_path:
                    return "https://image.tmdb.org/t/p/w500" + poster_path

        return "https://via.placeholder.com/300x450?text=No+Poster"
    except Exception as e:
        print(f"⚠️ Error fetching poster for {movie_title}: {e}")
        return "https://via.placeholder.com/300x450?text=Error"

# Recommendation function
def recommend(movie):
    movie = movie.lower()
    matched_titles = movies[movies['title'].str.lower().str.contains(movie)]
    if matched_titles.empty:
        return [("Movie not found", "https://via.placeholder.com/300x450?text=Not+Found")]

    idx = matched_titles.index[0]
    distances = list(enumerate(similarity[idx]))
    sorted_movies = sorted(distances, reverse=True, key=lambda x: x[1])

    recommended = []
    count = 0
    for i in sorted_movies:
        title = movies.iloc[i[0]].title
        year = movies.iloc[i[0]].get("year", 2000)
        if year >= 2010 and title.lower() != movie:
            poster = fetch_poster(title)
            recommended.append((title, poster))
            count += 1
        if count == 5:
            break

    if count < 5:
        for i in sorted_movies:
            title = movies.iloc[i[0]].title
            if not any(title == t for t, _ in recommended):
                poster = fetch_poster(title)
                recommended.append((title, poster))
                if len(recommended) == 5:
                    break
    return recommended

# UI
st.markdown('<div class="movie-title">CineMatch Movie Recommendation</div>', unsafe_allow_html=True)

movie_input = st.text_input("", placeholder="Write your movie name here...")


if st.button("Recommend"):
    if movie_input:
        recommendations = recommend(movie_input)
        st.write(f"### You searched for: **{movie_input}**")

        st.markdown("#### Recommended Movies:")
        cols = st.columns(5)
        for i, (title, poster) in enumerate(recommendations):
            with cols[i % 5]:
                st.markdown(
                    f"""
                    <div class="movie-card">
                        <img src="{poster}" alt="{title} poster">
                        <p>{title}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )






















