import sqlite3


class ProductRepository:

    def get_connect(self):
        return sqlite3.connect("../db/order.sqlite")

    def product(self, productId):
        try:
            connect = self.get_connect()
            cursor = connect.cursor()
            cursor.execute(
                """select * from `product` where id = ?""", (productId,))
            product = cursor.fetchone()
            return product
        except Exception as error_product:
            print(f"error_product {error_product}")
        finally:
            connect.close()
