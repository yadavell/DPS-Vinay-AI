from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test_heroku")
def test_heroku():
    return "Heroku Working"


@app.route("/")
def predict():
    try:
        year = request.args.get("year")
        month = request.args.get("month")
        return str(year) + " : " + str(month)
    except Exception as err:
        return err
