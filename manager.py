from typing import Optional
from models import Product
from interfaces import InventoryRepositoryADT

class InventoryManager:
    """
    Manager class yang mengelola logika bisnis inventaris.
    Menerapkan Dependency Inversion dengan menerima InventoryRepositoryADT.
    """
    def __init__(self, repository: InventoryRepositoryADT):
        self._repo = repository

    def register_product(self, product_id: str, name: str, price: float, stock: int, category: str) -> bool:
        new_product = Product(product_id, name, price, stock, category)
        success = self._repo.add_product(new_product)
        if success:
            print(f"[SUCCESS] Produk '{name}' (ID: {product_id}) berhasil didaftarkan.")
        else:
            print(f"[FAILED] Produk ID '{product_id}' sudah terdaftar dalam sistem.")
        return success

    def find_product(self, product_id: str) -> Optional[Product]:
        product = self._repo.get_product_by_id(product_id)
        if product:
            print(f"[FOUND] Detail Produk: {product}")
        else:
            print(f"[NOT FOUND] Produk dengan ID '{product_id}' tidak ditemukan.")
        return product

    def delete_product(self, product_id: str) -> bool:
        success = self._repo.remove_product(product_id)
        if success:
            print(f"[DELETED] Produk dengan ID '{product_id}' berhasil dihapus dari inventaris.")
        else:
            print(f"[FAILED] Gagal menghapus. Produk ID '{product_id}' tidak ditemukan.")
        return success

    def display_total_products(self):
        print(f"[INFO] Total jenis produk terdaftar saat ini: {self._repo.get_total_count()}")