from flask import jsonify
from flask import Blueprint
from flask_restful import Resource


products = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

# Create a Blueprint instance
products_blueprint = Blueprint("product_blueprint", __name__)


class GetAll(Resource):
    def get(self):
        return products

    def post(self):
        return {"msg": "nunca puedes"}, 201


class GetOne(Resource):
    def get(self, id):
        found = "No product founds with that id !"
        stat_code = 404
        for product in products:
            if product["id"] == id:
                found = product
                stat_code = 200

        return {"msg": found}, stat_code
