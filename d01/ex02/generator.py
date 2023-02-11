import sys
import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str) or not isinstance(sep, str):
        return "Error: Invalid arguments"
    else:
        if option == "unique":
            ret = list(dict.fromkeys(text.split(sep)))
        elif option == "shuffle":
            lst = text.split(sep)
            for i in range(len(lst)):
                ret = ""
                save = []
                while ret == "" or ret in save:
                    ret = random.choice(lst)
                save.append(ret)
                del lst[lst.index(ret)]
                yield ret
            return
        elif option == "ordered":
            ret = sorted(text.split(sep))
        elif option is None:
            ret = text.split(sep)
        else:
            return "Error: Invalid option."
        for word in ret:
            yield word

if __name__ == '__main__':
    text = "Le Le Lorem Ipsum est simplement du faux texte."
    print("\nNone:")
    for word in generator(text):
        print(word)
    print("\nUnique:")
    for word in generator(text, " ", "unique"):
        print(word)
    print("\nShuffle:")
    for word in generator(text, " ", "shuffle"):
        print(word)
    print("\nordered:")
    for word in generator(text, " ", "ordered"):
        print(word)
    print()
