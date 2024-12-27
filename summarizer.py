from sklearn.feature_extraction.text import TfidfVectorizer
from rouge_score import rouge_scorer
import numpy as np

def calculate_tfidf(sentences):
    """
    Menghitung TF-IDF untuk daftar kalimat.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    return vectorizer, tfidf_matrix

def summarize_text(sentences, tfidf_matrix, top_n=3):
    """
    Membuat ringkasan berdasarkan skor TF-IDF.
    """
    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    ranked_sentences = [sentences[i] for i in scores.argsort()[-top_n:][::-1]]
    return " ".join(ranked_sentences)

def evaluate_summary(generated_summary, reference_summary):
    """
    Mengevaluasi ringkasan menggunakan metrik ROUGE.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_summary, generated_summary)
    return scores

# Contoh penggunaan
sentences = [
    "Natural language processing is a field of artificial intelligence.",
    "It enables computers to understand human language.",
    "Applications include language translation and sentiment analysis.",
    "TF-IDF is a statistical measure used in text analysis.",
    "It evaluates the importance of a term relative to a document."
]
reference_summary = "TF-IDF is a measure used in text analysis. Applications include translation and sentiment analysis."

vectorizer, tfidf_matrix = calculate_tfidf(sentences)
generated_summary = summarize_text(sentences, tfidf_matrix, top_n=2)

# Evaluasi
scores = evaluate_summary(generated_summary, reference_summary)
print("Generated Summary:", generated_summary)
print("ROUGE Scores:", scores)