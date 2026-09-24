from nltk.corpus import stopwords

stopwords = set(stopwords.words("english"))

def remove_stopwords(tokens):
    filtered_tokens = [
        word 
        for word in tokens 
        if word.lower() not in stopwords 
    ]

    return filtered_tokens