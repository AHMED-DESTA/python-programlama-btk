#1 
class ogrenci:
    def __init__(self,ad,soyad,ders_notu):
        self.ad=ad
        self.soyad=soyad
        self.ders_notu=ders_notu

    def durum_sorgulama(self):
        return "basarili." if self.ders_notu>=50 else "basarisiz."
        
o1=ogrenci("Ali","Veli",70)
o2=ogrenci("Ayse","Fatma",40)
print(o1.__dict__)     
print(o1.durum_sorgulama())

print(o2.__dict__)
print(o2.durum_sorgulama()) 
