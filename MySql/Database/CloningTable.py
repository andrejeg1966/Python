"""
Created on 22.12.2025

@author: GoranAndrejevic
"""

import mysql.connector

# establishing the connection
connection = mysql.connector.connect(
    host="localhost", user="root", password="Velesnica1966?", database="testdb"
)
source_table_name = "customers"
new_table_name = "copyCustomer"
# Creating a cursor object
cursorObj = connection.cursor()
cursorObj.execute(f"CREATE TABLE {new_table_name} AS SELECT * FROM {source_table_name}")
print(f"Table '{source_table_name}' is cloned to '{new_table_name}' successfully.")
cursorObj.close()
connection.close()
