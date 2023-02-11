import sys

cookbook = {
        "sandwich": (["ham", "bread", "cheese", "tomatoes"], "lunch", 10),
        "cake": (["flour", "sugar", "eggs"], "dessert", 60),
        "salad": (["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15),
}

def printRecipesNames():
    for recipe in cookbook.keys():
        print(recipe)

def printRecipeByName(name):
    print("Recipe for " + name + ":")
    print("     Ingredients list: {}".format(cookbook[name][0]))
    print("     To be eaten for {}.".format(cookbook[name][1]))
    print("     Takes {} minutes of cooking.".format(cookbook[name][2]))

def deleteRecipe(name):
    if name in cookbook.keys():
        del cookbook[name]
        print("Recipe for " + name + " deleted!")
    else:
        print("Recipe " + name + " not found!")

def newRecipe():
    name = input("Enter a name:\n")
    if name in cookbook.keys():
        print("Recipe already exist.")
        return
    ingredients = []
    item = None
    print("Enter ingredients:")
    while item != "":
        item = input()
        if item != "":
            ingredients.append(item)
    meal = input("Enter a meal type:\n")
    prep_time = input("Enter a preparation time:\n")
    cookbook[name] = (ingredients, meal, prep_time)

def printOptions():
    print("List of available option:")
    print("    1: Add a recipe")
    print("    2: Delete a recipe")
    print("    3: Print a recipe")
    print("    4: Print the cookbook")
    print("    5: Quit\n")

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 recipe.py")
        exit(1)
    print("Welcome to the Python Cookbook !")
    option = 0
    while option != 5:
        printOptions()
        try:
            option = int(input("Please select an option:\n"))
        except ValueError:
            option = 0
        print()
        if option == 1:
            newRecipe()
        elif option == 2:
            toDel = input("Enter the name of the recipe you wanna delete:\n")
            print()
            deleteRecipe(toDel)
        elif option == 3:
            toPrint = input("Enter the name of the recipe you wanna print:\n")
            print()
            printRecipeByName(toPrint)
        elif option == 4:
            printRecipesNames()
        elif option == 5:
            print("Cookbook closed. Goodbye!")
        else:
            print("Sorry, this option does not exist.")
        print()
