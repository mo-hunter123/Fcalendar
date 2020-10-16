from flask import Flask
from flask import request, render_template, jsonify
import json


app = Flask(__name__)


@app.route('/')
def calendar():
    return render_template("json.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
