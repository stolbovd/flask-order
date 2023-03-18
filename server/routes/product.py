from flask import Blueprint, jsonify
from repository import ProductRepository


productRepository = ProductRepository()

product_bp = Blueprint('product', __name__)

@product_bp.route("/product/<productId>", methods=["GET"])
def route_product(productId):
    product = productRepository.product(productId)
    # print(product, productId)
    response = jsonify(product)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@product_bp.route("/product", methods=["GET"])
def route_all_products():
    products = productRepository.products()
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
