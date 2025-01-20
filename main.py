class Customer:
    def __init__(self, name):
        self.name = self.validate_name(name)
        self.orders_list = []  # Use a distinct name to avoid conflicts

    def validate_name(self, name):
        if isinstance(name, str) and 15 >= len(name) >= 1:
            return name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        # Return all orders for this customer
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        # Return unique coffees for this customer
        return set(order.coffee for order in Order.all if order.customer == self)

    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee) and isinstance(price, float):
            new_order = Order(price, self, coffee)
            self.orders_list.append(new_order)  # Append the actual order
            return new_order
        else:
            raise ValueError("Invalid coffee or price type.")


class Coffee:
    def __init__(self, name):
        # Check if _name is already set
        if hasattr(self, "_name"):
            raise AttributeError("Invalid choice...coffee name cannot be changed after initialization.")
        
        # Validate and assign the name
        self._name = self.validate_name(name)

    def validate_name(self, name):  
        """Validates the coffee name."""
        if isinstance(name, str) and len(name) >= 3:
            return name
        else:
            raise ValueError("Unavailable: Name must be a string with at least 3 characters.")

    @property
    def name(self):
        """Returns the coffee's name."""
        return self._name

    def __str__(self):
        """Return the coffee name when printed."""
        return self._name

    def __repr__(self):
        """Provide a string representation for debugging."""
        return f"Coffee(name='{self._name}')"

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return set(order.customer for order in Order.all if order.coffee == self)

    def num_orders(self):
        return len(self.orders())  # Return the count of orders

    def average_price(self):
        orders = self.orders()
        if orders:
            return sum(order._price for order in orders) / len(orders)  # Calculate average price
        return 0


class Order:
    all = []  # List to store all orders

    def __init__(self, price, customer=None, coffee=None):
        if hasattr(self, "_price"):
            raise AttributeError("Price cannot be changed after initialization.")

        self.customer = self.validate_customer(customer)
        self.coffee = self.validate_coffee(coffee)
        self._price = self.validate_price(price)
        Order.all.append(self)

    @staticmethod
    def validate_price(price):
        # Validate price
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            return price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")

    @staticmethod
    def validate_customer(customer):
        if isinstance(customer, Customer):
            return customer
        else:
            raise ValueError("Invalid customer.")

    @staticmethod
    def validate_coffee(coffee):
        if isinstance(coffee, Coffee):
            return coffee
        else:
            raise ValueError("Invalid coffee.")



customer = Customer("LARRY")
coffee = Coffee("Latte")

# # Creating an order
order = customer.create_order(coffee, 5.5)


print(coffee.num_orders()) 
print(coffee.average_price()) 




customer = Customer("LARRY")
coffee = Coffee("Latte")

# Creating an order
order = customer.create_order(coffee, 5.5)

print(coffee)  




















