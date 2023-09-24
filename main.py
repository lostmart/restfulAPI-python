from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "Author 1"
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Author 2"
    }
]


# home endpoint ('/')
@app.route("/")
def index():
    return jsonify({"msg": "This is a restAPI. All good and beautiful"})

# products endpoint ('/products')
@app.route("/products")
def get_products():
    return jsonify(products) 


# single product
@app.route("/products/<int:id>")
def single_product(id):
    found = 'No product found with that id !'
    stat_code = 404
    for product in products:
        print(type(id), type(product["id"]))
        if product["id"] == id:
            found = product
            stat_code = 200
        
    
    return jsonify({"msg": found}), stat_code

if __name__ == "__main__":
    app.run(debug=True)
