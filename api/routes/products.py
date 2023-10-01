from flask_restful import Resource

# import post parameters from the controller
import api.controllers.post_params as post_params

# import Product model Class
import api.models.product as ProductModel

# import DB handler with all required methods
import api.db.connectionhadler as conn


class GetAll(Resource):
    """
    Returns the result of fetchall() from the cursor
    The class DatabaseHandler handles the connection, the curor creation
    and its method get_data executes and commit a query SELECT * from the table passed as an argument

    Arguments:
    table_name: string (name of the table that you want to query within the DB)
    """

    def get(self):
        path = "api/db/test.db"
        db_handler = conn.DatabaseHandler(path)
        db_handler.connect()
        result = db_handler.get_data("products")
        return result

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
