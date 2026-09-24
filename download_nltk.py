import nltk

resources = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "omw-1.4",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "maxent_ne_chunker",
    "maxent_ne_chunker_tab",
    "words"
]

for resource in resources:
    print(f"Downloading: {resource}")
    nltk.download(resource)

print("All NLTK resources downloaded.")