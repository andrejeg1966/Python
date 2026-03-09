"""
Created on 17.12.2025

@author: GoranAndrejevic
"""

import mysql.connector

# establishing the connection
connection = mysql.connector.connect(
    host="localhost", user="root", password="Velesnica1966?", database="testdb"
)
old_table_name = "buyers"
new_table_name = "customer"
# Creating a cursor object
cursorObj = connection.cursor()
cursorObj.execute(f"RENAME TABLE {old_table_name} TO {new_table_name}")
print(f"Table '{old_table_name}' is renamed to '{new_table_name}' successfully.")
cursorObj.close()
connection.close()
