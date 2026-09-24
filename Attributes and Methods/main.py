class Cart:
    
    # Class Attributes.
    
    flat_discount = 0
    
    min_bill = 100
    
    def __init__(self):
        
        # Instance Attributes.
        
        self.items = {}  
    
    def add_items(self, item_name, quantity):
        
        self.items[item_name] = quantity
    
    def display_items(self):
        
        print(self.items)
    
    @classmethod
    def update_flat_discount(cls, new_flat_discount):
        
        cls.flat_discount = new_flat_discount
    
    @staticmethod
    def greet():
        
        print("Have a Great Shopping")
    
a = Cart()

a.add_items("Book", 4)

a.display_items()

Cart.update_flat_discount(50)

print(Cart.flat_discount)

Cart.greet()