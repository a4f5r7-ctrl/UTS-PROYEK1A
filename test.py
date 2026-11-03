import time
from repository import HashTableInventory
from repository_array import ArrayListInventory
from repository_linked_list import LinkedListInventory
from models import Product

# 1. Siapkan data uji (misal: 20.000 produk)
TOTAL_DATA = 1000000
target_id = f"PRD-{TOTAL_DATA}"  # Produk yang berada di urutan paling akhir (worst-case search)

hash_repo = HashTableInventory()
array_repo = ArrayListInventory()
linked_repo = LinkedListInventory()

for i in range(1, TOTAL_DATA + 1):
    p = Product(f"PRD-{i}", f"Barang {i}", 10000, 10, "Umum")
    hash_repo.add_product(p)
    array_repo.add_product(p)
    linked_repo.add_product(p)

print(f"=== UJI KECEPATAN PENCARIAN ({TOTAL_DATA:,} DATA) ===")

# Test Hash Table
start = time.perf_counter()
hash_repo.get_product_by_id(target_id)
end = time.perf_counter()
hash_time = (end - start) * 1000
print(f"Hash Table (O(1))       : {hash_time:.4f} ms")

# Test Array-based List
start = time.perf_counter()
array_repo.get_product_by_id(target_id)
end = time.perf_counter()
array_time = (end - start) * 1000
print(f"Array-based List (O(n)) : {array_time:.4f} ms")

# Test Linked List
start = time.perf_counter()
linked_repo.get_product_by_id(target_id)
end = time.perf_counter()
linked_time = (end - start) * 1000
print(f"Linked List (O(n))      : {linked_time:.4f} ms")