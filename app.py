from flask import Flask, render_template

from flask_pymongo import PyMongo
from newsapi import NewsApiClient

from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash

app= Flask(__name__)

@app.route('/')
def Index():
    newsapi=NewsApiClient(api_key="b4d1d8736a944873933ac5336502806a")
    topheadlines=newsapi.get_top_headlines(sources="abc-news")

    articles =topheadlines['articles']
    desc=[]
    news=[]
    img=[]

    for i in range(len(articles)):
        myarticles=articles[i] 
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        img.append(myarticles['urlToImage'])


    mylist =zip(news,desc, img)
    return render_template('index.html',context=mylist)

#app.secret_key ="rohit"

#app.config['MONGO_URI']="mongodb://localhost:27017/chatapp"

#mongo =PyMongo(app)

if __name__=="__main__":
    app.run(debug=True)




