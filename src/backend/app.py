from flask import Flask
from flask import request
from database import db
from sender import Sender
from secureCodeGenerator import Generator
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ttest.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass

    return f"<p>{name}, \n {account}</p>"


@app.route("/chat")
def chat():
    pass
