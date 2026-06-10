import re


custom_stopwords = [
    'get',
    'want',
    'need',
    'help',
    'question'
]


def process_query(query):

    query = query.lower()

    query = re.sub(
        r'[^a-zA-Z0-9\s]',
        '',
        query
    )

    words = query.split()

    words = [
        word for word in words
        if word not in custom_stopwords
    ]

    query = ' '.join(words)

    login_clues = [
        'into my account',
        'access account',
        'access my account',
        'sign in',
        'signin',
        'login',
        'log in',
        'cant access',
        'cannot access'
    ]

    if any(clue in query for clue in login_clues):

        query += (
            ' login signin access '
            'password registration problems'
        )

    return query