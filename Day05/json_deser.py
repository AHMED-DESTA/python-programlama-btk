import json 

with open('products.json', 'r', encoding='utf-8') as file: 
    data=json.load(file)

    #print(data)

    print(data[0]["product_name"])
    print(data[0]["price"])
    print(data[0]["catagory"])

    
