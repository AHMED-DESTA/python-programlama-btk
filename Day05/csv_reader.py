import csv 

# with open('urunler.csv', 'r', encoding='utf-8') as file:
#     reader=csv.reader(file)

#    # next(reader)

#     # print(reader) 
#     for satir in reader:
#     #   print(satir)
#      print(f"urun adi:{satir[1]}- urun fiyat: {satir[1]}")


with open('urunler.csv', encoding='utf-8') as file:
   reader=csv.DictReader(file)

   for satir in reader: 
       print(f"urun: {satir['urun_adi']}- fiyat: {satir['fiyat']}")
      
