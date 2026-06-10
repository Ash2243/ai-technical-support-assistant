{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aacd68d0-d674-44c0-b510-16800738c5ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4917556d-aa8f-46a5-ab7b-c7e164411ea2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_kb_data():\n",
    "    df=pd.read_csv('../kb/model_ready_kb.csv')\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "17c57ce8-3481-4221-9ba7-0b918a57b0f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def build_vectorizer(df):\n",
    "    tfidf = TfidfVectorizer(\n",
    "    stop_words='english',\n",
    "    ngram_range=(1, 2),\n",
    "    max_df=0.85,\n",
    "    min_df=2\n",
    ")\n",
    "    tfidf_matrix = tfidf.fit_transform(df['clean_instruction'])\n",
    "        \n",
    "    return tfidf,tfidf_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3ad62c9-6982-41de-8f68-c152ee1233ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "def retrieve_best_match(tfidf_matrix,df,query_vector):\n",
    "    similarity_scores = cosine_similarity(\n",
    "    query_vector,\n",
    "    tfidf_matrix\n",
    ").flatten()\n",
    "    best_match_index = similarity_scores.argmax()\n",
    "    best_match = df.iloc[best_match_index]\n",
    "    best_score = similarity_scores[best_match_index]\n",
    "    if best_score >= 0.70:\n",
    "        decision = 'AI Resolved'\n",
    "    elif best_score >= 0.55:\n",
    "        decision = 'AI Suggested Response - Confirmation Recommended'\n",
    "    else:\n",
    "        decision = 'Escalated to Human Support'\n",
    "    return {\n",
    "        \"decision\":decision,\n",
    "        \"category\":best_match['category'],\n",
    "        \"intent\":best_match['intent'],\n",
    "        \"response\":best_match['response'],\n",
    "        \"similarity_score\":best_score\n",
    "    }"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
