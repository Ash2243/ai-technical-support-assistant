import streamlit as st

from backend.retrieval_engine import load_kb_data, build_vectorizer
from backend.workflow_engine import handle_query


st.set_page_config(
    page_title="AI Technical Support Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Technical Support Assistant")

st.write(
    "Enter a customer support query and the system will retrieve a relevant response or escalate it based on confidence."
)

df = load_kb_data()

tfidf, tfidf_matrix = build_vectorizer(df)

user_query = st.text_area(
    "Enter your support query:",
    placeholder="Example: I cannot login to my account"
)

if st.button("Submit Query"):

    if user_query.strip() == "":
        st.warning("Please enter a support query.")

    else:

        result = handle_query(
            user_query,
            tfidf,
            tfidf_matrix,
            df
        )

        st.subheader("Workflow Decision")
        st.write(result["decision"])

        st.subheader("Matched Category")
        st.write(result["category"])

        st.subheader("Matched Intent")
        st.write(result["intent"])

        st.subheader("Similarity Score")
        st.write(round(result["similarity_score"], 2))

        st.subheader("Suggested Response")
        st.write(result["response"])
