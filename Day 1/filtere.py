sayilar=[-3,5,8,-1,-4]
# negatifler=[]

# for i in sayilar:
#     if i<0:
#         negatifler.append(i)
# print(negatifler)   

# def negatif(i):
#     return i<0 

# negatifler=list(filter(negatif,sayilar))
# print(negatifler)

# negatifler=list(filter(lambda i: i<0, sayilar)) #2.yol: negatif fonksiyonu yerine lambda fonksiyonu kullanarak negatif sayilari filtreleyebiliriz

# print(negatifler)   


# A_ileBaslayanlar=list(filter(lambda a: a.startswith("A"),["Ali","Ayse","Ahmet","Mehmet"]))  # A ile baslayan isimleri filtreler

# isimler=["ebru","Ayse","ceren","ali"]
# secilenler=list(filter(lambda x: x[0]=='a',isimler))  # A ile baslayan isimleri filtreler


# print(isimler) 
# print(secilenler)

users = [
{"username": "ebru_aydogan", "posts": ["Python 101", "İleri Seviye Python", "Data Science"]},
{"username": "btk_akademi", "posts": ["Duyuru", "Yeni Kurs"]},
{"username": "yazilim_ogrencisi", "posts": ["Merhaba Dünya"]},
{"username": "python_coder", "posts": []}
]
# pasifKullanicilar=[]
# for user in users: 
#     if len(user["posts"])<2: 

#         pasifKullanicilar.append(user)
print(pasifKullanicilar)    

filtered=filter(lambda user: len(user["posts"])<2, users)  # posts sayisi 2 den az olan kullanicilari filtreler
pasifler=list()
pasifKullanicilar=list(filtered)

