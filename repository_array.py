from typing import List, Optional
from models import Product
from interfaces import InventoryRepositoryADT

class ArrayListInventory(InventoryRepositoryADT):
    """
    Implementasi ADT Inventaris menggunakan Array-based List (Python List).
    Akses dan pencarian linier O(n).
    """
    def __init__(self):
        self._storage: List[Product] = []

    def add_product(self, product: Product) -> bool:
        # Cek apakah produk dengan ID yang sama sudah ada (O(n))
        if self.get_product_by_id(product.product_id) is not None:
            return False
        # Append ke akhir array: O(1)
        self._storage.append(product)
        return True

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        # Linear Search: O(n)
        for product in self._storage:
            if product.product_id == product_id:
                return product
        return None

    def remove_product(self, product_id: str) -> bool:
        # Mencari indeks elemen lalu menghapusnya: O(n)
        for i, product in enumerate(self._storage):
            if product.product_id == product_id:
                del self._storage[i]  # Menghapus dan menggeser elemen: O(n)
                return True
        return False

    def get_total_count(self) -> int:
        return len(self._storage)