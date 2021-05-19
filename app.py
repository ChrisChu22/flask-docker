import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/bye')
def bye():
    return 'Goodbye world!'


@app.route('/car')
def car():
    return 'I am a race car! 🚗'


@app.route('/final')
def final():
    return 'This is a change I am adding to see if my GitHub Actions work and everything has been deployed properly. Please accept this change for my final project. Thank you. :)'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
