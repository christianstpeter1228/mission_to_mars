from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('authentication')
mongo = PyMongo(app)

@app.route("/")
def home(): 

    mars_db= mongo.db.mars_db.find_one()

    return render_template("index.html", mars_db=mars_db)

@app.route("/scrape")
def scrape(): 

    mars_db = mongo.db.mars_db
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data= scrape_mars.scrape_mars_weather()
    mars_db.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)