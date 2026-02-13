'''
Created on 24.12.2025

@author: GoranAndrejevic
'''
import mysql.connector
#establishing the connection
connection = mysql.connector.connect(
   host='localhost',
   user='root',
   password='Velesnica1966?',
   database='MySqlPythonDB'
)
cursorObj = connection.cursor()
create_view_query = """
CREATE VIEW tutorial_view AS
SELECT tutorial_id, tutorial_title, tutorial_author, submission_date
FROM tutorials_tbl
WHERE submission_date >= '2023-01-01'
"""
cursorObj.execute(create_view_query)
connection.commit()
print("View created successfully.")
cursorObj.close()
connection.close()