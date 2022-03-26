import os
from flask import (
    Flask, url_for,request, render_template, redirect,flash, session )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, check_password_hash   
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_names")
def get_names():
    names = mongo.db.names.find()
    return render_template("names.html" , names = names)


@app.route("/create", methods=["GET", "POST"])
def create():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)