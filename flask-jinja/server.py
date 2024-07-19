from flask import Flask, render_template
import random
from datetime import date
import requests







######################## FLASK APP ########################

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = random.randint(1,10)
    current_year = date.today().year
    me = "Sonni"
    return render_template("index.html", num=random_number, current_year=current_year, me=me)


@app.route("/guess/<name>")
def check_name(name):
    params = {
        "name": name
    }
    # request for gender guess
    response_gen = requests.get(url="https://api.genderize.io?", params=params)
    response_gen.raise_for_status()
    gender = response_gen.json()["gender"]

    # request for age guess
    response_age = requests.get(url="https://api.agify.io?", params=params)
    response_age.raise_for_status()
    age = response_age.json()["age"]

    return render_template("indexname.html", name=name.title(), age=age, gender=gender)



if __name__ == "__main__":
    app.run(debug=True)