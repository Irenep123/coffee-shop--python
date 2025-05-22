from customer import Customer
from coffee import Coffee

# Create some customers
c1 = Customer("Joe")
c2 = Customer("Becky")

# Create some coffee types
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create some orders
c1.create_order(coffee1, 5.5)
c1.create_order(coffee1, 6.0)
c2.create_order(coffee1, 4.5)
c2.create_order(coffee2, 3.0)

# Test outputs
print("Most aficionado for Latte:", Customer.most_aficionado(coffee1).name)
print("Average price for Latte:", round(coffee1.average_price(), 2))
print("Coffees ordered by Joe:", [coffee.name for coffee in c1.coffees()])
print("Orders by Becky:", c2.orders())
print("Total Latte orders:", coffee1.num_orders())