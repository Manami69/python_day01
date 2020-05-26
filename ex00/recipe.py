class recipe():

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self.name = name
        self.description = description
# checking cooking level
 
        if isinstance(int(cooking_lvl), int) is False:
            print("Cooking level must be an integer between 1 and 5")
            return
        elif int(cooking_lvl) < 1 and int(cooking_lvl) > 5:
            print("Cooking level must be between lvl 1 and 5")
            return
        else:
            self.cooking_lvl = int(cooking_lvl)

# checking cooking time

        if isinstance(int(cooking_time), int) is False:
            print("Cooking level must be an integer")
            return
        elif int(cooking_time) < 0:
            print("Cooking level must be a positive number")
            return
        else:
            self.cooking_time = int(cooking_time)

# checking ingredients

        if isinstance(ingredients, list) is False:
            print("ingredients must be a list")
            return
        else:
            self.ingredients = ingredients

# checking recipe type

        if recipe_type is not 'starter' or recipe_type is not 'lunch' or recipe_type is not 'dessert':
            print("Recipe type must be starter, lunch or dessert")
            return
        else:
            self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe for {} - Cooking level {}\nThis recipe is a {} \
and you'll need {} min to cook it\nIngredients are {}\n{}".format(
        self.name, self.cooking_lvl, self.recipe_type, self.cooking_time,
        self.ingredients, self.description)
        return txt