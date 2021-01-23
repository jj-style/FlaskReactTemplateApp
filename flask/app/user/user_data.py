from flask_restful import fields

user_response = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "uri": fields.Url("user_ep", attribute="user.id"),
}


def password_t(pwd):
    if len(pwd) < 3:
        raise ValueError(f"Password must be 3 or more characters, was {len(pwd)}")
    return pwd
