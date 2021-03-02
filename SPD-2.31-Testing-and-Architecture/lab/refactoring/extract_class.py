# by Kami Bigdely
# Extract Class
foods = {'butternut squash soup':[45, True, 'soup','North African',\
     ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
        ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
          'they get soft and golden on top 2. Put all in blender with'
          'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
               '. Add coconut milk. Simmer for 5 mintues.'],
        'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
            '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                '4. Mixed them thoroughly'],
        'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
            'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                'the seasonings 2. In a bowl, mix ground beef with the'
                'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

class Food:
    def __init__(self, name, prep_time, is_veggie, food_type, 
                cuisine, ingredients, recipe):
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.recipe = recipe
    
    def print_details(self):
        print("Name:", name)
        print("Prep time:", prep_time, "mins")
        print("Is Veggie?", is_veggie)
        print("Food Type:", food_type)
        print("Cuisine:", cuisine)
        for ingredient in self.ingredients:
            print(ingredient, end=', ')
        print()
        print("recipe", recipe)
        print("***")


for key, value in foods.items():
    name = key
    prep_time = value[0]
    is_veggie = 'Yes' if value[1] else "No"
    food_type = value[2]
    cuisine = value[3]
    ingredients = []
    for ingredient in value[4]:
        ingredients.append(ingredient)
    recipe = value[5]

    food = Food(name, prep_time, is_veggie, food_type, cuisine, ingredients, recipe)
    food.print_details()