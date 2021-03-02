# by Kami Bigdely
# Consolidate conditional expressions
"""
LEADING DOCSTRING
"""
def dice(ingredients):
    """
    FUNC DOCSTRING
    """
    print("diced all ingredients.")

def mix_all(diced_ingredients):
    """
    FUNC DOCSTRING
    """
    print("mixed all.")

def add_salt():
    """
    FUNC DOCSTRING
    """
    print('added salt.')

def pour(liquid):
    """
    FUNC DOCSTRING
    """
    print('poured', liquid + '.',)

def make_shirazi_salad(ingredients):
    """
    FUNC DOCSTRING
    """
    required_ingredients = ['cucumber', 'tomato', 'onion', 'lemon juice']
    has_all_ingredients = all(ingredient in ingredients  for ingredient in required_ingredients)
    if has_all_ingredients:
        dice(ingredients)
        mix_all(ingredients)
        add_salt()
        pour('lemon juice')
        print('Your yummy shirazi salad is ready!')
    else:
        print('lacks ingredients.')


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
