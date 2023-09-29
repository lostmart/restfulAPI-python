from flask import request

from flask_restful import Resource, reqparse

import sqlite3


# DATABASE stuff ...
conn = sqlite3.connect("test.db")

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Step 3: Execute the SQL query to retrieve all products
cursor.execute("SELECT * FROM products")

# Step 4: Fetch the results
products = cursor.fetchall()

# # Step 5: Display the products or perform further operations
for product in products:
    # print(product)
    pass


product_put_args = reqparse.RequestParser(bundle_errors=True)  # shows multiple error
product_put_args.add_argument(
    "price",
    type=float,
    help="The price cannot be empty and needs to be a number",
    required=True,
)
product_put_args.add_argument(
    "description",
    type=str,
    help="The description of the product is required",
    required=True,
)
product_put_args.add_argument(
    "test", type=str, help="The description of the product is required", required=True
)
product_put_args.add_argument(
    "images",
    type=str,
    help="The images of the product are required",
    required=True,
    action="append",
)

product_put_args.add_argument("Authorization", location="headers")


class GetAll(Resource):
    def get(self):
        return products

    def post(self):
        args = product_put_args.parse_args()
        return {"msg": args}, 201


class GetOne(Resource):
    def get(self, id):
        found = "No product founds with that id !"
        stat_code = 404
        for product in products:
            if product["id"] == id:
                found = product
                stat_code = 200

        return {"msg": found}, stat_code

    def put(self, id):
        return {"msg": id}, 200
