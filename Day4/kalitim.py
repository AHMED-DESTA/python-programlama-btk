class person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sinifi olusturuldu.")

def intro(self):
         print(f"merhaba benim adim {self.name}")
  
class student(person):
    def __init__(self, name, surname, age, number):
          super().__init__(name, surname, age)
          self.number=number
          print("student sinifi olusturuldu.")

    def study(self):
          print(f"{self.name} {self.surname} ders çalışıyor.")

    def intro(self):
          print(self.name, self.surname, self.age, self.number)


class teacher(person):
    def __init__(self, name, surname, age,branch):
          super().__init__(name, surname, age,branch)
          self.branch=branch
          print("teacher sinifi olusturuldu.")

    def teach(self): 
          print(f"{self.name}, {self.branch},ders anlatıyor.")

    def intro(self):
           print(self.name, self.surname, self.age, self.branch)  
    


p1=person("ebru,", "kurt", 30)
print(p1.name, p1.surname, p1.age)
s1=student("ayşe", "yılmaz", 20, 12345)
print(s1.name, s1.surname, s1.age,s1.number,)
t1=teacher("mehmet", "doğan", 40, "matematik")
print(t1.name, t1.surname, t1.age, t1.branch)


p1.intro()
s1.intro()
t1.intro()
t1.teach()