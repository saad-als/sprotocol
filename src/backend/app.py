from flask import Flask

app = Flask(__name__)


@app.route("/")
def runningServer():
    return "<p>Server is running....</p>"
