from flask import Flask, request
from flask_restful import Api, Resource

from routes.products import GetAll, GetOne

app = Flask(__name__)
api = Api(app)


# home endpoint ('/')
# @app.route("/")
# def index():
#     return jsonify({"msg": "This is a restAPI. All good and beautiful"})


# home endpoint ('/')
class Welcome(Resource):
    def get(self):
        return {"msg": "This is a restAPI. All good and beautiful"}


api.add_resource(Welcome, "/")
api.add_resource(GetAll, "/products")
api.add_resource(GetOne, "/product/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)
