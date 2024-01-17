from flask import Flask
from backend.accounts.sender import Sender

app = Flask(__name__)


@app.route("/")
def running():

    return "<p>nothing is here</p>"
