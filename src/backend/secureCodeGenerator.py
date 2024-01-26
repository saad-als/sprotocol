from werkzeug.security import generate_password_hash, check_password_hash


class Generator:

    # secure_password = here will be the database object
    # a def for creating the secure code by sender request
    def createCode(self, user_name, password):
        self.secure_password = generate_password_hash(password)
        # add secure code to db and username who generated it

    # for checking if the secure code match the original sent code
    def checkCode(self, password):
        return check_password_hash(self.secure_password, password)
