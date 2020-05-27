import sys
import datetime
from recipe import Recipe


class Book():

    def __init__(self, name):
        if isinstance(name, str) is False:
            print("Name for your book need to be a string")
        else:
            self.name = name
        self.last_update = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S")
        self.creation_date = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S")
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipe_list:
            for i in self.recipe_list[key]:
                if name == i.name:
                    print(str(i))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key in self.recipe_list:
            if key == recipe_type:
                for i in self.recipe_list[key]:
                    print(str(i))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) is False:
            print("You need to put a Recipe too add one on the book")
            return
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S")
        print("{} recipe succesfully added to {} book".format(
            recipe.name, self.name))
