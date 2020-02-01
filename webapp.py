from flask import Flask, request, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/shop")
def render_shop():
    return render_template('shop.html')

@app.route("/gallery")
def render_gallery():
    return render_template('gallery.html')

@app.route("/about")
def render_about():
    return render_template('about.html')

@app.route("/contact")
def render_contact():
    return render_template('contact.html')

@app.route("/img1")
def render_contact():
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)
