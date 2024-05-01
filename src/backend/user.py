from .database import db, User
from sqlalchemy import select
from .secureCodeGenerator import generate_password_hash, check_password_hash


class User:

    # create a user - Sender
    def create_sender(self, username):
        self.hash_code = generate_password_hash(username)
        self.user = User(id=1, username=username, secure_code=self.hash_code)
        db.session.add(self.user)
        db.session.commit()

    # create a user - Recevier
    def create_recevier(self, username, sender_hash_code):
        try:
            is_sender_exist = db.session.execute(
                select(User).where(User.secure_code == sender_hash_code).filter(User.id == 1)).scalar_one()

            is_same_code = check_password_hash(
                sender_hash_code, is_sender_exist.secure_code)

            if is_same_code:
                self.user = User(id=2, username=username,
                                 secure_code=sender_hash_code)

                db.session.add(self.user)

                db.session.commit()

        except:
            pass
