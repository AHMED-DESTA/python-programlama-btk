# liste=[True,True,True,True]
# sonuc=all(liste)
# print(sonuc )


notlar=[40,70,80,90]   
sonuc = True
# for n in notlar: 
#    if n<50: 
#     sonuc=False
print(sonuc)
print(n>=50 for n in notlar)  # tum notlarin 50 den buyuk olup olmadigini kontrol eder
sonuc=all([n>=50 for n in notlar])  # tum notlarin 50 den buyuk olup olmadigini kontrol eder
print(sonuc)    