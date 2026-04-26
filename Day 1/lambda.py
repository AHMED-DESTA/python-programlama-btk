katlayici=  lambda n: lambda a: a*n   # fonksiyon fabrika ggibi calisir 

ikiKatiniAl= katlayici(2)  # iki katini alma fonksiyonu olusturduk
ucKatiniAl= katlayici(3)   # uc katini alma fonks 
sonuc=ucKatiniAl(5)  # 5 sayisinin uc katini alir
print(ikiKatiniAl(10))  # 10 sayisinin iki katini alir
print(sonuc)  # 5 sayisinin uc katini yazdirir  
