
liste = ["Ahmet", " ", "Meryem", None, "Ali", "  ", "Selin"]
# secilenler=list(filter(lambda x: x==' ',ham_veriler))  # bosluk iceren verileri filtreler    
# print(secilenler)   
# liste = ["Ahmet", " ", "Meryem", None, "Ali", "  ", "Selin"]

result = list(filter(lambda x: x and x.strip(), liste))

print(result)