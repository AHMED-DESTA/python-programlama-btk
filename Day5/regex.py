import re 

text="btk akademi python kursu btk"

pattern="btk"

match= re.search(pattern,text)

# sonuc=match.span()
# sonuc=match.start()
# sonuc=match.end()

match=re.findall(pattern,text)

re.sub(pattern,"BTK",text)
sonuc=re.sub(pattern,"BTK",text)    
print(sonuc)