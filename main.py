msg = '''Please select your choice (After anything you did , please save the file):
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
    if product_dict.get(name) < amount:
        return f"you can't sell this product. you don't have {amount} of {name}, you only have {product_dict[name]} of it"       

    product_dict[name] -= amount

    if product_dict[name] == 0:
        del product_dict[name]
        return f"sold successfuly. Now {name} is out of stock"    
    else:
        return f"sold successfuly. Remaining: {product_dict[name]}"        

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
    
def report_products():
    if product_dict:
        product_count =[]
        count_all = 0
        max_product = max(product_dict.values())
        max_product_names = [
        name
        for name, qty in product_dict.items()
        if qty == max_product
        ]
        min_product = min(product_dict.values())
        min_product_names = [
        name
        for name, qty in product_dict.items()
        if qty == min_product
        ]
        for name,qty in product_dict.items():
            product_count.append(f"{name} : {qty}")
            count_all += qty
        report = f'''
count of all the products you have in your store : {count_all}
the max amount of product is {max_product} which is for {" and ".join(max_product_names)}
the min amount of product is {min_product} which is for {" and ".join(min_product_names)}
        '''
        return product_count , report
    

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
        print ("Here is your report : ")
        product_count , report = report_products ()
        for pro in product_count:
            print (pro)
        print (report)

    elif choice == '7': #exit the program 
        break
    else :
        print("Please enter a valid number")
