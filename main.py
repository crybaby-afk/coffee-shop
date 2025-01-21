class Customer:
    def __init__(self, name):
        self.name = self.validate_name(name)
        self.orders_list = []  # Uses a distinct name to avoid conflicts

    def validate_name(self, name):
        if isinstance(name, str) and 15 >= len(name) >= 1:
            return name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")


    def orders(self):
        # Return all orders for this customer
        return [order for order in Order.all if order.customer == self]
    
    def coffee(self):
        # Return unique coffee for this customer
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
        self._name = self.validate_name(name)

    def validate_name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            return name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Cannot modify the coffee name after initialization.")

    def num_orders(self):
        """Return the total number of orders for this coffee."""
        return len([order for order in Order.all if order.coffee == self])

    def average_price(self):
        """Return the average price of this coffee across all orders."""
        orders = [order for order in Order.all if order.coffee == self]
        if orders:
            total_price = sum(order._price for order in orders)
            return total_price / len(orders)
        return 0
    @name.setter
    def name(self, new_name):
        raise AttributeError("Cannot modify the coffee name after initialization.")

    def __setattr__(self, key, value):
        if key == "_name" and hasattr(self, "_name"):
            raise AttributeError(f"{key} cannot be modified after initialization.")
        super().__setattr__(key, value)



class Order:
    all = []  # List to store all orders

    def __init__(self, price, customer=None, coffee=None):
        if hasattr(self, "_price"):
            raise AttributeError("Price cannot be changed after input.")

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



customer1 = Customer("astalavista")
coffee1 = Coffee("Latte")

order1 = customer1.create_order(coffee1, 5.5)

print(f"Customer: {customer1.name}, Coffee: {coffee1.name}, Average Price: {coffee1.average_price()}")

customer2 = Customer("LARRY")
order2 = customer2.create_order(coffee1, 6.5)

print(f"Customer: {customer2.name}, Coffee: {coffee1.name}, Average Price: {coffee1.average_price()}")



