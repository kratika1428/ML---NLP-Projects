from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemmatize_words(tokens):
    return [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]