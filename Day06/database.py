import sqlite3 

connection = sqlite3.connect('btk_akademi.db')
cursor=connection.cursor()

print("Database created successfully")
connection.close() 
