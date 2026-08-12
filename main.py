'''from database import get_connection


def view_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")

    products = cursor.fetchall()

    print("\n========================= PRODUCTS ================================")

    for product in products:
        print(product)

    cursor.close()
    connection.close()


view_products()'''


#Making the output more readable, formatted and user friendly
'''from database import get_connection


def view_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity, ReorderLevel
        FROM Products
    """)

    products = cursor.fetchall()

    print("\n===========================================================")
    print("                     PRODUCT LIST")
    print("===========================================================")
    print(f"{'ID':<5}{'Product Name':<22}{'Price':<15}{'Stock':<10}{'Reorder':<10}")
    print("-" * 62)

    for product in products:
        print(
            f"{product.ProductID:<5}"
            f"{product.ProductName:<22}"
            f"Rs.{product.Price:<12.2f}"
            f"{product.StockQuantity:<10}"
            f"{product.ReorderLevel:<10}"
        )

    print("=" * 62)

    cursor.close()
    connection.close()


view_products()'''

from database import get_connection

#View Products
def view_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity, ReorderLevel
        FROM Products
    """)

    products = cursor.fetchall()

    print("\n===========================================================")
    print("                     PRODUCT LIST")
    print("===========================================================")
    print(f"{'ID':<5}{'Product Name':<22}{'Price':<15}{'Stock':<10}{'Reorder':<10}")
    print("-" * 62)

    for product in products:
        print(
            f"{product.ProductID:<5}"
            f"{product.ProductName:<22}"
            f"Rs.{product.Price:<12.2f}"
            f"{product.StockQuantity:<10}"
            f"{product.ReorderLevel:<10}"
        )

    print("=" * 62)

    cursor.close()
    connection.close()

#Add Product
def add_product():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n========== ADD PRODUCT ==========")

    product_name = input("Enter product name: ")

    # Validate Category ID
    while True:
        try:
            category_id = int(input("Enter category ID: "))

            if category_id <= 0:
                print("Category ID must be greater than 0.")
                continue

            cursor.execute(
                "SELECT CategoryID FROM Categories WHERE CategoryID = ?",
                category_id
            )

            if cursor.fetchone() is None:
                print("Category ID does not exist. Please try again.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Validate Supplier ID
    while True:
        try:
            supplier_id = int(input("Enter supplier ID: "))

            if supplier_id <= 0:
                print("Supplier ID must be greater than 0.")
                continue

            cursor.execute(
                "SELECT SupplierID FROM Suppliers WHERE SupplierID = ?",
                supplier_id
            )

            if cursor.fetchone() is None:
                print("Supplier ID does not exist. Please try again.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Validate Price
    while True:
        try:
            price = float(input("Enter price: "))

            if price <= 0:
                print("Price must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid price.")

    # Validate Stock Quantity
    while True:
        try:
            stock_quantity = int(input("Enter stock quantity: "))

            if stock_quantity < 0:
                print("Stock quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Validate Reorder Level
    while True:
        try:
            reorder_level = int(input("Enter reorder level: "))

            if reorder_level < 0:
                print("Reorder level cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    query = """
        INSERT INTO Products
        (ProductName, CategoryID, SupplierID, Price, StockQuantity, ReorderLevel)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(
        query,
        product_name,
        category_id,
        supplier_id,
        price,
        stock_quantity,
        reorder_level
    )

    connection.commit()

    print("\nProduct added successfully!")

    cursor.close()
    connection.close()

#Search Product
def search_product():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n========== SEARCH PRODUCT ==========")

    search_name = input("Enter product name to search: ")

    query = """
        SELECT ProductID, ProductName, Price, StockQuantity, ReorderLevel
        FROM Products
        WHERE ProductName LIKE ?
    """

    cursor.execute(query, "%" + search_name + "%")

    products = cursor.fetchall()

    if not products:
        print("\nNo products found.")

    else:
        print("\n===========================================================")
        print("                     SEARCH RESULTS")
        print("===========================================================")
        print(f"{'ID':<5}{'Product Name':<22}{'Price':<15}{'Stock':<10}{'Reorder':<10}")
        print("-" * 62)

        for product in products:
            print(
                f"{product.ProductID:<5}"
                f"{product.ProductName:<22}"
                f"Rs.{product.Price:<12.2f}"
                f"{product.StockQuantity:<10}"
                f"{product.ReorderLevel:<10}"
            )

        print("=" * 62)

    cursor.close()
    connection.close()

