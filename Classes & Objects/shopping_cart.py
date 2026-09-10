class cart:
    
    def __init__(self):
        
        self.items = {}
        self.price_details = {"book": 50, "laptop" : 30000}
    
    def add_items(self, item_name, quantity):
        
        self.items[item_name] = quantity
    
    def remove_items(self, item_name):
        
        del self.items[item_name]
    
    def update_quantity(self, item_name, updated_quantity):
        
        self.items[item_name] = updated_quantity
    
    def get_cart_items(self):
        
        cart_items = []
        
        for item_name in self.items.keys():
            
            cart_items.append(item_name)
            
        return cart_items
    
    def get_total_price(self):
        
        total_price = 0 
        
        for item, quantity in self.items.items():
            
            total_price += quantity * self.price_details[item]
            
        return total_price

            
cart_obj = cart()

cart_obj.add_items("books", 5)

cart_obj.add_items("laptop", 1)

print(cart_obj.items)

cart_obj.remove_items("laptop")

print(cart_obj.items)

cart_obj.update_quantity("books", 10)

print(cart_obj.items)

print(cart_obj.get_cart_items())

print(cart_obj.get_total_price())
        