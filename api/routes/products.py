from flask_restful import Resource

# import post parameters from the controller
import api.controllers.post_params as post_params

# import Product model Class
import api.models.product as ProductModel

# import the connection and its cursor
import api.db.connection as conn


# Execute the SQL query to retrieve all products
conn.cursor.execute("SELECT * FROM products")

# Fetch the results
products = conn.cursor.fetchall()

def execute_fetch():
    # Execute the SQL query to retrieve all products
    conn.cursor.execute("SELECT * FROM products")

    # Fetch the results
    return conn.cursor.fetchall()



class GetAll(Resource):
    def get(self):
        return execute_fetch()

    def post(self):
        args = post_params.product_put_args.parse_args()

        # try to create a Product object based on the Product class
        try:
            new_product = ProductModel.Product(
                args["price"], args["description"], args["images"]
            )
        # throw en error if any arguments are wrong
        except Exception as e:
            error_msg = "Object error! " + str(e)
            return {"msg": error_msg}, 500

        return {"msg": vars(new_product)}, 201


class GetOne(Resource):
    pass
    # def get(self, id):
    #     found = "No product founds with that id !"
    #     stat_code = 404
    #     for product in products:
    #         if product["id"] == id:
    #             found = product
    #             stat_code = 200

    #     return {"msg": found}, stat_code

    # def put(self, id):
    #     return {"msg": id}, 200
