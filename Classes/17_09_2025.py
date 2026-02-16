# An online marketplace wants to build a shipping management module for tracking both normal and express deliveries.
# You are asked to create two Python classes to handle this system.

# 1. Class: Shipping
# This class should store the basic details of any order.
# It must have attributes for the order_id ,amount, and shipping_days.
# Include methods to:

# estimate_delivery() - Returns the estimated number of shipping days.

# update_amount(value) - Update the amount by adding a given value to it.

# 2. Class: ExpressShipping 
# The company also provides an express delivery option, so create a subclass called ExpressShipping that extends Shipping.
# It should include an additional attribute for an extra charge.

# Add methods to:

# calculate_total() - Calculate and return the total amount by adding the extra charge to the base amount.

# faster_shipping() - Reduce the shipping days by 2 for faster delivery and return the updated days.

# Note: Write classes alone , you need not create objects for each

class Shipping:
    def __init__(self,order_id ,amount, shipping_days):
        self.order_id = order_id
        self.amount = amount
        self.shipping_days = shipping_days

    def estimate_delivery(self):
        return self.shipping_days
    def update_amount(self,value):
        self.amount+=value
class ExpressShipping(Shipping):
    def __init__(self,order_id ,amount, shipping_days,extra_charge):
        self.extra_charge = extra_charge
        super().__init__(order_id ,amount, shipping_days)
    def calculate_total(self):
        self.extra_charge += self.amount
        return self.amount
    def faster_shipping(self):
        self.shipping_days-=2
        return self.shipping_days

