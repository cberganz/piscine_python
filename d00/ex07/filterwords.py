import sys
import argparse
import string

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('S', type=str)
    parser.add_argument('N', type=int)
    args = parser.parse_args()
    initialList = args.S.split()
    noPunctuationList = [s.translate(str.maketrans('', '', string.punctuation)) for s in initialList]
    finalList = [x for x in noPunctuationList if len(x) > args.N]
    print(finalList)
