import csv 

with open('urunler.csv','w',encoding='utf-8',newline='') as file: 
    writer = csv.writer(file)

    writer.writerow(['urun_adi', 'fiyat'])

    writer.writerow(['Laptop','25000'])

    urunler =[['mouse','500'],['klavye','1200'],['monitor','4000']]

    writer.writerows(urunler)

    print("doaya basariyle olusturuldu")
      

fieldNames=["urun","fiyat"]
urunler=[
    {'urun':'Laptop','fiyat':'25000'},
        {'urun':'mouse','fiyat':'4500'},
    {'urun':'klavye','fiyat':'7800'},
        {'urun':'monitor','fiyat':'15000'}
]
writer.writerows(urunler)
writer.writerow({'urun_adi': 'monitor', 'fiyat':'4000'})



print("DictWriter ile doaya basariyle olusturuldu")





