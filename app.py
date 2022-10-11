from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test_heroku")
def test_heroku():
    return "Heroku Working"
