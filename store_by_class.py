class PRODUCT:
    def __init__(self , i , n , p , c):
        self.id = i
        self.name = n
        self.price = p
        self.count = c
    
    @staticmethod
    def sort():
        PRODUCTS.sort(key= lambda x: int(x["code"]))
    
    @staticmethod
    def add():
        while True:
            code = int(input("enter code: "))
            name = input("enter name: ")
            for product in PRODUCTS:
                if int(product["code"]) == code:
                    print("the code is exist.")
                    break
                elif product["name"] == name:
                    print("the name is exist.")
                    break
            else:
                price = input("enter price: ")  
                count = int(input("enter count: "))
                break 
            
        new_product = PRODUCT(code , name , price , count)
        PRODUCTS.append(new_product)
    
    def edit(self):
        '''''
        while True:
            edit_list = PRODUCT.search()
            if edit_list != None:
                edit_list["name"] = input("pls enter name: ")
                edit_list["price"] = input("pls enter price: ")
                edit_list["count"] = input("pls enter count: ")
                break 
    for product in PRODUCT:
        if product["code"] == edit_list["code"] or product["name"] == edit_list["name"]:
            product.update({"name":edit_list["name"] , "price":edit_list["price"] , "count":edit_list["count"]})
    '''''
    
    @staticmethod       
    def search():
        '''''
        user_input = input("type your keyword: ")  
        for product in PRODUCTS:
            if product["code"] == user_input or product["name"] == user_input:
                print(product["code"],"\t\t" , product["name"],"\t\t" , product["price"],"\t\t" ,product["count"],"\t\t" )
                token = 1
                return product
        else:
            print("not found")
            token = -1
        '''''
    
    def remove(self):
        '''''
        while True:
            remove_from_list = PRODUCT.search() 
            if remove_from_list != None:
                for product in PRODUCTS:
                    if product["code"] == remove_from_list["code"] or product["name"] == remove_from_list["name"]:
                        PRODUCTS.remove(product)
                        break
                break
        '''''
    
    @staticmethod    
    def show_list():
        PRODUCT.sort()
        print("code\t\tname\t\t\tprice\t\tcount") 
        for product in PRODUCTS:
            print(product["code"], "\t\t" , product["name"], "\t\t\t" , product["price"])
        
    def buy(self):
        '''''
        buy_items = search()
        number_of_buy = int(input("how much do you want: "))
        
        for product in PRODUCTS:
            if product["name"] == buy_items["name"]:
                if int(product["count"]) >= number_of_buy:
                    product["count"] = str(int(product["count"]) - number_of_buy)
                else:
                    print("Limited stock. Stock is ", product["count"] ," pieces.")
        finish_buy = input("if your buying is finish enter yes else enter no: ")
        if finish_buy == "yes":
            break
        else:
            continue
        '''''
        
class Database:
    def __init__(self):
        ...
        
    def read(self):
        f = open("class/database.txt","r")
        
        for line in f:
            line = line.strip()  # حذف فاصله‌ها و اینترها
            if not line:  # نادیده گرفتن خطوط خالی
                continue
            result = line.split(",")
            
            my_obj = PRODUCT(result[0],result[1],result[2],result[3])
            
            PRODUCTS.append(my_obj)
            
            f.close

    def write(self):
        file = open("store/database.txt", "w")
        for product in PRODUCTS:
            if all(key in product for key in ["code", "name", "price", "count"]):
                file.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")

class Store:
    def __init__(self):
        ...
    
    @staticmethod
    def show_menu():
        print("1- Add")
        print("2- Edit")
        print("3- Remove")
        print("4- Search")
        print("5- Show List")
        print("6- Buy")
        print("7- Exit")                
 
 
 
PRODUCTS = []
db = Database()    
print("Welcome to farhad store")
print("Loading...")
db.read()
print("Data Loading.")

while True:
    
    Store.show_menu()
    choice = int(input("enter number: "))
    
    if choice == 1 :
        PRODUCT.add()
    elif choice == 2:
        id = int(input("enter product id: "))
        if p.id == id:
            p.edit()
    elif choice == 3:
        id = int(input("enter product id: "))
        for p in PRODUCTS:
            p.remove()
    elif choice == 4:
        PRODUCT.search()
    elif choice == 5:
        PRODUCT.show_list()
    elif choice == 6:
        while True:
            name = int(input("enter product name: "))
            if p.name == name:
                p.buy()
            while True:
                end_buy = input("do you want to end buying(yes or no)? ")
                if end_buy == "yes":
                    flag == 1
                    break
                elif end_buy == "no":
                    continue
                else:
                    print("pls write the (yes or no)")
                    flag = 0
            if flag == 1:
                break
    elif choice == 7:
        PRODUCT.sort()
        db.write()
        exit(0)
    else:
        print("wrong number.pls enter corect number.")