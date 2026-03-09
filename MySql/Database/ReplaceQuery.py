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
replace_query = "REPLACE INTO tutorials_tbl (tutorial_id, tutorial_title, tutorial_author, submission_date) VALUES (3, 'Learning Java', 'John Doe', '2023-07-28')"
cursorObj.execute(replace_query)
connection.commit()
print("REPLACE query executed successfully.")
cursorObj.close()
connection.close()
