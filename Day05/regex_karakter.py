text="ABC 123 983 1A3 1_2"
import re

# pattern=r"\d\d\d"
# pattern=r"\d{3}"
pattern=r"\d+"

# match=re.search(pattern)
match=re.findall(pattern,text)
pattern=r"^A([a-zA-Z]{3})"

for i in match:
    print(i.group())



# sonuc=match

# print(ssonuc)