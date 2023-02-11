from book import Book
from recipe import Recipe

if __name__ == '__main__':
    cookbook = Book("My recipes")
    recipe1 = Recipe("Miam", 2, 5, ["ing1", "ing2"], "No brief", "lunch")
    cookbook.add_recipe(recipe1)
    cookbook.get_recipes_by_types("lunch")
    cookbook.get_recipe_by_name("Miam")
