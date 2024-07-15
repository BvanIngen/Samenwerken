from flask import Flask
import Ben
import bryan

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/anders")
def anders():
    return "<p>Een hele andere wereld</p>"

@app.route("/bryan1")
def felixfunctie1():
    return bryan.functievanBryan()

@app.route("/Ben1")
def JodieFunctie():
    return Ben.functieBen()

@app.route("/Ben2/<destad>")
def BenFunctie2(destad):
    return Ben.functieBen2(destad)