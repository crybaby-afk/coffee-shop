class Customer:
    def __init__(self,name):
       self.name=self.validate_name(name)

    def validate_name(self,name):
        if isinstance(name,str)and 15>= len(name) >=1 :
            return name
        else:
            raise ValueError("Unavailable")
        
    


class Coffee:
    def __init__(self, name):
        # Check if _name is already set
        if hasattr(self, "_name"):
            raise AttributeError("Invalid choice...coffee name cannot be changed after initialization.")
        
        # Validate and assign the name
        self._name = self.validate_name(name)

    @staticmethod
    def validate_name(name):
        """Validates the coffee name."""
        if isinstance(name, str) and len(name) >= 3:
            return name
        else:
            raise ValueError("Unavailable: Name must be a string with at least 3 characters.")

    @property
    def name(self):
        """Returns the coffee's name."""
        return self._name
    
        



coffee=Coffee("mocha")
coffee.name = ("chai moto")
print (coffee.name)
