from flask import Flask
from flask import request
from flask_cors import CORS
from database import db
app = Flask(__name__)
cors = CORS()
# testing only
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_sprotocol.db"
db.init_app(app)
cors.init_app(app)
# create database
with app.app_context():
    db.create_all()


@app.route("/")
def home():

    return "hello Saad this is / route"


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    return 'its working'


if __name__ == '__main__':
    app.run(debug=True)
