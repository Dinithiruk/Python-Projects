inventory ={} # dictionary for empty inventory 

# add products by checking whether they already exists or not in the dictionary 
def add_stock(product_name,quantity):
    if product_name in inventory:
        inventory[product_name] += quantity
    else:
        inventory[product_name]=quantity


#Updating the inventory 
def update_stock(product_name,new_quantity):
    if product_name in inventory:
        inventory[product_name]=new_quantity
    else:
        print("Product couldn't found in the inventory")

# function to display inventory  
def display_inventory():
    print("\n Inventory : \n")
    for product_name , quantity in inventory.items():
        print(f"{product_name}:{quantity}")


# adding products to the ineventory 
add_stock("Staplers ", 350)
add_stock("Pencils-Atlas brand ",500)
add_stock("CR Book - Promate brand",2000)
add_stock("Instument box ",400)
add_stock("Glitter papers - 12 colors ",600)

#before updating the inventory 
display_inventory() 

#after updating the inventory 
update_stock("Staplers ", 1000)
display_inventory() 
