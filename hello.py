from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

"""
Jinja2:
safe
capitalize
lower
upper
title
trim
striptags
"""

# Create a route decorator
@app.route("/")
def index():
    first_name = "Marco"
    stuff = "This is <strong>BOLD</strong> Text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza
                           )

# localhost:5000/user/john
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

# Create Customer Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500