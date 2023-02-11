import argparse

parser = argparse.ArgumentParser()
parser.add_argument('A', type=int)
parser.add_argument('B', type=int)

args = parser.parse_args()
print("Sum:         " + str(args.A + args.B))
print("Difference:  " + str(args.A - args.B))
print("Product:     " + str(args.A * args.B))
if args.B != 0:
    print("Quotient:    " + str(round(args.A / args.B, 4)))
    print("Remainder:   " + str(args.A % args.B))
else:
    print("Quotient:    ERROR(division by 0)")
    print("Remainder:   ERROR(modulo by 0)")
