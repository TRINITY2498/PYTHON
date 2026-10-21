# Introduction to Inheritence.

class product:
    
    def __init__(self, name, price, deal_price, ratings):
        
        self.name = name 
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
        
    def display_product_details(self):
        
        print("Product : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal Price : {}".format(self.deal_price))
        print("Ratings : {}".format(self.ratings))
        print("You Saved : {}".format(self.you_save))
        
# p = product("Shoes", 1500, 700, 4.5)
# p.display_product_details()
        
        
class ElectronicItem(product):
    
    def set_warranty(self, warranty_in_months):
        
        self.warranty_in_months = warranty_in_months
    
    def get_warranty(self):
        
        return self.warranty_in_months

class GroceryItem(product):
    
    pass

e_item = ElectronicItem("Phone", 35000, 20000, 4.5)

e_item.set_warranty(12)

print(e_item.get_warranty())

# e_item.display_product_details()

g_item = GroceryItem("Milk", 50, 45, 2.5)

# g_item.display_product_details()