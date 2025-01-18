class Customer:
    def __init__(self,name):
       self.name=self.validate_name(name)
       self.orders = []

    def validate_name(self,name):
        if isinstance(name,str)and 15>= len(name) >=1 :
            return name
        else:
            raise ValueError("Unavailable")
        
        
    def orders(self):
        return set([order for order in Order.all if order.coffee==self])
    
    def customers(self):
        return  set([order for order in order.all if order.customer==self])
    

def create_order(self,coffee,price):
    if isinstance (coffee,Coffee) and isinstance(price,float):
         new_Order=(price,self,coffee)
         self.orders.append()
         return new_Order
    
        
    


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
    
    def orders(self):
        return set([order for order in Order.all if order.coffee==self])
    
    def customers(self):
        return set([order for order in order.all if order.customer==self])
    

    def num_orders



class Order:
    all=[]
    def __init__(self,price,customer=None, coffee=None):
        if hasattr(self, "_price"):
            raise AttributeError("")

        self.customer = self.validate_customer(customer)
        self.coffee = self.validate_coffee(coffee)
        self._price = self.validate_price(price)
        Order.all.append(self)



    def validate_price(price):
        #to validate price
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            return price
        else:
            raise ValueError("invalid price")
        

    def customer(self,customer):
        if isinstance (customer,Customer):
            return customer
        else:
            raise ValueError("Customer is invalid")
        

    
    def Coffee(self,Coffee):
        if isinstance (Coffee,Coffee):
            return Coffee
        else:
            raise ValueError("Coffee is invalid")
            

    
    


    
        



order=Order(10.0)
order.price = ()
print (order.price)
