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
# creating the database 
cursorObj.execute("CREATE DATABASE MySqlPythonDB")
print("Database Created Successfully")
# disconnecting from server
# Show databases 
cursorObj.execute("SHOW DATABASES")
# Fetch all the databases 
databases = cursorObj.fetchall()
# Printing the list of databases
print("The list of databases are: ")
for database in databases:
    print(database[0])
# Disconnecting from server
connection.close()