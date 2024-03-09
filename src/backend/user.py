from .database import User, db
from .secureCodeGenerator import Generator


class User:

    def __init__(self, user_name=None) -> None:
        self.user_name = user_name
        self.secure_code = Generator.createCode(self.user_name)

    def createSender(self, username):
        user = User(username)
        db.session.add(user)
        db.session.commit()

    def createRecevier(self, username, hash_code):
        is_sender_exist = db.session.execute(
            db.select(User).where(User.secure_code == hash_code)).scalar()
        if is_sender_exist:
            user = User(username)
            db.session.add(user)
            db.session.commit()
