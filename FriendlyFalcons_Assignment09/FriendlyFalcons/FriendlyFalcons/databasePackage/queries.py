# File Name: queries.py
# Student Name: David Becker, Ian McDaniel, Derick Bellofatto
# Email: beckerd8@mail.uc.edu, mcdaniip@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Access SQL Server data from the GroceryStoreSimulator DB and print a formatted result using modularized Python code.
# Brief Description of what this module does: Contains all SQL SELECT query functions.
# Anything else that's relevant: 

from unittest import result
from databasePackage.connector import *

# Step 1: Get products
def get_all_products():
    db = DBConnection()
    db.cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
    return db.cursor.fetchall()

# Step 3: Get manufacturer name
def get_manufacturer_name(manufacturer_id):
    db = DBConnection()
    db.cursor.execute(f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}")
    result = db.cursor.fetchone()
    return result[0] if result else "Unknown"

# Step 5: Get brand name
def get_brand_name(brand_id):
    db = DBConnection()
    db.cursor.execute(f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}")
    result = db.cursor.fetchone()
    return result[0] if result else "Unknown"

# Step 6: Get number of items sold
def product_sales(product_id):
    db = DBConnection()
    db.cursor.execute(f"SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})")
    result = db.cursor.fetchone()
    return result[0] if result else "Unknown"
