class Mobile:
    
    def __init__(self, model, camera):
        
        self.model = model
        self.camera = camera 
    
    def make_call(self, number):
        
        print("Calling...{}".format(number))
        
mobile_obj_1 = Mobile("Galaxy M31", "64MP")

print(id(mobile_obj_1))
print(type(mobile_obj_1))

mobile_obj_2 = Mobile("Oneplus 8T", "64MP")

print(id(mobile_obj_2))
print(type(mobile_obj_2))

# mobile_obj.make_call("7058438724")

