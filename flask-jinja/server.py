from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = random.randint(1,10)
    current_year = date.today().year
    me = "Sonni"
    return render_template("index.html", num=random_number, current_year=current_year, me=me)


if __name__ == "__main__":
    app.run(debug=True)