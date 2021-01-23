from flask_restful import Resource


class Index(Resource):
    def get(self):
        return "hello world"


class Health(Resource):
    def get(self):
        return {"STATUS": "OK"}
