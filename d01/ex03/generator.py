import sys
import random

def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str) or not isinstance(sep, str):
        yield "ERROR"
    else:
        if option == "unique":
            for word in list(dict.fromkeys(text.split(sep))):
                yield word
        elif option == "shuffle":
            lst = text.split(sep)
            for i in range(len(lst)):
                ret = random.choice(lst)
                del lst[lst.index(ret)]
                yield ret
        elif option == "ordered":
            for word in sorted(text.split(sep)):
                yield word
        elif option is None:
            for word in text.split(sep):
                yield word
        else:
            yield "ERROR"

if __name__ == '__main__':

    # Options proof
    print("\n1. Options proof")

    text = "Le Le Lorem Ipsum est simplement du faux texte."

    print("\n1.1 None:")
    for word in generator(text):
        print(word)

    print("\n1.2 Unique:")
    for word in generator(text, " ", "unique"):
        print(word)

    print("\n1.3 Shuffle:")
    for word in generator(text, " ", "shuffle"):
        print(word)

    print("\n1.4 ordered:")
    for word in generator(text, " ", "ordered"):
        print(word)

    print("\n1.5 With different sep:")
    for word in generator(text, sep="e"):
        print(word)

    print()

    # Error management
    print("\n2. Error management")

    print("\n2.1 Invalid arg text")
    text=1.0
    for word in generator(text, sep="."):
        print(word)

    print("\n2.2 Invalid arg sep")
    for word in generator("Lorem Ipsum", sep=1.0):
        print(word)

    print("\n2.3 Invalid arg option")
    for word in generator("Lorem Ipsum", option="Not a good option"):
        print(word)

    print()
