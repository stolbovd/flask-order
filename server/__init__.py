from flask import Flask, redirect, url_for, request, jsonify
from repository import ProductRepository

# инициализация классов
app = Flask(__name__)

@app.route("/test")
def route_test():
    return jsonify({'a': 2})

productRepository = ProductRepository()

@app.route("/product/<productId>", methods=["GET"])
def route_product(productId):
    print(productId)
    product = productRepository.product(productId)
    print(product, productId)
    return jsonify(product)

# запуск приложения
#if __name__ == "__main__":
app.run(debug=True)