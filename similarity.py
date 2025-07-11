

import os, pickle, requests

def _get_confirm_token(r):
    for k, v in r.cookies.items():
        if k.startswith("download_warning"):
            return v
    return None

def _save_response(r, dest):
    CHUNK = 32768
    with open(dest, "wb") as f:
        for chunk in r.iter_content(CHUNK):
            if chunk: f.write(chunk)

def download_and_load_similarity():
    file_id = "1opOfUXKqHvnZLd2u3z5l_KmgRbmTVH0n"
    url = "https://docs.google.com/uc?export=download"
    dest = "similarity.pkl"

    if not os.path.exists(dest):
        print("⬇️  Downloading...")
        session = requests.Session()
        resp = session.get(url, params={"id": file_id}, stream=True)
        token = _get_confirm_token(resp)
        if token:  # large file confirm
            resp = session.get(url, params={"id": file_id, "confirm": token}, stream=True)
        _save_response(resp, dest)
        print("✅  Done!")

    with open(dest, "rb") as f:
        return pickle.load(f)
