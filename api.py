import flask
import requests
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# CREATE RELEASE JSON FROM API REQUEST
r = requests.get("https://www.energy.gov/sites/prod/files/2020/12/f81/code-12-15-2020.json")
json = r.json()
releases = json["releases"]


# WRITE CSV FILE
with open('organizations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['organization', 'labor_hours', 'status', 'licenses', 'date_created'])

    for x in releases:
        licenses = []
        for l in x['permissions']['licenses']:
            name = l['name']
            licenses.append(name)

        writer.writerow([x['organization'], x['laborHours'], x['status'], licenses, x['date']['created']])


@app.route('/', methods=['GET'])

def home():
    return releases[0]
app.run()
