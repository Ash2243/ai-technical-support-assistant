{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "372413a4-71bb-4e36-881b-b4d25c02997c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def handle_query(user_query, tfidf, tfidf_matrix, df):\n",
    "    \n",
    "    clean_query = process_query(user_query)\n",
    "\n",
    "    query_vector = tfidf.transform([clean_query])\n",
    "\n",
    "    result = retrieve_best_match(tfidf_matrix, df, query_vector)\n",
    "\n",
    "    result[\"original_query\"] = user_query\n",
    "    result[\"processed_query\"] = clean_query\n",
    "\n",
    "    return result"
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
