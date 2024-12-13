from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def calculate_tfidf(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    return vectorizer, tfidf_matrix

def summarize_text(sentences, tfidf_matrix, top_n=3):
    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    ranked_sentences = [sentences[i] for i in scores.argsort()[-top_n:][::-1]]
    return " ".join(ranked_sentences)
