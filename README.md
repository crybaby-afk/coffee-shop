# A Customer can place many Orders.
# A Coffee can have many Orders.
# Each Order is associated with one Customer and one Coffee.
# Classes and Their Responsibilities
1. ## Customer
Represents a customer of the coffee shop.
Attributes:
name: The name of the customer (must be a string between 1 and 15 characters).
orders: A list of all orders placed by the customer.
Methods:
validate_name: Ensures the customer's name is valid.
orders: Returns all orders placed by the customer.
coffees: Returns a unique list of coffees ordered by the customer.
create_order: Creates and returns a new Order associated with the customer and a specific coffee.
2. Coffee
Represents a type of coffee offered at the shop.
Attributes:
name: The name of the coffee (must be a string with at least 3 characters and cannot be changed after creation).
Methods:
validate_name: Ensures the coffee's name is valid.
orders: Returns all orders associated with this coffee.
customers: Returns all unique customers who have ordered this coffee.
num_orders: Returns the total number of orders for this coffee.
average_price: Calculates the average price of all orders for this coffee.
3. Order
Represents an order placed by a customer for a specific coffee.
Attributes:
customer: The customer who placed the order.
coffee: The coffee associated with the order.
price: The price of the order (must be a float between 1.0 and 10.0).
Methods:
validate_price: Ensures the price is valid.
validate_customer: Ensures the customer is valid.
validate_coffee: Ensures the coffee is valid.