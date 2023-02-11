from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipe_list = { "starter": [], "lunch": [], "dessert": [] }

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self.name + " Cookbook :\n"
        + "Creation date: " + self.creation_date
        + "\nLast update: " + self.last_update
        + "\nRecipes: \n"
        + "  Starters: " + self.recipe_list["starter"]
        + "\n  Lunch: " + self.recipe_list["lunch"]
        + "\n  Desserts: " + self.recipe_list["dessert"]
        print(txt)
        return txt

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        if not isinstance(name, str):
            print("Error: not a valid name")
        else:
            for cat in self.recipe_list.values():
                for recipe in cat:
                    if recipe == name:
                        print(recipe)
                        return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            print("Error: not a valid name")
        else:
            if not recipe_type in self.recipe_list:
                print("Recipe type not found in " + self.name + " cookbook!")
            else:
                for recipe in self.recipe_list[recipe_type]:
                    print(recipe)


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Invalid recipe: is not an instance of Recipe!")
            return
        if recipe.recipe_type in self.recipe_list:
            self.recipe_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            print("Invalid recipe type: should be 'starter' or 'lunch' or 'dessert'!")
