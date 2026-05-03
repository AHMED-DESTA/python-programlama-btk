import sqlite3 
connection = sqlite3.connect('btk_akademi.db')  
cursor=connection.cursor()  

cursor.execute("SELECT * FROM urunler ")

urunler=cursor.fetchall()

print("--- stok listesi---")

for urun in urunler:
    print(f"ID: {urun[0]}| Urun: {urun[1]} | Fiyat: {urun[2]}TL")
connection.close()
 

 