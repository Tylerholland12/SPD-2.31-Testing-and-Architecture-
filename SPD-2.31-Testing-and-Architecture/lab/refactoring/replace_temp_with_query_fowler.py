# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
"""
Leading docstring
"""
QUANT = 0
ITEM_PRICE = 0
def get_price():
    """
    docstring for functinon
    """
    base_price = QUANT * ITEM_PRICE
    discount_factor = 0
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor
