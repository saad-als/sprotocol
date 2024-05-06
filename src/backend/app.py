from flask import Flask
from flask import request
from flask_cors import CORS
from database import db
from user import User
app = Flask(__name__)
cors = CORS()
# testing only
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_sprotocol.db"
db.init_app(app)
cors.init_app(app)
# create database
with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_data = request.get_json()
        print("data from frontend is here", user_data)

    return "hello Saad this is / route"


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    pass


if __name__ == '__main__':
    app.run(debug=True)
