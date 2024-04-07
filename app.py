from flask import Flask
from views import views
from flask import Blueprint, render_template, request

import phone_tracker

app = Flask(__name__)
# app.register_blueprint(views, url_prefix="/views")

@app.route("/")
def home():
    return render_template("index.html", name="Rohan")

@app.route("/", methods=['POST'])
def getValue():
    number = request.form['number']
    phone_tracker.getLocation(number)
    return render_template("myLocation.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
