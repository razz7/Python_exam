import pandas as pd
from textblob import TextBlob


def sentiment():
    #Sentiment analysis on Polarity and Subjectivity for all speeches using TextBlob:
    df_first_clean = pd.read_pickle('../pickled_data/data_first_clean.pkl')

    def sentiment(text):
        try:
            return TextBlob(text).sentiment
        except:
            return None

    df_first_clean['Polarity'] = df_first_clean['first_clean'].apply(sentiment).apply(lambda x: x[0])
    df_first_clean['Subjectivity'] = df_first_clean['first_clean'].apply(sentiment).apply(lambda x: x[1])


    return df_first_clean