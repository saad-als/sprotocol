from flask import Flask
from flask import request
from .database import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ttest.db"  # testing only
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    pass


@app.route("/chat")
def chat():
    pass
