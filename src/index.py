import psycopg2
import pandas as pd
def create_connection():
    conn = psycopg2.connect(
        dbname="GrocerySystem",
        user="",
        password="",
        host="",
        port=""
    )
    return conn

# Supplier CRUD operations
def create_supplier(supplier_name, contact_info, address):
    print("Creating supplier...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO suppliers (supplier_name, contact_info, address) VALUES (%s, %s, %s)", (supplier_name, contact_info, address))
    conn.commit()
    cursor.close()
    conn.close()
    print("Supplier created.")

def read_suppliers():
    print("Reading suppliers...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT supplier_id, supplier_name, contact_info, address FROM suppliers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    print("Suppliers read.")
    return rows

def update_supplier(supplier_id, supplier_name, contact_info, address):
    print("Updating supplier...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE suppliers SET supplier_name = %s, contact_info = %s, address = %s WHERE supplier_id = %s", (supplier_name, contact_info, address, supplier_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Supplier updated.")

def delete_supplier(supplier_id):
    print("Deleting supplier...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM suppliers WHERE supplier_id = %s", (supplier_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Supplier deleted.")

# Product CRUD operations
def create_product(product_name, category, price, stock_quantity, seller_id):
    print("Creating product...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (product_name, category, price, stock_quantity, seller_id) VALUES (%s, %s, %s, %s, %s)", (product_name, category, price, stock_quantity, seller_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Product created.")

def read_products():
    print("Reading products...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, product_name, category, price, stock_quantity, seller_id FROM products")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    print("Products read.")
    return rows

def update_product(product_id, product_name, category, price, stock_quantity, seller_id):
    print("Updating product...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET product_name = %s, category = %s, price = %s, stock_quantity = %s, seller_id = %s WHERE product_id = %s", (product_name, category, price, stock_quantity, seller_id, product_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Product updated.")

def delete_product(product_id):
    print("Deleting product...")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Product deleted.")

# Test functions
def test_create_and_read_supplier():
    print("Running test_create_and_read_supplier...")
    create_supplier("Test Supplier", "test@example.com", "123 Test St, Testville")
    suppliers = read_suppliers()
    assert any(supplier[1] == "Test Supplier" and supplier[3] == "123 Test St, Testville" for supplier in suppliers)
    print("test_create_and_read_supplier passed")

def test_update_supplier():
    print("Running test_update_supplier...")
    create_supplier("Update Test", "update@example.com", "456 Update Rd, Update City")
    suppliers = read_suppliers()
    supplier_id = next(supplier[0] for supplier in suppliers if supplier[1] == "Update Test")
    update_supplier(supplier_id, "Updated Supplier", "updated@example.com", "789 Updated Ave, Update City")
    suppliers = read_suppliers()
    assert any(supplier[1] == "Updated Supplier" and supplier[3] == "789 Updated Ave, Update City" for supplier in suppliers)
    print("test_update_supplier passed")

def test_delete_supplier():
    print("Running test_delete_supplier...")
    create_supplier("Delete Test", "delete@example.com", "101 Delete St, Deleteville")
    suppliers = read_suppliers()
    supplier_id = next(supplier[0] for supplier in suppliers if supplier[1] == "Delete Test")
    delete_supplier(supplier_id)
    suppliers = read_suppliers()
    assert not any(supplier[0] == supplier_id for supplier in suppliers)
    print("test_delete_supplier passed")

def test_create_product():
    print("Running test_create_and_read_product...")
    create_product("Test Product", "Category A", 9.99, 100, 1)  # Assuming seller_id 1 exists
    # products = read_products()
    # assert any(product[1] == "Test Product" and product[2] == "Category A" for product in products)
    # print("test_create_and_read_product passed")

def test_update_product():
    print("Running test_update_product...")
    create_product("Update Product", "Category B", 19.99, 50, 1)  # Assuming seller_id 1 exists
    products = read_products()
    product_id = next(product[0] for product in products if product[1] == "Update Product")
    update_product(product_id, "Updated Product", "Category B", 29.99, 60, 1)
    products = read_products()
    assert any(product[1] == "Updated Product" and product[3] == 29.99 for product in products)
    print("test_update_product passed")

def test_delete_product():
    print("Running test_delete_product...")
    create_product("Delete Product", "Category C", 5.99, 20, 1)  # Assuming seller_id 1 exists
    products = read_products()
    product_id = next(product[0] for product in products if product[1] == "Delete Product")
    delete_product(product_id)
    products = read_products()
    assert not any(product[0] == product_id for product in products)
    print("test_delete_product passed")

if __name__ == "__main__":
    test_create_and_read_supplier()
    test_update_supplier()
    test_delete_supplier()
    test_create_product()
    test_update_product()
    test_delete_product()
    print("All tests passed!")


data = read_suppliers()

print(data)