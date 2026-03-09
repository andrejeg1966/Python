"""
Created on 17.12.2025

@author: GoranAndrejevic
"""

import mysql.connector

# establishing the connection
conn = mysql.connector.connect(
    user="root", password="Velesnica1966?", host="localhost", database="MySqlPythonDB"
)
# Creating a cursor object
cursor = conn.cursor()
# Creating a table
sql = """CREATE TABLE tutorials_tbl(
   tutorial_id INT NOT NULL AUTO_INCREMENT,
   tutorial_title VARCHAR(100) NOT NULL,
   tutorial_author VARCHAR(40) NOT NULL,
   submission_date DATE,
   PRIMARY KEY ( tutorial_id )
)"""
cursor.execute(sql)
print("The table tutorials_tbl is created successfully!")
# Closing the connection
conn.close()