#Update Product
def update_product():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n========== UPDATE PRODUCT ==========")

    product_name = input("Enter product name to update: ")

    # Check if product exists
    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity, ReorderLevel
        FROM Products
        WHERE ProductName LIKE ?
    """, "%" + product_name + "%")

    products = cursor.fetchall()

    if not products:
        print("\nProduct not found.")
        cursor.close()
        connection.close()
        return

    # If more than one product matches
    if len(products) > 1:
        print("\nMultiple products found:")

        for product in products:
            print(
                f"ID: {product.ProductID} | "
                f"Name: {product.ProductName} | "
                f"Price: Rs.{product.Price:.2f} | "
                f"Stock: {product.StockQuantity}"
            )

        print("\nPlease enter a more specific product name.")
        cursor.close()
        connection.close()
        return

    product = products[0]

    print(f"\nProduct found: {product.ProductName}")
    print(f"Current Price: Rs.{product.Price:.2f}")
    print(f"Current Stock: {product.StockQuantity}")
    print(f"Current Reorder Level: {product.ReorderLevel}")

    # New price
    while True:
        try:
            new_price = float(input("\nEnter new price: "))

            if new_price <= 0:
                print("Price must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid price.")

    # New stock quantity
    while True:
        try:
            new_stock = int(input("Enter new stock quantity: "))

            if new_stock < 0:
                print("Stock quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # New reorder level
    while True:
        try:
            new_reorder = int(input("Enter new reorder level: "))

            if new_reorder < 0:
                print("Reorder level cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Update product
    cursor.execute("""
        UPDATE Products
        SET Price = ?,
            StockQuantity = ?,
            ReorderLevel = ?
        WHERE ProductID = ?
    """, new_price, new_stock, new_reorder, product.ProductID)

    connection.commit()

    print("\nProduct updated successfully!")

    cursor.close()
    connection.close()

#Delete Product
def delete_product():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n========== DELETE PRODUCT ==========")

    product_name = input("Enter product name to delete: ")

    # Check if product exists
    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity
        FROM Products
        WHERE ProductName LIKE ?
    """, "%" + product_name + "%")

    products = cursor.fetchall()

    if not products:
        print("\nProduct not found.")
        cursor.close()
        connection.close()
        return

    # If multiple products match
    if len(products) > 1:
        print("\nMultiple products found:")

        for product in products:
            print(
                f"ID: {product.ProductID} | "
                f"Name: {product.ProductName} | "
                f"Price: Rs.{product.Price:.2f} | "
                f"Stock: {product.StockQuantity}"
            )

        print("\nPlease enter a more specific product name.")
        cursor.close()
        connection.close()
        return

    product = products[0]

    print(f"\nProduct found: {product.ProductName}")
    print(f"Price: Rs.{product.Price:.2f}")
    print(f"Stock: {product.StockQuantity}")

    confirmation = input(
        "\nAre you sure you want to delete this product? (yes/no): "
    )

    if confirmation.lower() == "yes":

        cursor.execute("""
            DELETE FROM Products
            WHERE ProductID = ?
        """, product.ProductID)

        connection.commit()

        print("\nProduct deleted successfully!")

    else:
        print("\nDelete cancelled.")

    cursor.close()
    connection.close()

