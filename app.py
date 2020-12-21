### IMPORT DEPENDENCIES

from flask import Flask, render_template, jsonify
import pymongo

# INITIATE YOUR CONFIGURATION 
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.fruits_db
coll = db.fruits

greeting = "Greetings good friends!"
movie_list = ["Fast and Furious", "Batman", "Star Wars", "Superman"]
mydict = { "player_1" : "James Harden", 
            "player_2" : "Kevin Durant"}

# CREATE YOUR WEBAPP 

# render a list from python into our HTML
@app.route("/")
def main(): 
    return render_template("index.html", list = movie_list)

# render a list from mongoDB into jsonified route
@app.route("/fruits/api")
def fruits_api():
    mylist = []
    for item in coll.find({}, {"_id":0}): 
        mylist.append(item)
    return jsonify(results = mylist)

# render a list from mongoDB into HTML
@app.route("/fruits")
def fruits(): 
    results = list(coll.find())
    return render_template("fruits.html", fruits=results)

# render a dictionary from python into HTML
@app.route("/player")
def player(): 
    return render_template("player.html", dict = mydict)

# render variables from python into route
@app.route("/contact")
def contact(): 
    email = "abc@xyz.com"
    return f"My email is {email}."

# render variables from a route into a route
@app.route("/contact/<name>")
def contact_name(name):    
    email = f"{name}@xyz.com"
    return f"My email is {email}."

if __name__ == "__main__":
    app.run(debug=True)