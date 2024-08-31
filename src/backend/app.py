from flask import Flask
from flask import request
from flask_cors import CORS
from database import User, Base
from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.orm import Session
app = Flask(__name__)
cors = CORS()

# initializing engine and session
engine = create_engine("sqlite://", echo=True)
session = Session(engine)
Base.metadata.create_all(engine)
# enabling CORS
cors.init_app(app)

# Creating a user


def create_user(username, secure_code):
    with Session(engine) as session:
        new_user = User(username=username, secure_code=secure_code)
        session.add(new_user)
        session.commit()


def get_user(usr):
    stmt = select(User).where(User.username == usr)

    for user in session.scalers(stmt):
        print(user)


@app.route("/", methods=['GET', 'POST'])
def home():
    create_user("Saad", "12345e")
    return "hello Saad this is / route"


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    return 'its working'


if __name__ == '__main__':
    app.run(debug=True)
