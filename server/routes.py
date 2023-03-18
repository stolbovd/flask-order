from flask import Flask, jsonify
from repository import ProductRepository


productRepository = ProductRepository()

# инициализация классов
app = Flask(__name__)


@app.route("/test")
def route_test():
    return jsonify({'a': 2})


@app.route("/product/<productId>", methods=["GET"])
def route_product(productId):
    product = productRepository.product(productId)
    print(product, productId)
    return jsonify(product)
