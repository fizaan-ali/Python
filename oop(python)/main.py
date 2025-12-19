import csv


class Item:
    # class attribute -> belongs to the class itself
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: int, quantity=0):
        # Runs validations to the received arguments
        assert price >= 0, f"Price {price} is not >= 0!"
        assert quantity >= 0, "Quantity should be >= 0!"

        # Assigns to self object
        self.name = name
        self.price = price 
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) 

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        

    def __repr__(self): # how objects are displayed in console
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero!
        # for i.e 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer() 
        elif isinstance(num, int):
            return True
        else:
            return False


item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 250, 8)
item2.has_numpad = False # only attribute for item2
item2.pay_rate = 0.7
item2.apply_discount() # now it will apply dicount of at 0.7
print(item2.price)

print(Item.__dict__) # __dict__ -> magic attribute that gives all the attributes available for that thing -> al the attributes for class level
print(item1.__dict__) # all the attributes for instance level

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

for instance in Item.all: # now this will print all the names of our items 
    print(instance.name)


print(Item.is_integer(5.0))