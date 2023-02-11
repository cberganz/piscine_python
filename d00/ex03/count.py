import string
import sys

def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if args is None or len(args) == 0:
        args = input("What is the text to analyze? ")
    else:
        args = args[0]
    if type(args) != str:
        print("AssertionError: argument is not a string")
        return
    count_upper = sum(1 for char in args if char.isupper())
    count_lower = sum(1 for char in args if char.islower())
    count_punctuation = sum(1 for char in args if char in string.punctuation)
    count_spaces = sum(1 for char in args if char.isspace())
    print("The text contains " + str(len(args)) + " character(s):")
    print("- " + str(count_upper) + " upper letter(s)")
    print("- " + str(count_lower) + " lower letter(s)")
    print("- " + str(count_punctuation) + " punctuation mark(s)")
    print("- " + str(count_spaces) + " space(s)")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: invalid args count!")
        exit(1)
    text_analyzer(sys.argv[1])
