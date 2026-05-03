import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

target_id=2
cursor.execute("DELETE FROM urunler WHERE id=?",(target_id,))
db.commit()
print("Data deleted successfully")
db.close()