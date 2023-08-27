from hashlib import sha256
from werkzeug.security import generate_password_hash

class AuthLogic:

    @staticmethod
    def generate_password(password: str):
        return generate_password_hash(password)