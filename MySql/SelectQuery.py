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
table_name = 'tutorials_tbl'
#Creating a cursor object 
cursorObj = connection.cursor()
select_query = f"SELECT tutorial_id, tutorial_title, tutorial_author, submission_date FROM {table_name}"
cursorObj.execute(select_query)
result = cursorObj.fetchall()
print("Tutorial Table Data:")
for row in result:
    print(row)
cursorObj.close()
connection.close()