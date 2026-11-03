from repository import HashTableInventory
from manager import InventoryManager

def main():
    print("=== SISTEM MANAJEMEN INVENTARIS PRODUK E-COMMERCE ===")
    
    # Inisialisasi Repositori Hash Table & Manager
    repo = HashTableInventory()
    inventory_system = InventoryManager(repo)

    print("\n1. Mendaftarkan Produk Baru")
    inventory_system.register_product("PRD-001", "Laptop Gaming Pro", 15000000, 50, "Elektronik")
    inventory_system.register_product("PRD-002", "Mouse Wireless", 250000, 200, "Aksesoris")
    inventory_system.register_product("PRD-003", "Mechanical Keyboard", 850000, 120, "Aksesoris")
    inventory_system.display_total_products()

    print("\n2. Mencari Detail Produk saat Diakses Pelanggan")
    inventory_system.find_product("PRD-001")
    inventory_system.find_product("PRD-999")

    print("\n3. Menghapus Produk dari Peredaran")
    inventory_system.delete_product("PRD-002")
    inventory_system.display_total_products()

    print("\n4. Verifikasi Pencarian Setelah Produk Dihapus")
    inventory_system.find_product("PRD-002")

if __name__ == "__main__":
    main()