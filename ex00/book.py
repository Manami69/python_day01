import datetime

class Book():

    def __init__(self, name, recipe_list={'starter' : {}, 'lunch' : {}, 'dessert' : {}}, last_update="", creation_date=""):
        self.last_update = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.creation_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.name = name
        if isinstance(recipe_list, dict) is False:
            print ("recipe list need to be a dictionnary with 3 keys 'lunch', 'starter' ans 'dessert")
            return

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """

        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""

        pass
