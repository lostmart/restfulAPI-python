from flask import Flask, request
from flask_restful import Api, Resource

from api.routes.products import GetAll, GetOne


app = Flask(__name__)
api = Api(app)


# home endpoint ('/')
class Welcome(Resource):
    def get(self):
        return {"msg": "This is a restAPI. All good and beautiful"}


api.add_resource(Welcome, "/")
api.add_resource(GetAll, "/api/products")
api.add_resource(GetOne, "/api/products/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)
