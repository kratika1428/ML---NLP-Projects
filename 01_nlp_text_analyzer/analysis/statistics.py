import re

def get_statistics(text):
    characters = len(text)
    words = text.split()
    word_count = len(words)
    unique_words = len(set(words))
    sentences = re.split(r"[.!?]+", text)
    sentences = [
        sentence
        for sentence in sentences
        if sentence.strip()
    ]
    sentence_count = len(sentences)

    if word_count > 0 :
        average_word_length = (
            sum(len(word) for word in words)
            / word_count
        )
    else:
        average_word_length = 0

    if sentence_count > 0 :
        average_sentence_length = (
            word_count / sentence_count
        )
    else:
        average_sentence_length = 0

    return {
        "characters": characters,
        "words": word_count,
        "sentences": sentence_count,
        "unique_words": unique_words,
        "average_word_length":
            round(average_word_length, 2),
        "average_sentence_length":
            round(average_sentence_length, 2)
    }