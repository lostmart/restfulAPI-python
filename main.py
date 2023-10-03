from flask import Flask
from swagger_config import swaggerui_blueprint

from flask_restful import Api, Resource

from api.routes.products import GetAll, GetOne
from api.routes.users import User


app = Flask(__name__)
api = Api(app)


# swagger config
app.register_blueprint(swaggerui_blueprint)


# home endpoint ('/')
class Welcome(Resource):
    def get(self):
        return {"msg": "This is a restAPI. All good and beautiful"}


api.add_resource(Welcome, "/")
api.add_resource(GetAll, "/api/products")
api.add_resource(GetOne, "/api/products/<int:product_id>")
# users
api.add_resource(User, "/api/users")



if __name__ == "__main__":
    app.run(debug=True)
