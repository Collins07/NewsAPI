from flask import Flask, render_template
app = Flask(__name__)


from newsapi import NewsApiClient


@app.route('/')
@app.route('/home')
def home():

    newsapi = NewsApiClient(api_key="1111f8f3bf334cc6a0af77fa30f68e29")

    top_headlines = newsapi.get_top_headlines(sources= "bbc-news" )

    t_articles = top_headlines['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range(len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article["title"])
        desc.append(main_article["description"])
        img.append(main_article["urlToImage"])
        p_date.append(main_article["publishedAt"])
        url.append(main_article["url"])

        contents = zip(news,desc,img,p_date,url)


    return render_template('index.html', contents=contents)


if __name__ == '__main__':
    app.run(debug = True)