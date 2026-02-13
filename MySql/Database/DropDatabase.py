'''
Created on 17.12.2025

@author: GoranAndrejevic
'''
import mysql.connector
# creating the connection object
connection = mysql.connector.connect(
host ="localhost",
user ="root",
password ="Velesnica1966?"
)
# creating cursor object
cursorObj = connection.cursor()
# dropping the database 
cursorObj.execute("DROP DATABASE MySqlPythonDB")
print("Database dropped Successfully")
# disconnecting from server
connection.close()