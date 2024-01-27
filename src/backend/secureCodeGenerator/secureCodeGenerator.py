from werkzeug.security import generate_password_hash, check_password_hash


class Generator:

    secure_password = None
    user_name = None

    # creating the secure code by using user name and save the code in the database
    def createCode(self, user_name):
        self.user_name = user_name
        self.secure_password = generate_password_hash(user_name)
    # getting the secure code from the database

    def getCode(self):
        return self.secure_password
    # checking the secure code if it matches the one in the database which is the user name as a plain text

    def checkCode(self, sec_code):
        return check_password_hash(sec_code, self.user_name)
