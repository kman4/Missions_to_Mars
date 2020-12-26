### IMPORT DEPENDENCIES

from flask import Flask, render_template, redirect,jsonify
from flask_pymongo import pymongo 
import scape

# INITIATE YOUR CONFIGURATION 
app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017'
mongo = PyMongo(app)

@app.route("/")
def index()
    mars_data = db.collection.find_one()
    return render_template('index.html', list=mars_data)
                           
@appl.route("/scrape")
def scrape()
    scrape.scrape_all()
    retunr redirect("/")                       
                           
