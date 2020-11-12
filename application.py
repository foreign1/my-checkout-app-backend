from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Please access api/v1/checkout/ for post requests"