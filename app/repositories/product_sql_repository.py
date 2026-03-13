from app.models.product import Product

class ProductSQLiteRepository:
    def __init__(self, connection):
        self.connection = connection

    def list_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products")

        rows = cursor.fetchall()

        products = []
        for row in rows:
            product = Product(
                id=row[0],
                name=row[1],
                desc=row[2],
                amount=row[3],
                price=row[4]
            )
            products.append(product)

        return products

    def find_by_name(self, product_name):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (product_name,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Product(
            id=row[0],
            name=row[1],
            desc=row[2],
            amount=row[3],
            price=row[4]
        )

    def create_product(self, name, desc, amount, price):

        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO products (name, desc, amount, price) VALUES (?, ?, ?, ?)",
            (name, desc, amount, price)
        )

        self.connection.commit()

        product_id = cursor.lastrowid

        return Product(
            id=product_id,
            name=name,
            desc=desc,
            amount=amount,
            price=price
        )
    
    def find_by_id(self, id: int):
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT * FROM products WHERE id=?",
            (id,)
        )

        row = cursor.fetchone()

        if row:
            return Product(
                id=row[0],
                name=row[1],
                desc=row[2],
                amount=row[3],
                price=row[4]
            )

    def update_name(self, id: int, new_name: str):
        cursor = self.connection.cursor()

        cursor.execute(
            "UPDATE products SET name=? WHERE id=?",
            (new_name, id)
        )

        self.connection.commit()

    def delete_product(self, product_id):
        cursor = self.connection.cursor()

        cursor.execute(
            "DELETE FROM products WHERE id = ?",
            (product_id,)
        )

        self.connection.commit()
        return cursor.rowcount
