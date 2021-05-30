import pandas as pd

def lixdata():

    df_first_clean = pd.read_pickle('../pickled_data/data_first_clean.pkl')


    # Copy main dataframe (first clean - we don't want lemmatization here!):
    df_lix = df_first_clean.copy()
    df_lix = df_lix.drop(columns = ['speech', 'first_clean_tokenized'])


    # WORD COUNT:
    # Method to calculate total words in each speach:
    def word_count(speech):
        return sum(1 for word in speech.split(' '))

    # Get total words in each speech and add result to DataFrame:
    df_lix['word_count'] = df_lix.first_clean.apply(word_count)


    # COUNT OF PERIODS:
    # Method to calculate total number of periods (period or colon) in each speach:
    def period_count(speech):
        result = speech.count('.') + speech.count(':')
        return result

    # Get total number of periods in each speech and add result to DataFrame:
    df_lix['period_count'] = df_lix.first_clean.apply(period_count)


    # COUNT OF LONG WORDS:
    # Method to long words (< 6 characters) in each speach:
    def long_word_count(speech):
        count = 0
        for word in speech.split(' '):
            if len(word) > 6:
                count += 1
        return count

    # Get total number of long words in each speech and add result to DataFrame:
    df_lix['long_words_count'] = df_lix.first_clean.apply(long_word_count)


    # CALCULATE LIX:
    # Calculates LIX for each speech and adds result to DataFrame:
    df_lix['lix'] = (df_lix.word_count/df_lix.period_count) + ((df_lix.long_words_count*100) / df_lix.word_count)

    return df_lix