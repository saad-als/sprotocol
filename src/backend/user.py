from .database import User, db


class User:

    def __init__(self, user_name="saad", secure_code="No s_code") -> None:
        self.user_name = user_name
        self.secure_code = secure_code

    def createUser(self):
        user = User(self.user_name, self.secure_code)
        db.session.add(user)
        db.session.commit()
