# by Kami Bigdely
# Remove control flag
"""
METHOD DOCSTRING
"""
def find_food(food, fridge):
    """
    FUNC DOCSTRING
    """
    for item in fridge:
        if food in item:
            return item

        return None

if __name__ == "__main__":
    FOOD = 'wesabi'
    food_list = ['onion', 'cucumber','Guacamole', 'kabob barg', 'wesabi']
    found_item = find_food(FOOD, food_list)
    print(FOOD, "Found: " + found_item  if found_item is not None else "not found")
