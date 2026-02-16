class Order:
    def __init__(self):
        self.cart=[]
    def add_items(self,item_name,price,quantity):
        current=[{"item_name":item_name,"price":price,"quantity":quantity}]
        self.cart.append(current)
    def calculate(self):
        sum =0
        for i in self.cart:
            sum=sum+i[self.price*self.quantity]
        print(sum)
new=Order()