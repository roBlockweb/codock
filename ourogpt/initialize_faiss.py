from .utils import initialize_faiss, add_texts_to_index, save_faiss

START_TEXTS = [
    "Artificial intelligence and machine learning",
    "Data science and analytics",
    "Neural networks and deep learning",
    "Large language models and transformers"
]

if __name__ == "__main__":
    index = initialize_faiss()
    add_texts_to_index(START_TEXTS, index)
    save_faiss(index)
    print("FAISS initialized with starter content")
