#Put this at the top of your kata00.py file
kata = (19,42,21)

if __name__ == '__main__':
    s = "{}".format(kata).strip('(').strip(')')
    print("The " + str(len(kata)) + " numbers are: " + s)
