class ProductError(Exception):
    pass

class EmptyNameError(ProductError):
    pass

class InvalidPriceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class ProductNotFoundError(Exception):
    pass