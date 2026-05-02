#1 (1-@ araligindaki her sayinin karesini veren generator fonksiyonu)

# def sayi_uret(max):
#    sayi=0
#    while True:
#       yield sayi**2
#       sayi+=1
# print(sayi_uret(max))

# generator =sayi_uret(max)
# for i in generator :
#     print(i)

#2 fibonacci serisini hem normal hem de genetator fonksiyonu ile yazınız.

def fib_list(max):
    liste=[]
    count=0
    sayi1,sayi2=0,1
    while len(liste)<=max: 
       liste.append(sayi2)
       sayi1,sayi2=sayi2,sayi1+sayi2
    # print(liste)   
    count+=1
    return liste


print(fib_list(5))