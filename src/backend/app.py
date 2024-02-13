from flask import Flask
from flask import request
from .database import db
from .secureCodeGenerator import Generator
from .user import User
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ttest.db"  # testing only
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = "saad"
        my_code = Generator.createCode(username)
        new_user = User(username, my_code)
        new_user.createUser()

    return f"<p>This is from server.</p>"


@app.route("/chat")
def chat():
    pass
