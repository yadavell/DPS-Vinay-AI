from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test_heroku")
def test_heroku():
    return "Heroku Working"


@app.route("/", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        year = data["year"]
        month = data["month"]
        return str(year) + " : " + str(month)
    except Exception as err:
        return err
