import streamlit as st

from preprocessing.cleaning import clean_text
from preprocessing.lemmatization import lemmatize_words
from preprocessing.stemming import stem_words
from preprocessing.stopwords_removal import remove_stopwords
from preprocessing.tokenization import tokenize_sentences, tokenize_words

from analysis.statistics import get_statistics
from analysis.frequency_analysis import get_tokens_frequency, get_word_frequency

from visualization.frequency_chart import create_frequency_chart

st.set_page_config(
    page_title="Text Analyzer",
    layout="centered"
)
st.title("Text Analyzer")
st.write("Analyzing the Text with the help of NLP")

st.divider()

text = st.text_area(
    label="Enter your text",
    height= 250,
    placeholder="Type or paste your text here...."
)

if st.button("Analyze Text"):
    if not text.strip():
        st.warning("Please enter some text")
    else:

        #statistics analysis
        stats = get_statistics(text)
        st.header("Text Statistics")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(
                "Characters",
                stats["characters"]
            )
        with col2:
            st.metric(
                "Words",
                stats["words"]
            )
        with col3:
            st.metric(
                "Sentences",
                stats["sentences"]
            )
        with col4:
            st.metric(
                "Unique_words",
                stats["unique_words"]
            )

        #cleaning of the text
        cleaned = clean_text(text)
        st.subheader("Cleaned Text")
        st.write(cleaned)

        #tokenization of the text
        word_tokens = tokenize_words(cleaned)
        sent_tokens = tokenize_sentences(text)
        st.subheader("Tokenization")
        st.write(f"word tokens: {len(word_tokens)}")
        st.write(f"sentence tokens: {len(sent_tokens)}")
        with st.expander("View word tokens"):
            st.write(word_tokens)

        #stopwords removal after tokenization
        filtered_tokens = remove_stopwords(word_tokens)
        st.subheader("Stopword Removal")
        st.write(f"Original Tokens: {len(word_tokens)}")
        st.write(f"After Stopword Removal: {len(filtered_tokens)}")
        with st.expander("View Filtered Tokens"):
            st.write(filtered_tokens)

        #frequency analysis
        frequency = get_word_frequency(filtered_tokens)
        top_words = get_tokens_frequency(
            filtered_tokens,
            top_n=10
        )
        st.subheader("Word Frequency Analysis")
        fig = create_frequency_chart(top_words)

        st.pyplot(fig)

        #stemming after stopwords removal
        stemmed = stem_words(filtered_tokens)
        st.subheader("Stemming")
        with st.expander("View Stemmed Words"):
            st.write(stemmed)

        #lemmatization after stopwords removal
        lemmatized = lemmatize_words(filtered_tokens)
        st.subheader("Lemmatization")
        with st.expander("View Lemmatized Words"):
            st.write(lemmatized)