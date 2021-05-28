from flask import Flask, render_template
from fetchSpeech import getspeech
import pandas as pd
from sentiment import sentiment

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/speech')
def speech():
    return getspeech()

@app.route('/checkdata')
def get_tabel():
    df = pd.read_pickle("../notebooks/pickled_data/data_for_flask.pkl")
    df2 = df.drop(columns = ['speech'])
    return df2.to_html()

@app.route('/sentiment')
def getSentiment():
    df = sentiment()
    df2 = df.drop(columns = ['speech', 'first_clean', 'first_clean_tokenized'])
    return df2.to_html()



if __name__ == "__main__":
     # Only for debugging while developing
     app.run(host='0.0.0.0', debug=True, port=5001)


