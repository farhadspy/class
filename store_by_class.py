class PRODUCT:
    def __init__(self , i , n , p , c):
        self.id = i
        self.name = n
        self.price = p
        self.count = c
    
    @staticmethod
    def sort():
        PRODUCTS.sort(key= lambda x: int(x.id))
    
    @staticmethod
    def add():
        while True:
            code = int(input("enter code: "))
            name = input("enter name: ")
            for product in PRODUCTS:
                if int(product.id) == code:
                    print("the code is exist.")
                    break
                elif product.name == name:
                    print("the name is exist.")
                    break
            else:
                price = input("enter price: ")  
                count = int(input("enter count: "))
                break 
            
        new_product = PRODUCT(code , name , price , count)
        PRODUCTS.append(new_product)
    
    def edit(self ,name ,price ,count):
        self.name = name
        self.price = price
        self.count = count  
        print("Product edited successfully.")
   
    @staticmethod       
    def search():
        user_input = input("type your name: ")  
        for product in PRODUCTS:
            if product.name == user_input:
                print(product.id,"\t\t" , product.name,"\t\t" , product.price,"\t\t" ,product.count,"\t\t" )
                return product
        else:
            print("not found")
            
    def remove(self):
        PRODUCTS.remove(self)
                          
    @staticmethod    
    def show_list():
        PRODUCT.sort()
        print("code\t\t name\t\t\t price\t\t\tcount") 
        for product in PRODUCTS:
            print(product.id, "\t\t" , product.name, "\t\t\t" , product.price , "\t\t\t" , product.count)
        
    def buy(self ,Total_price ,finish):
        while finish == 0:
            number_of_buy = int(input("how much do you want: "))
            if int(self.count) >= number_of_buy:
                self.count = int(self.count) - number_of_buy
                Total_price = (int(self.price) * number_of_buy) + Total_price   
            else:
                print("Limited stock. Stock is ", self.count ," pieces.")
            
            print("Total_price: " ,Total_price)
            while True:
                finish_buy = input("do you want continue (yes or no): ")
                if finish_buy == "no":
                    finish = 1
                    return finish
                elif finish_buy == "yes":
                    break
                else:
                    print("enter (yes or no): ") 
       
       
       
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
            
        f.close()

    def write(self):
        try:
            with open("class/database.txt", "w") as file:
                for product in PRODUCTS:
                    file.write(f"{product.id},{product.name},{product.price},{product.count}\n")
        except FileNotFoundError:
            print("Error: Could not write to 'class/database.txt'. Check if the directory exists.")
        except Exception as e:
            print(f"Error while writing to file: {e}")


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
flag = 0
Total_price = 0
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
        for p in PRODUCTS:
            if int(p.id) == id:
                name = input("pls enter name: ")
                price = input("pls enter price: ")
                count = int(input("pls enter count: "))
                p.edit(name , price , count)
                break
    elif choice == 3:
        id = int(input("enter product id: "))
        for p in PRODUCTS:
            if int(p.id) == id:
                p.remove()
    elif choice == 4:
        PRODUCT.search()
    elif choice == 5:
        PRODUCT.show_list()
    elif choice == 6:
        finish = 0
        while finish == 0:
            name = input("enter product name: ")
            for p in PRODUCTS:
                if p.name == name:
                    finish = p.buy(Total_price ,finish)
                    break
    elif choice == 7:
        PRODUCT.sort()
        db.write()
        exit(0)
    else:
        print("wrong number.pls enter corect number.")