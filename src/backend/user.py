from .database import User, db
from .secureCodeGenerator import Generator


class User:

    def __init__(self, user_name="saad", secure_code="No s_code") -> None:
        self.user_name = user_name
        self.secure_code = Generator.createCode(secure_code)

    def createUser(self, username):
        user = User(self.user_name, self.secure_code)
        db.session.add(user)
        db.session.commit()
