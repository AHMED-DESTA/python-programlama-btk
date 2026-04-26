# sayilar=[1,2,3,4,5]
# kareler=[] 

# for i in sayilar:
#     kareler.append(i**2)
  
# def kareHesapla(i): 
#     return i**2

# kareleri=list(map(kareHesapla,sayilar))   #2.yol: ->>: kareleri=list(map(lambda i: i**2, sayilar))
# print(kareleri) 
# text={"ebru","ayse","ali"}
# sonuc=list(map(lambda x: x.upper(),text)) # text icindeki her bir elemani buyuk harfe cevirir
# print(sonuc)    

liste=[1.3,2.5,3.7]
sonuc=list(map(int,liste))  # liste icindeki her bir elemani tam sayiya cevirir
print(sonuc)
