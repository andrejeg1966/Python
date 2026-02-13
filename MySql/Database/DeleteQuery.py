'''
Created on 24.12.2025

@author: GoranAndrejevic
'''
import mysql.connector
import datetime
#establishing the connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Velesnica1966?',
    database='MySqlPythonDB'
)
#Creating a cursor object 
cursorObj = connection.cursor()
delete_query = "DELETE FROM tutorials_tbl WHERE tutorial_id = 6"
cursorObj.execute(delete_query)
connection.commit()
print("Row deleted successfully.")
cursorObj.close()
connection.close()