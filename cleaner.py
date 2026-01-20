nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


import re 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

negations = {"no" , "not" , "never" , "nah" }

stop_words = stop_words - negations

def normalize_text(text:str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    return text
    
def remove_special_char(text:str) -> str:
   text = re.sub(r"[^a-z\s]", "", text)
   return text


def tokenize_and_clean(text:str) -> str:
    tokens = word_tokenize(text)
    return [t for t in tokens if t not in stop_words]

def clean_text(text:str) -> str:
    text = normalize_text(text)
    text = remove_special_char(text)
    tokens = tokenize_and_clean(text)
    return " ".join(tokens)
