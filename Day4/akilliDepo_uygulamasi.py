# Ana sinif
class Urun:
    def __init__(self, ad, fiyat, agirlik, stok):
        self.ad = ad
        self.fiyat = fiyat
        self.agirlik = agirlik
        self.stok = stok

    def kargo_hesapla(self):
        return self.agirlik * 10

    def __str__(self):
        return f"{self.ad} - Fiyat: {self.fiyat}, Stok: {self.stok}"


# Elektronik urun
class ElektronikUrun(Urun):
    def kargo_hesapla(self):
        return self.agirlik * 12


# Gida urunu
class GidaUrunu(Urun):
    def kargo_hesapla(self):
        return self.agirlik * 8


# Tehlikeli urun
class TehlikeliUrun(Urun):
    def kargo_hesapla(self):
        return self.agirlik * 20


# Depo yonetimi
class DepoYonetici:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        self.urunler.append(urun)


# Lojistik islemleri
class Lojistik:
    def dusuk_stok(self, urunler):
        for urun in urunler:
            if urun.stok < 5:
                yield urun


# PROGRAM

depo = DepoYonetici()

u1 = ElektronikUrun("Laptop", 1000, 2, 3)
u2 = GidaUrunu("Elma", 5, 1, 10)
u3 = TehlikeliUrun("Gaz", 50, 3, 2)

depo.urun_ekle(u1)
depo.urun_ekle(u2)
depo.urun_ekle(u3)

# Listeleme
for urun in depo.urunler:
    print(urun)

# Kargo
print("Kargo:", u1.kargo_hesapla())

# Dusuk stok
lojistik = Lojistik()
for urun in lojistik.dusuk_stok(depo.urunler):
    print("Dusuk stok:", urun.ad)