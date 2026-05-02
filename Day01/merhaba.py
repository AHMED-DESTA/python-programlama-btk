# sayilar=[]

# for i in range(6):
#     sayilar.append(i**2)

# print(sayilar)

# liste=[i**2 for i in range(6)]
# print(liste)
isimler=["Ali","Veli","Ayşe","Fatma"]   
# for i in isimler:
#     isimler.append(i.upper())
# isimler.upper()
# print(isimler)       

# isimler2=[]
# for isim in isimler:
#     isimler2.append(isim.upper())
# print(isimler2)

# sehirler=["Ankara","eskisehir","Afyon","Kutahya"]
# a_olanlar=[sehir for sehir in sehirler if 'a'in sehir or "A" in sehir]

# print(a_olanlar)
notlar=[50,60,30,80,90]
# sonuc=[]

# for n in notlar:
#     if (n>=50):
#         sonuc.append("gecti")
#     else: 
#         sonuc.append("kaldi")
# print(sonuc)
sonuc= [ "gecti" if (n>=50) else "kaldi" for n in notlar] 
print(sonuc)