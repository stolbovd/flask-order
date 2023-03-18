from flask import Blueprint, jsonify

from repository.productRepository import ProductRepository

productRepository = ProductRepository()

product_bp = Blueprint('product', __name__)

@product_bp.route("/product/<productId>", methods=["GET"])
def route_product(productId):
    product = productRepository.product(productId)
    print(product, productId)
    return jsonify(product)
