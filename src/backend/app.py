from flask import Flask
from flask import request
# from .database import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdb.db"  # testing only


@app.route("/", methods=['GET', 'POST'])
def home():
    return "hello Saad this is / route"


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    pass


if __name__ == '__main__':
    app.run(debug=True)
