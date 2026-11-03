from abc import ABC, abstractmethod
from typing import Optional
from models import Product

class InventoryRepositoryADT(ABC):
    """
    Abstract Data Type (ADT) untuk Repositori Inventaris.
    Mendefinisikan kontrak operasi dasar tanpa terikat implementasi spesifik.
    """

    @abstractmethod
    def add_product(self, product: Product) -> bool:
        """Menambahkan/mendaftarkan produk baru. Target: O(1)"""
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Mencari detail produk berdasarkan ID Produk. Target: O(1)"""
        pass

    @abstractmethod
    def remove_product(self, product_id: str) -> bool:
        """Menghapus produk dari inventaris berdasarkan ID Produk. Target: O(1)"""
        pass

    @abstractmethod
    def get_total_count(self) -> int:
        """Mendapatkan jumlah total jenis produk yang terdaftar."""
        pass