from typing import Dict, Optional
from models import Product
from interfaces import InventoryRepositoryADT

class HashTableInventory(InventoryRepositoryADT):
    """
    Implementasi konkret ADT menggunakan Hash Table (Python Dict).
    Sangat efisien untuk skala jutaan data dengan akses O(1).
    """
    def __init__(self):
        self._storage: Dict[str, Product] = {}

    def add_product(self, product: Product) -> bool:
        if product.product_id in self._storage:
            return False
        self._storage[product.product_id] = product
        return True

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        return self._storage.get(product_id, None)

    def remove_product(self, product_id: str) -> bool:
        if product_id in self._storage:
            del self._storage[product_id]
            return True
        return False

    def get_total_count(self) -> int:
        return len(self._storage)