import json 

#person_dict={"name":"ali","languages": ["C#","python"]}  


person_dict={
  "name": "ebru aydogan",
  "languages": ["C#","python"],
   "isFullTime":True 
}
with open("person.json","w",encoding="utf-8") as f:
    json.dump(person_dict, f,indent=4,ensure_ascii=False)

    print("veriler person.json dosyasina basariyle kaydedildi.")
                                        