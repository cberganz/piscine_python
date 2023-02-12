class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise ValueError("Invalid arguments in instanciation of 'GotCharacter'.")
        self.first_name = first_name
        self.is_alive = is_alive

    @property
    def __dict__(self):
        return "\nFirst name: " + self.first_name \
        + "\nFamily name: " + self.family_name \
        + "\nHouse words: " + self.house_words \
        + "\nVital informations: " + ("En vie" if self.is_alive else "Mort(e)")
        + "\n"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
        print(self.first_name + " from the " + self.family_name + "'s family just died. " + self.house_words + ".")

class Stark(GotCharacter):
    """ A class representing the Stark family. Or when bad things happen to good people. """
    def __init__(self, first_name=None, is_alive=True):
         super().__init__(first_name=first_name, is_alive=is_alive)
         self.family_name = "Stark"
         self.house_words = "Winter is Coming"

if __name__ == '__main__':

    # Normal behavior
    print("\n1. Normal behavior")

    print("\n1.1 Class instanciation")
    arya = Stark("Arya")

    print("\n1.2 print_house_words()")
    arya.print_house_words()

    print("\n1.3 __dict__")
    print(arya.__dict__)

    print("\n1.4 Call to die()")
    arya.die()

    print("\n1.5 __dict__")
    print(arya.__dict__)

    # Error management
    print("\n\n2. Error management")

    print("\n2.1 Invalid argument first_name")
    try:
        arya = Stark(1.0)
        print("Failure")
    except ValueError as e:
        print(e)
        print("Success")

    print("\n2.2 Invalid argument is_alive")
    try:
        arya = Stark("Arya", is_alive=1.0)
        print("Failure")
    except ValueError as e:
        print(e)
        print("Success")

    print()
