from flask import Flask
from fetchSpeech import getspeech

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/demo')
def hello_demo():
    return 'Hello DEMO'

@app.route('/speech')
def speech():
    return getspeech()



if __name__ == "__main__":
     # Only for debugging while developing
     app.run(host='0.0.0.0', debug=True, port=5001)


