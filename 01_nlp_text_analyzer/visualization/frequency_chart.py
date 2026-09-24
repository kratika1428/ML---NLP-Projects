import matplotlib.pyplot as plt

def create_frequency_chart(top_words):
    words = [item[0] for item in top_words]
    counts = [item[1] for item in top_words]
    fig, ax = plt.subplots()
    ax.bar(words, counts)
    ax.set_xlabel("Words")
    ax.set_ylabel("Frequency")
    ax.set_title("Top Word Frequencies")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig