# soru 1 
# liste=[] 
# tam_bolenler=[i for i in range(1,101) if i % 12 == 0]
# print(tam_bolenler) 

# soru 2
# metin="BTK 2026 eigitim yili 5.donem" 
# for x in metin:
#     if x.isdigit():  # isdigit() metodu, bir karakterin rakam olup olmadığını kontrol eder. Eğer karakter bir rakamsa True döner, aksi takdirde False döner.
#         print(x)
# 2.soru 2.yol 
# metin="BTK 2026 eigitim yili 5.donem"
# rakamlar=[char for char in metin if char.isdigit()]

#         soru 3
# sicakliklar=[10,2,-3,5,0]
# for s in sicakliklar:
#             if s<4:
#                 print("buzlanma Tehlikesi") 
#             else: 
#                 print("Normal") 


# soru 4
# ogrenciler=["Ali", "Ayse"] 
# notlar =[40,70]           
# if ogrenciler[0]=="Ali" and notlar[0]<50:
#     print("Ali",notlar[0],"<50=","Ali kaldi")   # ///// bu cozum iyi olmayabilir.../////

    #4.soru 2.yol 
ogrenciler=["Ali", "Ayse"]
notlar =[40,70]
sonuclar=["gecti" if n>50 else "kaldi" for n in notlar] 
sozluk={ogrenciler:sonuclar for ogrenciler,sonuclar in zip(ogrenciler,sonuclar)} 
print(sozluk)


# #5.soru asagidaki kodu list comprehension kullanarak yaziniz
# list1=[1,2,3]
# list2=[10,20]  
# carpimlar=[] 
# for x in list1:
#     for y in list2: 
#         carpimlar.append(x*y)
#     carpimlar2=[x*y for x in list1 for y in list2]

# print(carpimlar)