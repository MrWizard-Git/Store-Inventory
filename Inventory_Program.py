import json 

File_name = 'Project3\\Data.json'

try:
    with open(File_name, "r") as f:
        data = json.load(f)
except:
    data = []

def save_inventory():
    with open(File_name, "w") as f:
                json.dump(data, f , indent=4)


def Add_Product():
    Product = input("Product Name: ")
    Price = float(input("Product Price: ₹ "))
    Quantity = int(input("Product Quantity: "))

    newdata = {
        "Product" : Product,
        "Price" : Price,
        "Quantity" : Quantity,
        "Total" : Price * Quantity
    }

    data.append(newdata)

    with open(File_name, "w") as f:
        json.dump(data, f , indent=4)

def view_Product(data):
    for i in data:
        print(f"{i["Quantity"]} pics {i["Product"]} | Total= ₹{i["Total"]}\n")

def Modify_Quantity(data):
    Modify_Product = input("[+] Enter Product Name which you want to modify: ")
    for item in data:
        if item["Product"].lower() == Modify_Product.lower():
            print(f"There are {item["Quantity"]} pics {item["Product"]}")
            New_Quantity = int(input("[+] Enter Quantity: "))
            item["Quantity"] = New_Quantity
            item["Total"] = New_Quantity * item["Price"]
            save_inventory()
            print("\nDone 👍\n")
            break

def Delete_Product(data):
    Modify_Product = input("[+] Enter Product Name which you want to Delete: ")
    for item in data:

        if item["Product"].lower() == Modify_Product.lower():
            print(f"You want to delete {item["Product"]}")
            data.remove(item)
            save_inventory()
            print("Product Deleted.")
            break


while True:
    print("To Add Product: Enter 1️⃣ ")
    print("To View Products: Enter 2️⃣ ")
    print("To Modify Product's Quantity: Enter 3️⃣ ")
    print("To Delete Product: Enter 4️⃣ ")
    print("To Exit: Enter 5️⃣")

    choice = int(input("Enter Command>>> "))

    if choice == 1:
        Add_Product()

    if choice == 2:
        view_Product(data)

    if choice == 3:
        Modify_Quantity(data)

    if choice == 4:
        Delete_Product(data)

    elif choice == 5:
        break
  
