import sys

if len(sys.argv) == 1:
    print("Usage: python3 whois.py [Numeric argument].")
    sys.exit(1)

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("AssertionError: argument is not an integer")
    sys.exit(1)

argAsNum = int(sys.argv[1])

if (argAsNum == 0):
    print("I'm Zero.")
elif(argAsNum % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
