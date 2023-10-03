class Product:
    """
    Returns an object: Product with the following attributes

    Attributes:
        price: float
        description: string
        imgUrl: string

    """

    def __init__(self, price, description, imgUrl):
        self.product_id = None
        self.price = price
        self.description = description
        self.imgUrl = imgUrl