#Low Stock Alert
def low_stock_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity, ReorderLevel
        FROM Products
        WHERE StockQuantity <= ReorderLevel
        ORDER BY StockQuantity ASC
    """)

    products = cursor.fetchall()

    print("\n===========================================================")
    print("                     LOW STOCK ALERT")
    print("===========================================================")

    if not products:
        print("All products have sufficient stock.")
    else:
        print(f"{'ID':<5}{'Product Name':<22}{'Price':<15}{'Stock':<10}{'Reorder':<10}")
        print("-" * 62)

        for product in products:
            print(
                f"{product.ProductID:<5}"
                f"{product.ProductName:<22}"
                f"Rs.{product.Price:<12.2f}"
                f"{product.StockQuantity:<10}"
                f"{product.ReorderLevel:<10}"
            )

        print("\n⚠ These products need restocking!")

    print("=" * 62)

    cursor.close()
    connection.close()

# Purchase Product
def purchase_product():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n========== PURCHASE PRODUCT ==========")

    product_name = input("Enter product name: ")

    # Find product
    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity
        FROM Products
        WHERE ProductName LIKE ?
    """, "%" + product_name + "%")

    products = cursor.fetchall()

    if not products:
        print("\nProduct not found.")
        cursor.close()
        connection.close()
        return

    # Handle multiple matching products
    if len(products) > 1:
        print("\nMultiple products found:")

        for product in products:
            print(
                f"ID: {product.ProductID} | "
                f"Name: {product.ProductName} | "
                f"Stock: {product.StockQuantity}"
            )

        print("\nPlease enter a more specific product name.")

        cursor.close()
        connection.close()
        return

    product = products[0]

    print(f"\nProduct found: {product.ProductName}")
    print(f"Price per unit: Rs.{product.Price:.2f}")
    print(f"Current Stock: {product.StockQuantity}")

    try:
        # Purchase quantity
        quantity = int(input("Enter purchase quantity: "))

        if quantity <= 0:
            print("\nQuantity must be greater than 0.")
            cursor.close()
            connection.close()
            return

        # Get suppliers
        cursor.execute("""
            SELECT SupplierID, SupplierName
            FROM Suppliers
            ORDER BY SupplierID
        """)

        suppliers = cursor.fetchall()

        if not suppliers:
            print("\nNo suppliers available.")
            cursor.close()
            connection.close()
            return

        # Display suppliers
        print("\nAvailable Suppliers:")
        print("-" * 40)

        for i, supplier in enumerate(suppliers, start=1):
            print(
                f"{i}. {supplier.SupplierName}"
            )

        print("-" * 40)

        # Choose supplier
        supplier_choice = int(
            input("Choose supplier: ")
        )

        if supplier_choice < 1 or supplier_choice > len(suppliers):
            print("\nInvalid supplier choice.")
            cursor.close()
            connection.close()
            return

        # Get selected supplier
        selected_supplier = suppliers[supplier_choice - 1]

        supplier_id = selected_supplier.SupplierID
        supplier_name = selected_supplier.SupplierName

        # Calculate total amount
        total_amount = product.Price * quantity

        print(f"\nSelected Supplier: {supplier_name}")
        print(f"Price per Unit: Rs.{product.Price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: Rs.{total_amount:.2f}")

        # Increase stock
        cursor.execute("""
            UPDATE Products
            SET StockQuantity = StockQuantity + ?
            WHERE ProductID = ?
        """, quantity, product.ProductID)

        # Record transaction
        cursor.execute("""
            INSERT INTO Transactions
            (
                ProductID,
                ProductName,
                CustomerID,
                CustomerName,
                SupplierID,
                SupplierName,
                TransactionType,
                Quantity,
                TransactionDate,
                TotalAmount
            )
            VALUES (?, ?, NULL, NULL, ?, ?, 'Purchase', ?, GETDATE(), ?)
        """,
        product.ProductID,
        product.ProductName,
        supplier_id,
        supplier_name,
        quantity,
        total_amount)

        connection.commit()

        # Calculate new stock
        new_stock = product.StockQuantity + quantity

        print("\nPurchase recorded successfully!")
        print(f"Product: {product.ProductName}")
        print(f"Supplier: {supplier_name}")
        print(f"Price per Unit: Rs.{product.Price:.2f}")
        print(f"Previous Stock: {product.StockQuantity}")
        print(f"Purchased Quantity: {quantity}")
        print(f"Total Amount: Rs.{total_amount:.2f}")
        print(f"New Stock: {new_stock}")

    except ValueError:
        print("\nPlease enter valid numbers.")

    except Exception as e:
        connection.rollback()
        print("\nAn error occurred:", e)

    cursor.close()
    connection.close()

