class Product:
    """
    Returns an object: Product with the following attributes

    Attributes:
        price: float
        description: string
        images: list ( a list of images files names )

    """

    def __init__(self, price, description, images):
        self.price = price
        self.description = description
        self.images = images
