# x=5

# print(type(x))  
# print(type(int))
# print(type(str))

class person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sinifi olusturuldu.")

    def intro(self):
         print(f"merhaba benim adim {self.name}")