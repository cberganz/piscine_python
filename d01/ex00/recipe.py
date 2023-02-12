class Recipe:
    def __init__(self, name, lvl, time, ingredients, brief, rtype):
        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ingredients
        self.description = brief
        self.recipe_type = rtype
        self.check_args()

    def __str__(self):
        txt="\n\tRecipe for " + self.name + ":" \
        + "\n\tLevel: " + str(self.cooking_lvl) \
        + "\n\tTime to prepare: " + str(self.cooking_time) \
        + "\n\tRecipe type: " + self.recipe_type \
        + "\n\tIngredients: " + str(self.ingredients) \
        + "\n"
        return txt

    def check_args(self):
        if not isinstance(self.name, str):
            raise ValueError("Invalid argument for name.")
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl < 1 or self.cooking_lvl > 5:
            raise ValueError("Argument cooking_lvl must be an integer between 1 and 5.")
        if not isinstance(self.cooking_time, int) or self.cooking_time < 1:
            raise ValueError("Argument cooking_time must be an integer >= 1.")
        if not isinstance(self.ingredients, list):
            raise ValueError("Argument ingredient should be an iterable list.")
        for item in self.ingredients:
           if not isinstance(item, str):
               raise ValueError("Ingredients list contains a non str item.")
        if not isinstance(self.description, str):
            raise ValueError("Argument description should be an str.")
        if self.recipe_type != "starter" and self.recipe_type != "lunch" and self.recipe_type != "dessert":
            raise ValueError("Argument rtype should be one of 'starter', 'lunch' or 'dessert'.")
