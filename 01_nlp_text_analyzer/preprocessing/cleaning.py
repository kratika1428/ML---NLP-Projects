import re

def clean_text(text):
    text = text.lower() # convert into lowercase
    text = re.sub(r"https?://\S+|www\.\S+","", text) # remove url
    text = re.sub(r"\d+","", text) # remove numbers
    text = re.sub(r"[^A-Za-z\s]","", text) # remove punctuations
    text = " ".join(text.split()) #remove extra spaces

    return text