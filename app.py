# 1. import Flask
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import JTscrap_mars
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Use flask_pymongo to set up mongo connections
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# 3. Define what to do when a user hits the index route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# 4. Scrape
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = JTscrap_mars.scrape()
    mars.update({}, mars_data,upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)