from flask_restful import reqparse

user_params = reqparse.RequestParser(bundle_errors=True)  # shows multiple error

user_params.add_argument(
    "first_name",
    type=str,
    help="The first name cannot be empty and needs to be a string",
    required=True,
)


user_params.add_argument(
    "last_name",
    type=str,
    help="The last name cannot be empty and needs to be a string",
    required=True,
)

user_params.add_argument(
    "email",
    type=str,
    help="The email cannot be empty and needs to be a string",
    required=True,
)

user_params.add_argument(
    "password",
    type=str,
    help="The password cannot be empty and needs to be a string",
    required=True,
)