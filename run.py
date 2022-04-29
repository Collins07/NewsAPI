from flask import Flask, render_template
app = Flask(__name__)


from newsapi import NewsApiClient


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)