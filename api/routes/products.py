from flask_restful import Resource

# import post parameters from the controller
import api.controllers.post_params as post_params

# import the connection and its cursor
import api.db.connection as conn


# Execute the SQL query to retrieve all products
conn.cursor.execute("SELECT * FROM products")

# Fetch the results
products = conn.cursor.fetchall()


class GetAll(Resource):
    def get(self):
        return products

    def post(self):
        args = post_params.product_put_args.parse_args()
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
