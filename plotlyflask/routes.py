"""Routes for parent Flask app"""
from flask import Flask
from flask import current_app as app
from flask.templating import render_template

@app.route("/")
def home():
    return render_template(
        "home.html"
    )