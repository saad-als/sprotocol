from database import db, User
from sqlalchemy import select
from secureCodeGenerator import generate_password_hash, check_password_hash


class User:
    # create a user - Sender
    def create_sender(self, username):
        self.hash_code = generate_password_hash(username)
        self.user = User(username=username, secure_code=self.hash_code)
        db.session.add(self.user)
        db.session.commit()

    # get sender user hashcode from db
    def get_sender_hashcode(self, usr):
        get_hash = db.session.execute(select(usr).filter_by(
            secure_code=usr.secure_code)).scalar_one()
        return get_hash

    # create a user - Recevier
    def create_recevier(self, username, sender_hash_code):
        try:
            # query a user based on id which is (1) and check if hashcodes matches
            is_sender_exist = db.session.execute(
                select(User).where(User.secure_code == sender_hash_code).filter(User.id == 1)).scalar_one()

            is_same_code = check_password_hash(
                sender_hash_code, is_sender_exist.secure_code)

            # if sender user exits, create a second user receiver and commit it to db
            if is_same_code:
                self.user = User(username=username,
                                 secure_code=sender_hash_code)
                db.session.add(self.user)
                db.session.commit()

        except Exception as er:
            print("error occured : ", er)
