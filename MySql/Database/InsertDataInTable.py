'''
Created on 22.12.2025

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
column_to_add = 'tutorial_price'
new_tutorial_data = [
    (2, 'Learn MySQL', 'Abdul S', '2023-03-28'),
    (3, 'JAVA Tutorial', 'Sanjay', '2007-05-06'),
    (4, 'Python Tutorial', 'Sasha Lee', '2016-09-04'),
    (5, 'Hadoop Tutorial', 'Chris Welsh', '2023-03-28'),
    (6, 'R Tutorial', 'Vaishnav', '2011-11-04')
]
#Creating a cursor object 
cursorObj = connection.cursor()
cursorObj.execute("truncate table tutorials_tbl")
sql = "INSERT INTO tutorials_tbl VALUES (1, 'Learn PHP', 'John Paul', '2023-3-28')"
cursorObj.execute(sql)
insert_query = f'INSERT INTO {table_name} (tutorial_id, tutorial_title, tutorial_author, submission_date) VALUES (%s, %s, %s, %s)'
cursorObj.executemany(insert_query, new_tutorial_data)
connection.commit()
print("Row inserted successfully.")
describe_table_query = f"DESCRIBE {table_name}"
cursorObj.execute(describe_table_query)
columns_info = cursorObj.fetchall()
print(f"Description of table '{table_name}':")
for column in columns_info:
    print(f"Column Name: {column[0]}, Type: {column[1]}, Null: {column[2]}, Key: {column[3]}, Default: {column[4]}, Extra: {column[5]}")
add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {column_to_add} INT"
cursorObj.execute(add_column_query)
print(f"Column '{column_to_add}' is added to table '{table_name}' successfully.")
cursorObj.close()
connection.close()

