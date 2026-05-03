import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

sql="SELECT * FROM urunler"

cursor.execute(sql)

# urun=cursor.fetchone()
# print(urun)

urunler=cursor.fetchall()
for u in urunler:
    print(f"ID: {u[0]}, Ürün Adı: {u[1]}, Stok Adedi: {u[3]}")

toplam=0
for urun in urunler:
    toplam += urun[3]
print(toplam)


db.close() 





















# import sqlite3

# db = sqlite3.connect("btk_akademi.db")
# cursor = db.cursor()


# liste = [
#     ("Klavye", 300000.0, 50),
#     ("Monitör", 3500.0, 15),
#     ("USB Kablo", 120.0, 200),
#     ("Mouse", 450.0, 80),
#     ("Kulaklık", 1200.0, 30),
#     ("Webcam", 50000.0, 25),
#     ("Hard Disk 1TB", 100225.0, 40),
# ]

# sql = "INSERT INTO urunler (urun_adi, fiyat, stok_adedi) VALUES (?, ?, ?)"


# cursor.executemany(sql, liste)

# db.commit()
# print(f"{len(liste)} kayıt başarıyla sisteme işlendi.")
# db.close()