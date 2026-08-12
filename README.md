# StockEase

**StockEase** is a Python and Microsoft SQL Server-based Inventory Management System designed to simplify and organize inventory operations.

The system provides a command-line interface for managing products, stock levels, suppliers, customers, purchases, sales, and transaction history. It also includes low-stock monitoring to help identify products that require restocking.

---

## Features

### Product Management
- View all available products
- Add new products
- Search products by name
- Update product information
- Delete products
- Track product price and stock quantity

### Stock Management
- Monitor current stock levels
- Define reorder levels for products
- Identify products requiring restocking
- Automatically increase stock when products are purchased
- Automatically decrease stock when products are sold

### Supplier Management
- Store supplier information
- Select suppliers when recording purchases
- Maintain supplier-product relationships

### Customer Management
- Store customer information
- Select customers when recording sales
- Maintain customer transaction records

### Purchase Management
- Search products by name
- Select suppliers from available suppliers
- Enter purchase quantity
- Calculate total purchase amount
- Automatically update product stock
- Record purchase transactions

### Sales Management
- Search products by name
- Select customers from available customers
- Validate available stock before a sale
- Calculate total sale amount
- Automatically update product stock
- Record sales transactions

### Transaction History
- View previous purchase and sales transactions
- Display product names
- Display customer names
- Display supplier names
- Display transaction type
- Display quantity
- Display total amount
- Display transaction date

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Application logic and command-line interface |
| Microsoft SQL Server | Database management |
| T-SQL | Database creation, queries, and data management |
| pyodbc | Python-to-SQL Server database connectivity |
| Visual Studio Code | Development environment |
| SQL Server Management Studio | Database development and management |
| Git & GitHub | Version control and project hosting |

---

## System Architecture

StockEase follows a simple application-database architecture:

```text
User
  │
  ▼
Python Application
(main.py)
  │
  ▼
Database Connection
(database.py)
  │
  ▼
Microsoft SQL Server
(InventoryDB)
  │
  ├── Categories
  ├── Suppliers
  ├── Products
  ├── Customers
  └── Transactions
