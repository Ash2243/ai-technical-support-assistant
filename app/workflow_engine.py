from backend.preprocessing import process_query

from backend.retrieval_engine import (
    retrieve_best_match
)


def handle_query(
    user_query,
    tfidf,
    tfidf_matrix,
    df
):

    clean_query = process_query(
        user_query
    )

    query_vector = tfidf.transform(
        [clean_query]
    )

    result = retrieve_best_match(
        tfidf_matrix,
        df,
        query_vector
    )

    result["original_query"] = (
        user_query
    )

    result["processed_query"] = (
        clean_query
    )

    return result