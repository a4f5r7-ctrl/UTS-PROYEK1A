class Product:
    """Representasi entitas produk dalam sistem inventaris."""
    def __init__(self, product_id: str, name: str, price: float, stock: int, category: str):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __repr__(self) -> str:
        return f"Product(ID='{self.product_id}', Name='{self.name}', Price={self.price}, Stock={self.stock})"