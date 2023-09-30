class Product:
  def __init__(self, price, description, images):
    self.price = price
    self.description = description
    self.images = images


try:
  product1 = Product( "la description", ["1", 2, 3])
  print(product1.images)
except Exception as e:  
  print("noooooooooooo !!!", e)


