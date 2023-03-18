from model.product import Product
from repository.repository import Repository

class ProductRepository(Repository):

    def product(self, productId):
        try:
            connect = self.get_connect()
            cursor = connect.cursor()
            cursor.execute(
                """select * from `product` where id = ?""", (productId,))
            product = cursor.fetchone()
            return Product(product)
        except Exception as error_product:
            print(f"error_product {error_product}")
        finally:
            connect.close()
