from flask import Flask, request
from flask_cors import CORS
import pickle
app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/test_heroku")
def test_heroku():
    return "Heroku Working"

@app.route("/", methods=["POST"])
def apppredict():
    try:
        data = request.get_json()
        year = data["year"]
        month = data["month"]
        prediction = int(model.predict([[year, month]]))
        return prediction
    except Exception as err:
        return err
