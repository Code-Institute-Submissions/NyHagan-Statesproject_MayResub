import os
from flask import (
    Flask, url_for,request, render_template, redirect,flash, session )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId    
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def hello():
    return "hi"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)