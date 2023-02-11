import sys

if len(sys.argv) < 2:
    print("Usage: python3 exec.py [Arguments list].")
    sys.exit(1)

print(' '.join(sys.argv[1:])[::-1].swapcase())
