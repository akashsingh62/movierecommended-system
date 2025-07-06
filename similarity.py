import os
import pickle
import requests

def download_and_load_similarity():
    url = "https://drive.google.com/file/d/10E2cedXTDUynyK0WqEUB86n2QP1Mvlf3/view?usp=drive_link"
    filename = "similarity.pkl"

    # Agar file pehle se nahi hai to download karo
    if not os.path.exists(filename):
        print("📦 Downloading similarity.pkl ...")
        r = requests.get(url)

        # ⚠️ Check karo ki HTML page to nahi aa raha
        content_type = r.headers.get('Content-Type', '')
        if "text/html" in content_type:
            with open("error_response.html", "w", encoding="utf-8") as f:
                f.write(r.text)
            raise Exception("❌ ERROR: Got HTML instead of .pkl file. Link ya permission sahi check karo!")

        # ✅ Save correct file
        with open(filename, "wb") as f:
            f.write(r.content)
        print("✅ Download complete!")

    # 📦 Load karo similarity.pkl file
    with open(filename, "rb") as f:
        similarity = pickle.load(f)
    return similarity
