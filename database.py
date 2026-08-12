import pyodbc


def get_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=InventoryDB;"
        "Trusted_Connection=yes;"
    )

    return connection