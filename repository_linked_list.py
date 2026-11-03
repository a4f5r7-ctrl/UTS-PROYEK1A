from typing import Optional
from models import Product
from interfaces import InventoryRepositoryADT

class Node:
    """Representasi elemen/node pada Singly Linked List."""
    def __init__(self, data: Product):
        self.data: Product = data
        self.next: Optional['Node'] = None


class LinkedListInventory(InventoryRepositoryADT):
    """
    Implementasi ADT Inventaris menggunakan Linked List.
    Akses dan penelusuran O(n), penambahan di Head O(1).
    """
    def __init__(self):
        self._head: Optional[Node] = None
        self._count: int = 0

    def add_product(self, product: Product) -> bool:
        # Cek duplikasi terlebih dahulu: O(n)
        if self.get_product_by_id(product.product_id) is not None:
            return False

        # Penambahan di posisi paling depan (Head Insertion): O(1)
        new_node = Node(product)
        new_node.next = self._head
        self._head = new_node
        self._count += 1
        return True

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        # Traversal/Penelusuran dari Head: O(n)
        current = self._head
        while current:
            if current.data.product_id == product_id:
                return current.data
            current = current.next
        return None

    def remove_product(self, product_id: str) -> bool:
        current = self._head
        previous: Optional[Node] = None

        # Penelusuran mencari node yang ingin dihapus: O(n)
        while current:
            if current.data.product_id == product_id:
                if previous is None:
                    # Menghapus node pertama (Head)
                    self._head = current.next
                else:
                    # Menghubungkan node sebelumnya ke node setelahnya
                    previous.next = current.next
                self._count -= 1
                return True
            previous = current
            current = current.next

        return False

    def get_total_count(self) -> int:
        return self._count