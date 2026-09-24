from nltk import sent_tokenize
from nltk import word_tokenize

def tokenize_words(text):
    return word_tokenize(text)

def tokenize_sentences(text):
    return sent_tokenize(text)