from flask import Flask, render_template
from fetchSpeech import getspeech
import pandas as pd
from sentiment import sentiment
from lix import lixdata


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


@app.route('/lix')
def getLix():
    df = lixdata()
    df2 = df[["year", "lix"]]
    data = df2.to_records(index=False)
    print(data)

    labels= [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("lix_chart.html", labels= labels, values = values)

@app.route('/obamatrump')
def obamaVsTrump():
    df = lixdata()
    mask_obama = (df['President'] == 'Barack Obama')
    mask_trump = (df['President'] == 'Donald Trump')
    avg_lix_obama = df[mask_obama]['lix'].mean()
    avg_lix_trump = df[mask_trump]['lix'].mean()
    data = [("obama", avg_lix_obama), ("Trump",avg_lix_trump )]
    print(data)
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("obamaVsTrump.html", labels= labels, values = values)




if __name__ == "__main__":
     # Only for debugging while developing
     app.run(host='0.0.0.0', debug=True, port=5001)


