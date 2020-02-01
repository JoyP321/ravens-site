from flask import Flask, request, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():

if __name__=="__main__":
    app.run(debug=False)
