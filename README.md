# 🎬 Movie Recommendation System

A Streamlit-powered web app to recommend movies similar to a given title, complete with poster images and a preference for recent releases. This project uses scikit-learn, pandas, the TMDB API, and modern Python best practices.

---

## 🚀 Features

* **Content-Based Recommendations:** Finds similar movies using vectorized metadata (`overview`, `genres`, etc.) and cosine similarity.
* **Poster Retrieval:** Fetches movie posters via TMDB API, with a fallback to a placeholder when unavailable.
* **Modern UI:** Sleek, responsive Streamlit interface with custom HTML/CSS.
* **Recent Movie Preference:** Prioritizes newer movies (2010 and above) in results.
* **Robust Error Handling:** Gracefully manages missing data, API issues, and user input edge cases.

---

## 📸 Demo

![Demo Screenshot](https://via.placeholder.com/800x400?text=TMDB+Movie+Recommender)

---

## 📦 Getting Started

### ✅ Prerequisites

* Python 3.8+
* pip
* A TMDB API Key ([Get it here](https://www.themoviedb.org/documentation/api))

### 🔧 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/tmdb-movie-recommender.git
   cd tmdb-movie-recommender
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create your `.env` file:**

   ```env
   TMDB_API_KEY=your_tmdb_api_key_here
   ```

4. **(Optional) Generate similarity matrix:**

   ```bash
   python generate_similarity.py
   ```

   This will create `similarity.pkl` and update your `movies.csv`.

5. **Run the app:**

   ```bash
   streamlit run app.py
   ```

   The app runs on [http://localhost:8501](http://localhost:8501) by default.

---

## 📁 File Structure

```
.
├── app.py                  # Main Streamlit app
├── generate_similarity.py  # Script to compute similarity
├── .env                    # Environment file for TMDB API key
├── data/
│   ├── movies.csv          # Input/output movie dataset
│   └── similarity.pkl      # Cosine similarity matrix
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🧠 Usage

* Enter a movie name in the Streamlit UI and click **Recommend**.
* You'll see 5 similar movies with posters.
* If the title isn’t found, a placeholder is shown.

---

## 🛠 Customizing

* **Dataset:** You can use any CSV with `title`, `overview`, and `genres`.
* **Recommendation Logic:** Tweak `recommend()` in `app.py` to refine logic.
* **UI:** Modify HTML/CSS in the `st.markdown()` sections for custom look and feel.

---

## 🔐 API Key Security

Never commit your TMDB API key. Use `.env` to keep it private and `.gitignore` to exclude it from version control.

```bash
# .gitignore
.env
*.pkl
__pycache__/
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open issues for feedback or bugs.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* [TMDB API](https://www.themoviedb.org/documentation/api)
* [Streamlit](https://streamlit.io/)
* [scikit-learn](https://scikit-learn.org/)
* [pandas](https://pandas.pydata.org/)

---

**🎉 Happy building and movie discovering! 🍿**
