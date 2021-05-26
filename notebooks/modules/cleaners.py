from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pandas as pd
import re


def simple_clean(text):
    text = text.lower()
    text: str = re.sub("\n", "", text)
    return text


def clean_text(speech):
    tokens = word_tokenize(speech)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return words


def clean_two(list):
    result = []
    for e in list:
        tokens = word_tokenize(e)
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        result.append(words)
    return result
