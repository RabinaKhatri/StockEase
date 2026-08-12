/*
============================================================
        INVENTORY MANAGEMENT SYSTEM - DATABASE
============================================================

Database: InventoryDB

This script:
1. Creates the InventoryDB database
2. Creates five tables
3. Creates primary and foreign key relationships
4. Inserts sample data
5. Includes the final Transactions table structure

Tables:
- Categories
- Suppliers
- Products
- Customers
- Transactions
============================================================
*/


/* =========================================================
   1. CREATE DATABASE
   ========================================================= */

USE master;
GO

-- Create the database only if it does not already exist
IF DB_ID('InventoryDB') IS NULL
BEGIN
    CREATE DATABASE InventoryDB;
END;
GO


/* =========================================================
   2. USE INVENTORY DATABASE
   ========================================================= */

USE InventoryDB;
GO


/* =========================================================
   3. CREATE CATEGORIES TABLE
   =========================================================

   Stores different product categories.

   Example:
   Electronics
   Clothing
   Stationery
   Home Appliances
   Beauty Products
*/

CREATE TABLE Categories
(
    CategoryID INT IDENTITY(1,1) PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL
);
GO


/* =========================================================
   4. CREATE SUPPLIERS TABLE
   =========================================================

   Stores information about suppliers who provide products.
*/

CREATE TABLE Suppliers
(
    SupplierID INT IDENTITY(1,1) PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL,
    Contact VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(200)
);
GO


/* =========================================================
   5. CREATE PRODUCTS TABLE
   =========================================================

   Stores all products available in the inventory.

   CategoryID connects each product to a category.
   SupplierID connects each product to its supplier.
   Price stores the price per unit.
   StockQuantity stores the current available stock.
   ReorderLevel determines when a low-stock alert appears.
*/

CREATE TABLE Products
(
    ProductID INT IDENTITY(1,1) PRIMARY KEY,

    ProductName VARCHAR(100) NOT NULL,

    CategoryID INT NOT NULL,

    SupplierID INT NOT NULL,

    Price DECIMAL(10,2) NOT NULL,

    StockQuantity INT NOT NULL DEFAULT 0,

    ReorderLevel INT NOT NULL DEFAULT 5,

    -- Connect product to Categories table
    FOREIGN KEY (CategoryID)
        REFERENCES Categories(CategoryID),

    -- Connect product to Suppliers table
    FOREIGN KEY (SupplierID)
        REFERENCES Suppliers(SupplierID)
);
GO


/* =========================================================
   6. CREATE CUSTOMERS TABLE
   =========================================================

   Stores information about customers who purchase products.
*/

CREATE TABLE Customers
(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,

    CustomerName VARCHAR(100) NOT NULL,

    Contact VARCHAR(20),

    Email VARCHAR(100),

    Address VARCHAR(200)
);
GO


/* =========================================================
   7. CREATE TRANSACTIONS TABLE
   =========================================================

   Stores all purchase and sale transactions.

   TransactionType:
   - Purchase = stock is added
   - Sale     = stock is reduced

   CustomerID is NULL for purchases.

   SupplierID is NULL for sales.

   TotalAmount stores:
   Price × Quantity

   ProductName, CustomerName and SupplierName are also stored
   directly to make transaction history easier to display.
*/

CREATE TABLE Transactions
(
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,

    ProductID INT NOT NULL,

    CustomerID INT NULL,

    SupplierID INT NULL,

    TransactionType VARCHAR(20) NOT NULL,

    Quantity INT NOT NULL,

    TransactionDate DATETIME DEFAULT GETDATE(),

    TotalAmount DECIMAL(10,2) NULL,

    ProductName VARCHAR(100) NULL,

    CustomerName VARCHAR(100) NULL,

    SupplierName VARCHAR(100) NULL,

    -- Connect transaction to Products table
    FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    -- Connect sale transaction to Customers table
    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    -- Connect purchase transaction to Suppliers table
    FOREIGN KEY (SupplierID)
        REFERENCES Suppliers(SupplierID)
);
GO


/* =========================================================
   8. INSERT DATA INTO CATEGORIES
   =========================================================

   Adds the initial product categories.
*/

INSERT INTO Categories (CategoryName)
VALUES
    ('Electronics'),
    ('Clothing'),
    ('Stationery'),
    ('Home Appliances'),
    ('Beauty Products');
GO


/* =========================================================
   9. INSERT DATA INTO SUPPLIERS
   =========================================================

   Adds the initial suppliers.
*/

INSERT INTO Suppliers
(
    SupplierName,
    Contact,
    Email,
    Address
)
VALUES
    (
        'Tech World Suppliers',
        '9801234567',
        'techworld@gmail.com',
        'Kathmandu'
    ),
    (
        'Fashion Hub Nepal',
        '9812345678',
        'fashionhub@gmail.com',
        'Lalitpur'
    ),
    (
        'ABC Stationery',
        '9823456789',
        'abcstationery@gmail.com',
        'Biratnagar'
    ),
    (
        'Home Plus Suppliers',
        '9834567890',
        'homeplus@gmail.com',
        'Pokhara'
    ),
    (
        'Beauty Care Nepal',
        '9845678901',
        'beautycare@gmail.com',
        'Kathmandu'
    );
GO


/* =========================================================
   10. INSERT DATA INTO PRODUCTS
   =========================================================

   Adds the initial products and their stock information.
*/

INSERT INTO Products
(
    ProductName,
    CategoryID,
    SupplierID,
    Price,
    StockQuantity,
    ReorderLevel
)
VALUES
    ('Wireless Mouse', 1, 1, 1200.00, 25, 5),
    ('Keyboard', 1, 1, 1800.00, 15, 5),
    ('T-Shirt', 2, 2, 900.00, 30, 10),
    ('Notebook', 3, 3, 150.00, 50, 10),
    ('Electric Kettle', 4, 4, 2500.00, 8, 3),
    ('Face Wash', 5, 5, 450.00, 20, 5);
GO


/* =========================================================
   11. INSERT DATA INTO CUSTOMERS
   =========================================================

   Adds the initial customers.
*/

INSERT INTO Customers
(
    CustomerName,
    Contact,
    Email,
    Address
)
VALUES
    (
        'Ram Sharma',
        '9851234567',
        'ram@gmail.com',
        'Kathmandu'
    ),
    (
        'Sita Rai',
        '9862345678',
        'sita@gmail.com',
        'Lalitpur'
    ),
    (
        'Aayush Thapa',
        '9873456789',
        'aayush@gmail.com',
        'Bhaktapur'
    ),
    (
        'Priya Gurung',
        '9884567890',
        'priya@gmail.com',
        'Pokhara'
    );
GO


/* =========================================================
   12. VERIFY TABLE DATA
   =========================================================

   These queries allow us to check whether the sample
   data was inserted successfully.
*/

SELECT * FROM Categories;

SELECT * FROM Suppliers;

SELECT * FROM Products;

SELECT * FROM Customers;

SELECT * FROM Transactions;
GO


/* =========================================================
   END OF DATABASE SETUP SCRIPT
   ========================================================= */