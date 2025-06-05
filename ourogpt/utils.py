import os
import logging
import requests
from bs4 import BeautifulSoup
import faiss
from sentence_transformers import SentenceTransformer

from .config import Config

# logging setup
logger = logging.getLogger("ourogpt")
if not logger.handlers:
    os.makedirs(os.path.dirname(Config.LOG_PATH), exist_ok=True)
    handler = logging.FileHandler(Config.LOG_PATH)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# embedding model singleton
_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    return _embedding_model

# FAISS helpers

def initialize_faiss(dim=384, path=Config.FAISS_PATH):
    index = faiss.IndexFlatL2(dim)
    faiss.write_index(index, path)
    return index


def load_faiss(path=Config.FAISS_PATH):
    if os.path.exists(path):
        return faiss.read_index(path)
    return initialize_faiss()


def save_faiss(index, path=Config.FAISS_PATH):
    faiss.write_index(index, path)


def add_texts_to_index(texts, index):
    model = get_embedding_model()
    embeddings = model.encode(texts)
    index.add(embeddings)


def search_index(query, index, k=5):
    model = get_embedding_model()
    vec = model.encode([query])
    distances, ids = index.search(vec, k)
    return ids[0]

# scraping helper

def scrape(url):
    try:
        headers = {'User-Agent': Config.USER_AGENT}
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        logger.error(f"scrape failed: {e}")
        return ""
