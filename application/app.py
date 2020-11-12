from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Kindly direct all post requests to /api/v1/checkout/ "