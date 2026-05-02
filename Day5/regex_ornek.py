import re 
# text="Iletisim: 0505-123-4567 destek@btk.gov.tr veya 0505 987 1212"
  
# phone_pattern=r"\d{4}[-\s]?\d{3}[-\s]\d{4}[-\s]" 
# email_pattern=r"\w+@\w+.\w+.\w+"

# p_match=re.findall(phone_pattern,text)
  
# e_match=re.findall(email_pattern,text)
# print(e_match)
# print(p_match)


#2

data="fiyat: $1.200.00 | indirim: %20" 
pattern=r"^0-9.,]^" 

clean_data=re.sub(pattern,"",data)

print(clean_data)    