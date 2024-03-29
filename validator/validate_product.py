from vending.models.products import Product

def amount_available_greater_than_15(amountAvailable):
    if amountAvailable > 15: return True
    else: return False

def amount_available_is_not_int(amountAvailable):
    if not isinstance(amountAvailable, int): return True
    else: return False

def amount_available_is_negative(amountAvailable):
    if amountAvailable < 0: return True
    else: return False

def cost_is_not_multiple_of_5(cost):
    if cost%5 != 0: return True
    else: return False

def cost_is_negative(cost):
    if cost < 0: return True
    else: return False

def cost_is_not_int(cost):
    if isinstance(cost, bool): return True
    elif not isinstance(cost, int): return True
    else: return False

def productName_exists(productName):
    existing_product = Product.query.filter_by(productName=productName).first()
    if existing_product: return True
    else: return False

def productName_longer_than_32_characters(productName):
    if len(productName) > 32: return True
    else: return False

def validate_amountAvailable(amountAvailable):
    if amountAvailable is None: return (True, 'amountAvailable must not be None')
    if amount_available_is_not_int(amountAvailable): return (True, 'amountAvailable must be of type int')
    if amount_available_greater_than_15(amountAvailable):
        return (True, 'amountAvailable must be lesser than or equal to 15')
    if amount_available_is_negative(amountAvailable): return (True, 'amountAvailable must be positive')
    return (False, '')

def validate_cost(cost):
    if cost is None: return (True, 'cost must not be None')
    if cost_is_not_int(cost): return (True, 'cost must be of type int')
    if cost_is_not_multiple_of_5(cost): return (True, 'cost must be a multiple of 5')
    if cost_is_negative(cost): return (True, 'cost must be positive')
    return (False, '')

def validate_productName_when_adding_product(productName):
    if productName is None: return (True, 'productName cannot be None')
    if productName_exists(productName): return (True, 'productName already exists')
    if productName_longer_than_32_characters(productName): return (True, 'productName must be shorter than 32 characters')
    return (False, '')

def validate_productName_during_update(productName):
    if productName is None: return (True, 'productName cannot be None')
    if productName_longer_than_32_characters(productName): return (True, 'productName must be shorter than 32 characters')
    return (False, '')
