from flask_restful import fields

user_response = {"username": fields.String}


def password_t(pwd):
    if len(pwd) < 3:
        raise ValueError(f"Password must be 3 or more characters, was {len(pwd)}")
    return pwd