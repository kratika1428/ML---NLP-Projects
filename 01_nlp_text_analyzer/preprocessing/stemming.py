from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def stem_words(tokens):
    return [
        stemmer.stem(word)
        for word in tokens
    ]