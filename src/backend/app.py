from flask import Flask
from flask import request
from .database import db
from .user import User
app = Flask(__name__)
# testing only
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_sprotocol.db"
db.init_app(app)

# create database
with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass

    return "hello Saad this is / route"


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    pass


if __name__ == '__main__':
    app.run(debug=True)
