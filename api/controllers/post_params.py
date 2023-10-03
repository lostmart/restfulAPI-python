from flask_restful import reqparse

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
    "imgUrl",
    type=str,
    help="The image url of the product are required",
    required=True,
)

product_put_args.add_argument("Authorization", location="headers")
