class Customer:
    def __init__(self,name):
       self.name=self.validate_name(name)

    def validate_name(self,name):
        if isinstance(name,str)and 15>= len(name) >=1 :
            return name
        else:
            raise ValueError("Unavailable")
        
    


class Coffee:
    def __init__(self,name):
        if hasattr(self,_name):
            raise AttributeError("invalid choice...choose another coffee")
    def validate_name(self,name):
        if isinstance(name,str)and  len(name) >=3 :
            return name
        else:
            raise ValueError("Unavailable")
        




class Order:
    pass


customer=Customer("")
print(customer.name)
