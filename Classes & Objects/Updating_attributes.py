# Updating Attributes via another methods.

class Mobile:
    
    
    
    def __init__(self, model):
        
        self.model = model
    
    def update_model(self, model):
        
        self.model = model
    
obj1 = Mobile("Galaxy M51")

obj1.update_model("Galaxy J7")

print(obj1.model)
        
        