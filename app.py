import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
    return render_template("names.html", names=names)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        
        existing_user = mongo.db.people.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("create"))

        create = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.people.insert_one(create)

        
        session["user"] = request.form.get("username").lower()
        flash("Your account was created successfully!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("create.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if  request.method == "POST":
        existing_user = mongo.db.people.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                            "profile", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.people.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("get_names"))


@app.route("/fact", methods=["GET", "POST"])
def fact():
    if  request.method == "POST":
        
        find_state = request.form.get("find_state").capitalize()

        new_fact = request.form.get("add_fact").capitalize()

        if mongo.db.names.find_one({"state_name": find_state}):

            mongo.db.names.find_one_and_update({"state_name": find_state}, 
                                 {"$set": {"fun_fact": new_fact}} 
                                 )

            flash("A new Fact Has been Added!")

        else:
            flash("There is no state called " + find_state)
    
    return render_template("fact.html")


@app.route("/delfact", methods=["GET", "POST"])
def delfact():
    if  request.method == "POST":
        
        del_state = request.form.get("del_state").capitalize()

        mongo.db.names.find_one_and_update({"state_name": del_state}, 
                                 {"$set": {"fun_fact":''}} 
                                 )
        flash("Fact has been Deleted")
        return redirect(url_for('fact'))
        print(del_state)

    else:
        return render_template("delfact.html")    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)