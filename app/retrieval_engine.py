import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_kb_data():

    df = pd.read_csv(
        'kb/model_ready_kb.csv'
    )

    return df


def build_vectorizer(df):

    tfidf = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_df=0.85,
        min_df=2
    )

    tfidf_matrix = tfidf.fit_transform(
        df['clean_instruction']
    )

    return tfidf, tfidf_matrix


def retrieve_best_match(
    tfidf_matrix,
    df,
    query_vector
):

    similarity_scores = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    best_match_index = similarity_scores.argmax()

    best_match = df.iloc[
        best_match_index
    ]

    best_score = similarity_scores[
        best_match_index
    ]

    if best_score >= 0.70:

        decision = 'AI Resolved'

    elif best_score >= 0.55:

        decision = (
            'AI Suggested Response - '
            'Confirmation Recommended'
        )

    else:

        decision = (
            'Escalated to Human Support'
        )

    return {

        "decision": decision,

        "category":
        best_match['category'],

        "intent":
        best_match['intent'],

        "response":
        best_match['response'],

        "similarity_score":
        best_score
    }