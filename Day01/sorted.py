# liste=[25,10,5,80,33]
# print(liste)
 # print(sorted(liste, reverse=True))
# stok={"elma":50,"cilek":100,"muz":20}
# sirali=sorted(stok) 
# print(sirali)  # alfabetik siraya gore siralar



#ddiict={key: value}  # sozluk olusturmak icin kullanilir
# urunler=[
#   {"adi":"laptop", "fiyat":1000},
#   {"adi":"telefon", "fiyat":900},
#   {"adi":"tablet", "fiyat":700}
# ]
# sirali_urunler=sorted(urunler,key=lambda x: x ["fiyat"])  # urunleri fiyata gore siralar
# print(sirali_urunler)   

isimlller=["Ali","Ayse","Ahmet","Zeynep"]
sirali_isimler=sorted(isimlller,key=lambda x: len(x))  # uzunluga gore siralar
print(sirali_isimler) 