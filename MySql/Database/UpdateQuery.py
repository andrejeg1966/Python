"""
Created on 24.12.2025

@author: GoranAndrejevic
"""

import datetime

import mysql.connector

# establishing the connection
connection = mysql.connector.connect(
    host="localhost", user="root", password="Velesnica1966?", database="MySqlPythonDB"
)
# Creating a cursor object
cursorObj = connection.cursor()
update_query = (
    "UPDATE tutorials_tbl SET tutorial_title = 'Learning Java' WHERE tutorial_id = 3"
)
cursorObj.execute(update_query)
connection.commit()
print("Row updated successfully.")
cursorObj.close()
connection.close()
