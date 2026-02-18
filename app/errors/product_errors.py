class ProductError(Exception):
    """Base class for product-related errors"""
    pass

class EmptyNameError(ProductError):
    pass

class InvalidPriceError(ProductError):
    pass

class InvalidAmountError(ProductError):
    pass

class ProductNotFoundError(ProductError):
    pass