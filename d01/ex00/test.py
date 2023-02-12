from book import Book
from recipe import Recipe

if __name__ == '__main__':

    # Normal usage
    print("\n\n1. Normal usage:")

    cookbook = Book("My recipes")

    print("\n1.1 constructor:")
    recipe1 = Recipe("Pasta with butter", 4, 5, ["Pasta", "Butter"], "A meal made from pasta and butter. Perfect for every day.", "lunch")
    recipe2 = Recipe("Pasta with pesto", 4, 5, ["Pasta", "Pesto"], "A meal made of pasta and pesto. Perfect for every day.", "lunch")
    recipe3 = Recipe("Fruits salad", 4, 5, ["Orange juice", "Apple", "Bananas", "Fruits you like"], "Some fruits.", "dessert")
    recipe4 = Recipe("Cheese", 4, 5, ["Cheese", "Bread"], "Just cheese.", "dessert")
    recipe5 = Recipe("Salad", 4, 5, ["Salad", "Tomatoes", "Olive oil"], "Warning: It's green.", "starter")
    recipe6 = Recipe("Cheese", 4, 5, ["Cheese", "Bread"], "Just cheese.", "starter")
    recipe7 = Recipe("Carot", 4, 5, ["Carot", "Olive oil"], "Warning: It's orange", "starter")

    print("\n1.2 add_recipe():")
    cookbook.add_recipe(recipe1)
    cookbook.add_recipe(recipe2)
    cookbook.add_recipe(recipe3)
    cookbook.add_recipe(recipe4)
    cookbook.add_recipe(recipe5)
    cookbook.add_recipe(recipe6)
    cookbook.add_recipe(recipe7)

    print("\n1.3 get_recipes_by_types:")
    cookbook.get_recipes_by_types("starter")
    cookbook.get_recipes_by_types("lunch")
    cookbook.get_recipes_by_types("dessert")

    print("\n1.4 get_recipes_by_name:")
    cookbook.get_recipe_by_name("Cheese")
    cookbook.get_recipe_by_name("Salad")
    cookbook.get_recipe_by_name("Pasta with pesto")

    print("\n1.5 print(cookbook):")
    print(cookbook)


    # Error management
    print("\n\n2. Error management:\n")

    cookbook = Book("My recipes")

    print("\n2.1 Invalid argument name:")
    try:
        recipe1 = Recipe(1, 4, 5, ["ing1", "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.2 Invalid argument lvl (wrong type):")
    try:
        recipe1 = Recipe("Miam", "Hey", 5, ["ing1", "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.3 Invalid argument time (wrong type):")
    try:
        recipe1 = Recipe("Miam", 4, "he", ["ing1", "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.4 Invalid argument ingredients (not a str inside):")
    try:
        recipe1 = Recipe("Miam", 4, 5, [1, "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.5 Invalid argument ingredients (not a list):")
    try:
        recipe1 = Recipe("Miam", 4, 5, "ing1", "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.6 Invalid argument brief:")
    try:
        recipe1 = Recipe("Miam", 4, 5, ["ing1", "ing2"], 2, "lunch")
    except ValueError as e:
        print(e)

    print("\n2.7 Invalid argumnt rtype (wrong type):")
    try:
        recipe1 = Recipe("Miam", 4, 5, ["ing1", "ing2"], "No brief", 1)
    except ValueError as e:
        print(e)

    print("\n2.8 Invalid argumnt rtype (not in restrict):")
    try:
        recipe1 = Recipe("Miam", 4, 5, ["ing1", "ing2"], "No brief", "No")
    except ValueError as e:
        print(e)

    print("\n2.9 Invalid argument time (not in range):")
    try:
        recipe1 = Recipe("Miam", 4, 0, ["ing1", "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.10 Invalid argument lvl (not in range - < 1):")
    try:
        recipe1 = Recipe("Miam", 0, 5, ["ing1", "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.11 Invalid argument lvl (not in range - > 5):")
    try:
        recipe1 = Recipe("Miam", 6, 5, ["ing1", "ing2"], "No brief", "lunch")
    except ValueError as e:
        print(e)

    print("\n2.12 add_recipe (invalid argument):")
    cookbook.add_recipe("Hello")

    print("\n2.13 get_recipe_by_type (invalid argument):")
    cookbook.get_recipes_by_types(1)

    print("\n2.14 get_recipe_by_type (not exist):")
    cookbook.get_recipes_by_types("No")

    print("\n2.15 get_recipe_by_name (invalid argument):")
    cookbook.get_recipe_by_name(1)

    print("\n2.16 get_recipe_by_name (not exist):")
    cookbook.get_recipe_by_name("No")

    print()
