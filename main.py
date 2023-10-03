from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from flask_restful import Api, Resource

from api.routes.products import GetAll, GetOne


app = Flask(__name__)
api = Api(app)

SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "/static/swagger.json"  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Test application"},  # Swagger UI config overrides
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


# home endpoint ('/')
class Welcome(Resource):
    def get(self):
        return {"msg": "This is a restAPI. All good and beautiful"}


api.add_resource(Welcome, "/")
api.add_resource(GetAll, "/api/products")
api.add_resource(GetOne, "/api/products/<int:product_id>")


if __name__ == "__main__":
    app.run(debug=True)
