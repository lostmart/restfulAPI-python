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

    """

    def get(self):
        path = "api/db/test.db"
        db_handler = conn.DatabaseHandler(path)
        db_handler.connect()
        result = db_handler.get_data("products")
        db_handler.disconnect()
        return result

    def post(self):
        args = post_params.product_put_args.parse_args()

        # try to create a Product object based on the Product class
        try:
            new_product = ProductModel.Product(
                args["price"], args["description"], args["imgUrl"]
            )
            # insert data to the DB using the created objectd
            path = "api/db/test.db"
            db_handler = conn.DatabaseHandler(path)
            db_handler.connect()

            data_insert = db_handler.insert_data("products", vars(new_product))
            # check if the data insertion was succesfull
            if data_insert != "success!":
                return {"msg": str(data_insert)}, 500

            # print( vars(new_product))
        # throw en error if any arguments are wrong
        except Exception as e:
            error_msg = (
                "Object error! Something wrong with the argument parameter when creating the Product object: "
                + str(e)
            )
            return {"msg": error_msg}, 400

        # if all good the last product is sent back to the user (the new created product)
        new_created = db_handler.get_last_product("products")
        db_handler.disconnect()
        return {"msg": new_created}, 201


class GetOne(Resource):
    """
    Return one product based on the id parameter

    Arguments:
    product_id : int
    """

    def get(self, product_id):
        path = "api/db/test.db"
        db_handler = conn.DatabaseHandler(path)
        db_handler.connect()
        result = db_handler.get_one_product("products", product_id)
        if result:
            db_handler.disconnect()
            return result
        else:
            return {"msg": "no products found with that id"}, 404
