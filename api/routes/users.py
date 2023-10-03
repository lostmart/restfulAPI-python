from flask_restful import Resource
from api.models.user import NewUser
from api.controllers.users_params import user_params


class User(Resource):
    def post(self):
        # create a new user (sig-up) return new user?
        user_args = user_params.parse_args()
        print(user_args)
        
        # try to create a Product object based on the Product class
        try:
            new_user = NewUser(user_args["first_name"], user_args["last_name"], user_args["email"], user_args["password"])
        except Exception as e:
            error_msg = (
                "Object error! Something wrong with the argument parameter when creating the User object: "
                + str(e)
            )
            return {"msg": error_msg}, 400

        return { "msg": vars(new_user) }, 201
    


    def get(self):
        # log in user (return a token)

      return {"msg": "logging user ..."}

    def put(self):
        # modify as user (returned modified user)
        pass


    def delete(self):
        # delete a user
        pass