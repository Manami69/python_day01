from book import Book
from recipe import Recipe

# Creating a recipe book
allRecipe = Book("Toutes les recettes du monde entier")

# Creating some recipes
sandwichMM = Recipe("Sandwich Merguez Moutarde", 1, 20, [
                    'pain', 'moutarde', 'merguez'], "lunch",
                    "Faire cuire la merguez et en fourrer \
le sandwish.\nAspergez de moutarde")
flambadou = Recipe("Flambadiode", 5, 120, [
                   'huitre', 'foie gras', 'lard', 'fer rouge',
                   'une audience a faire flamber'], "lunch")
carrot = Recipe("Carrot cake", 2, 30, [
                'carottes', 'cake', 'epices'], 'dessert')
meat = Recipe("viande froide", 1, 100000, [
              'viande', 'abattoir', 'couteau', 'frigo'],
              "starter", "TW carniste")

# Testing the classes

print(sandwichMM)
print("book créé à {}, derniere modification à {}".format(
    allRecipe.creation_date, allRecipe.last_update))
allRecipe.add_recipe(sandwichMM)
allRecipe.add_recipe(flambadou)
allRecipe.add_recipe(carrot)
allRecipe.add_recipe(meat)
print("book créé à {}, derniere modification à {}".format(
    allRecipe.creation_date, allRecipe.last_update))
print("looking for all lunch")
allRecipe.get_recipes_by_types("lunch")
allRecipe.get_recipe_by_name("Carrot cake")
