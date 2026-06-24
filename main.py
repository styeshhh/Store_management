msg = '''Please select your choice :
1)add / Edit
2)sell
3)search
4)show
5)save
6)report
7)exit
'''
from pathlib import Path
current_dir = Path(__file__).parent
file_path = current_dir / "product.txt"
product_dict = {}
def load_products():
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                name_part, qty_part = line.split(" - ")
                name = name_part.split(":")[1].strip()
                qty = int(qty_part.split(":")[1].strip())
                product_dict[name] = qty

    except FileNotFoundError:
        pass

def add_product(name , qty):
    if name in product_dict:
        product_dict [name] = qty + int(product_dict.get(name))
        return f"the quantity of the {name} has been changed and now is {product_dict[name]}"       
    else :
        product_dict[name] = qty
        return "Added successfully"

def sell_product(name , amount):
        if product_dict.get(name) >= amount:
            product_dict [name] = int(product_dict.get(name)) - amount
            return f"the product saled succefully , now you have {product_dict [name]} of it"
        else :
            return f"you can't sell this product .you don't have {amount} of {name} , you only have {product_dict [name]} of it"
    
def search_product(name):
    qty = product_dict.get(name)
    if name in product_dict :
        return f"you have {qty} of {name}"
    else :
        return f"the {name} doesn't exists in your store"
def show_products() : 
    if product_dict:
        products =[]
        for name,qty in product_dict.items():
            products.append(f"product : {name} - quantity : {qty}")
        return products  
def save_product():
    with open (file_path,"w") as file:
        for name ,qty in product_dict.items():
            file.write(f"product : {name} - quantity : {qty} \n")  
        return  "saved successfuly"

load_products()
while True:
    choice = input(msg)
    if choice =='1': #add product
        name = input ("enter the product's name : ")
        qty = input ("enter the product's quantity : ")
        print (add_product(name , int(qty)))

    elif choice == '2': #sell product
        if product_dict :
            name = input ("enter the product's name : ")
            if name in product_dict:
                qty = input ("Enter the quantity you want to sell : ")
                print (sell_product(name , int(qty)))
            else :
                print (f"there is no such product as {name} in your store which you can sell it")

        else :
            print("your store is empty , there is nothing to be sold")
    elif choice == '3': # search product
        if product_dict:
            name = input ("enter the product's name you want to search for: ")
            print (search_product(name))
        else :
            print ("your store is empty , there is nothing to be serached")
    elif choice == '4': #show all the products
        products = show_products()
        if products :
            for product in products:
                print(product)
        else  :
            print("your store is empty , please add sth first")        

    elif choice == '5': # save products to a file
        print(save_product())
    elif choice == '6': #report products
        pass
    elif choice == '7': #exit the program 
        break
