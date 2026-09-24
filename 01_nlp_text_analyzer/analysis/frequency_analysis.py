from collections import Counter

def get_word_frequency(tokens):
    frequency = Counter(tokens)
    return frequency

def get_tokens_frequency(tokens, top_n=10):
    frequency = Counter(tokens)
    return frequency.most_common(top_n)