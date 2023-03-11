import sqlite3

class ProductRepository:
    
    def __init__(self) -> None:
        connect = sqlite3.connect("db/order.sqlite")
        self.cursor = connect.cursor()

    def product(self, productId):
        self.cursor.execute("select * from `product` where id = ?", [productId])
        product = self.cursor.fetchone()
        print(product)
        return product
