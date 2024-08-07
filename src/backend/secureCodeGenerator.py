from werkzeug.security import generate_password_hash, check_password_hash


class Generator:

    # create a hash code
    def generate_code(self, code):
        hashed_code = generate_password_hash(code)
        return hashed_code

    # check hash code
    def check_hash_code(self, code, password):
        return check_password_hash(code, password)
