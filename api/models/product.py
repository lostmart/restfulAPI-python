class Product:
  def __init__(self, price, description, images):
    self.price = price
    self.description = description
    self.images = images

product1 = Product(32, "la description", ["1", 2, 3])

print(product1.images)

