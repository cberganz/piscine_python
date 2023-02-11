
class Recipe:
    def __init__(self, name, lvl, time, ingredients, brief, rtype):
        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ingredients
        self.description = brief
        self.recipe_type = rtype

    def __str__(self):
        txt="Recipe for " + self.name + ":\n" + "Level: " + str(self.cooking_lvl) + "\nTime to prepare: " + str(self.cooking_time) + "\nRecipe type: " + self.recipe_type + "\nIngredients: " + str(self.ingredients)
        print(txt)
        return txt
