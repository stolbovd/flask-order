from flask import Flask, redirect, url_for, request, jsonify
from routes.product import product_bp
from routes.test import test_bp


# инициализация классов
app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(product_bp)


# запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
