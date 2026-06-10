{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9838f9f-509b-4b3a-a058-b82383c20399",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "custom_stopwords = ['get', 'want', 'need', 'help', 'question']\n",
    "def process_query(query):\n",
    "    query = query.lower()\n",
    "    query = re.sub(r'[^a-zA-Z0-9\\s]', '', query)\n",
    "    \n",
    "    words = query.split()\n",
    "    words = [word for word in words if word not in custom_stopwords]\n",
    "    query = ' '.join(words)\n",
    "\n",
    "    login_clues = ['into my account', 'access account', 'access my account', 'sign in', 'signin', 'login', 'log in', 'cant access', 'cannot access']\n",
    "    \n",
    "    if any(clue in query for clue in login_clues):\n",
    "        query += ' login signin access password registration problems'\n",
    "\n",
    "    return query"
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
