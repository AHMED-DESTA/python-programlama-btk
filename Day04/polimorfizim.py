hayvanlar= ["kedi","kopek","kus"]

# for h in hayvanlar:
#     if isinstance(h,kedi):
#         print("miyav")
#     elif isinstance(h,kopek):
#         print("hav")
#     elif isinstance(h,kus):
#         print("cik cik")

# class animals:
#     def speak(self):
#         print("hayvanlar ses çıkarır.")

# class Dog(animals):
#     def speak (self):
#         print("kopek havlıyor.")

# class cat(animals):
#     def speak(self):
#         print("kedi milavliyor.")

# d1=Dog()
# d1.speak()
# c1=cat()
# c1.speak()          
        

class sekil():
    def __init__(self, kenar1):
     self.kenar1=kenar1
     def alan_hesapla(self):
         return self.kenar1 * self.kenar1
     
class kare(sekil):
    pass
def alan_hesapla(self):
         return self.kenar1 * self.kenar1
     


class daire(sekil):
    def alan_hesapla(self):
        return 3.14 * self.kenar1 * (self.kenar1**2)
    

class dikdortgen(sekil):
    def __init__(self, kenar1, kenar2):
        super().__init__(kenar1)
        self.kenar2=kenar2
        
    def alan_hesapla(self):
        return self.kenar1 * self.kenar2     
    

k1=kare(5)
print(k1.alan_hesapla()) 
dk=dikdortgen(5,10)
print(dk.alan_hesapla())   
