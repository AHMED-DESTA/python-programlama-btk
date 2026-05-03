import sqlite3
connection = sqlite3.connect('btk_akademi.db')
cursor=connection.cursor()

sql="SELECT * FROM urunler WHERE urun_adi LIKE ?"

search_target="I%"

cursor.execute(sql,(search_target,))
results=cursor.fetchall()

print(results)