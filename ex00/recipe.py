import sys


class Recipe():

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description=""):
        """ Init your recipe with name, cooking level, cooking time,
 ingredients, recipe type and a desciption (optionnal)"""
# Checking name
        if isinstance(name, str) is False:
            #            del self
            raise TypeError("The name must be a string")

# checking cooking level

        if isinstance(int(cooking_lvl), int) is False:
            #            del self
            raise TypeError("Cooking level must be an integer \
between 1 and 5")

        elif int(cooking_lvl) < 1 and int(cooking_lvl) > 5:
            #            del self
            raise ValueError("Cooking level must be between \
lvl 1 and 5")


# checking cooking time

        if isinstance(int(cooking_time), int) is False:
            #            del self
            raise TypeError("Cooking level must be an integer")

        elif int(cooking_time) < 0:
            #            del self
            raise ValueError("Cooking level must be a positive number")

# checking ingredients

        if isinstance(ingredients, list) is False:
            #            del self
            raise TypeError("ingredients must be a list")

# checking recipe type
        if recipe_type not in ['starter', 'lunch', 'dessert']:
            #            del self
            raise ValueError("Recipe type must be starter, lunch or \
dessert")

        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.name = name
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe for {} - Cooking level {}\nThis recipe is a {} \
and you'll need {} min to cook it\nIngredients are {}\n{}".format(
            self.name, self.cooking_lvl, self.recipe_type, self.cooking_time,
            self.ingredients, self.description)
        return txt
