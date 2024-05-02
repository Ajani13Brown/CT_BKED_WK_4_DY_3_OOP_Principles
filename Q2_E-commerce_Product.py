class Product():
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def show_info(self):
        print(f'Product Id: {self.product_id}')
        print(f'Product Name: {self.name}')
        print(f'Price: {self.price}')

class Clothing(Product):
    def __init__(self,product_id ,name ,price, designer, size):
        super(). __init__(product_id, name, price)
        self.designer = designer
        self.size = size

    def show_info(self):
        print(f'Hannah bought {self.designer} {self.product_id} size {self.size} for {self.price}')


winter_jacket = Clothing('Jacket', 'Fleece Coat', 79.99, 'NorthFace', 'Medium')

winter_jacket.show_info()