# Sale Product
def sale_product():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n========== SALE PRODUCT ==========")

    product_name = input("Enter product name: ")

    # Find product
    cursor.execute("""
        SELECT ProductID, ProductName, Price, StockQuantity
        FROM Products
        WHERE ProductName LIKE ?
    """, ("%" + product_name + "%",))

    products = cursor.fetchall()

    if not products:
        print("\nProduct not found.")
        cursor.close()
        connection.close()
        return

    # Handle multiple matching products
    if len(products) > 1:
        print("\nMultiple products found:")

        for product in products:
            print(
                f"ID: {product.ProductID} | "
                f"Name: {product.ProductName} | "
                f"Price: Rs.{product.Price:.2f} | "
                f"Stock: {product.StockQuantity}"
            )

        product_name = input("\nEnter the exact product name: ")

        cursor.execute("""
            SELECT ProductID, ProductName, Price, StockQuantity
            FROM Products
            WHERE ProductName = ?
        """, (product_name,))

        product = cursor.fetchone()

    else:
        product = products[0]

    if not product:
        print("\nProduct not found.")
        cursor.close()
        connection.close()
        return

    product_id = product.ProductID
    product_name = product.ProductName
    price = product.Price
    current_stock = product.StockQuantity

    print(f"\nProduct found: {product_name}")
    print(f"Price per unit: Rs.{price:.2f}")
    print(f"Current Stock: {current_stock}")

    try:
        # Sale quantity
        quantity = int(input("Enter sale quantity: "))

        # Check quantity
        if quantity <= 0:
            print("\nSale quantity must be greater than 0.")
            cursor.close()
            connection.close()
            return

        # Check stock
        if quantity > current_stock:
            print("\nInsufficient stock!")
            print(f"Available stock: {current_stock}")
            cursor.close()
            connection.close()
            return

        # Display available customers
        cursor.execute("""
            SELECT CustomerID, CustomerName
            FROM Customers
            ORDER BY CustomerID
        """)

        customers = cursor.fetchall()

        if not customers:
            print("\nNo customers available.")
            cursor.close()
            connection.close()
            return

        print("\nAvailable Customers:")
        print("-" * 40)

        for i, customer in enumerate(customers, start=1):
            print(f"{i}. {customer.CustomerName}")

        print("-" * 40)

        # Choose customer
        customer_choice = int(input("Choose customer: "))

        if customer_choice < 1 or customer_choice > len(customers):
            print("\nInvalid customer choice.")
            cursor.close()
            connection.close()
            return

        # Get selected customer
        selected_customer = customers[customer_choice - 1]

        customer_id = selected_customer.CustomerID
        customer_name = selected_customer.CustomerName

        # Calculate total amount
        total_amount = price * quantity

        print(f"\nSelected Customer: {customer_name}")
        print(f"Price per Unit: Rs.{price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: Rs.{total_amount:.2f}")

        # Reduce stock
        new_stock = current_stock - quantity

        cursor.execute("""
            UPDATE Products
            SET StockQuantity = ?
            WHERE ProductID = ?
        """, (new_stock, product_id))

        # Record transaction
        cursor.execute("""
            INSERT INTO Transactions
            (
                ProductID,
                ProductName,
                CustomerID,
                CustomerName,
                SupplierID,
                SupplierName,
                TransactionType,
                Quantity,
                TransactionDate,
                TotalAmount
            )
            VALUES (?, ?, ?, ?, NULL, NULL, 'Sale', ?, GETDATE(), ?)
        """,
        product_id,
        product_name,
        customer_id,
        customer_name,
        quantity,
        total_amount)

        connection.commit()

        # Success message
        print("\nSale recorded successfully!")
        print(f"Product: {product_name}")
        print(f"Customer: {customer_name}")
        print(f"Price per Unit: Rs.{price:.2f}")
        print(f"Previous Stock: {current_stock}")
        print(f"Sold Quantity: {quantity}")
        print(f"Total Amount: Rs.{total_amount:.2f}")
        print(f"New Stock: {new_stock}")

    except ValueError:
        print("\nPlease enter valid numbers.")

    except Exception as e:
        connection.rollback()
        print("\nAn error occurred:", e)

    cursor.close()
    connection.close()

# View Transaction History
def view_transactions():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            TransactionID,
            ProductName,
            CustomerName,
            SupplierName,
            TransactionType,
            Quantity,
            TotalAmount,
            TransactionDate
        FROM Transactions
        ORDER BY TransactionID
    """)

    transactions = cursor.fetchall()

    print("\n" + "=" * 110)
    print("                         TRANSACTION HISTORY")
    print("=" * 110)

    if not transactions:
        print("No transactions found.")
    else:
        print(
            f"{'ID':<5}"
            f"{'Product':<20}"
            f"{'Customer':<18}"
            f"{'Supplier':<22}"
            f"{'Type':<12}"
            f"{'Qty':<6}"
            f"{'Total':<14}"
            f"{'Date':<20}"
        )

        print("-" * 110)

        for transaction in transactions:

            customer = transaction.CustomerName or "-"
            supplier = transaction.SupplierName or "-"

            transaction_date = transaction.TransactionDate.strftime(
                "%Y-%m-%d"
            )

            print(
                f"{transaction.TransactionID:<5}"
                f"{transaction.ProductName:<20}"
                f"{customer:<18}"
                f"{supplier:<22}"
                f"{transaction.TransactionType:<12}"
                f"{transaction.Quantity:<6}"
                f"Rs.{transaction.TotalAmount:<11.2f}"
                f"{transaction_date:<20}"
            )

    print("=" * 110)

    cursor.close()
    connection.close()

#Main Menu
def main_menu():

    while True:

        print("\n==================================================")
        print("          INVENTORY MANAGEMENT SYSTEM")
        print("==================================================")

        print("1. View Products")
        print("2. Add Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Alert")
        print("7. Purchase Product")
        print("8. Sale Product")
        print("9. View Transaction History")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product() 

        elif choice == "6":
            low_stock_products()

        elif choice == "7":
            purchase_product()

        elif choice == "8":
            sale_product()

        elif choice == "9":
            view_transactions()
            
        elif choice == "10":
            print("\nThank you for using the Inventory Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 10.")

main_menu()