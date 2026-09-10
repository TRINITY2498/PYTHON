# Attributes of an Object.

"""

class Mobile:
    
    def __init__(self, model, camera):
        
        self.model = model 
        self.camera = camera
        
mobile_obj = Mobile("Galaxy M51", "64 MP")

print(mobile_obj.model)

"""

# Accessing in Other Methods.

class Mobile:
    
    def __init__(self, model):
        
        self.model = model
    
    def get_model(self):
        
        print(self.model)
    
obj1 = Mobile("Galaxy M51")

obj1.get_model()
        
        