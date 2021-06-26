import flask
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    r = requests.get("https://www.energy.gov/sites/prod/files/2020/12/f81/code-12-15-2020.json")
    json = r.json()
    return json
app.run()
