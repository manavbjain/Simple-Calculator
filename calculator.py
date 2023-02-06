#!/usr/bin/python3

# importing argparse for parsing command line input
import argparse

# parsing command line inputs/arguments
parser = argparse.ArgumentParser(description="A Simple Command Line Calculator",
                                usage="./calculator.py [Operation] [Value1] [Value2]")

parser.add_argument("-a", "--add", help="adds the two inputs", action="store_true")
parser.add_argument("-s", "--subtract", help="subtracts the first input from the second input", action="store_true")
parser.add_argument("-m", "--multiply", help="multiplies the two inputs", action="store_true")
parser.add_argument("-d", "--divide", help="divides the second input by the first input", action="store_true")
parser.add_argument("-e", "--exponent", help="first input (base) raised to the second input (exponent)", action="store_true")
parser.add_argument("-sqrt", "--squareroot", help="squareroot of the input", action="store_true")
parser.add_argument("-cbrt", "--cuberoot", help="cuberoot of the input", action="store_true")
parser.add_argument("-fact", "--factorial", help="factorial of the input", action="store_true")
parser.add_argument("-comb", "--combinations", help="nCr where n is the first input and r in the second input", action="store_true")
parser.add_argument("-perm", "--permutations", help="nPr where n is the first input and r in the second input", action="store_true")


parser.add_argument("Value1", help="The first value", type=int)
parser.add_argument("Value2", nargs='?', help="The second value", type=int)

args = parser.parse_args()

# adding the inputs
def add (a, b):
    return (a + b)

# subtracting the inputs
def subtract (a, b):
    return (a - b)

# multiplying the inputs
def multiply (a, b):
    return (a * b)

# dividing the inputs
def divide (a, b):
    return (a // b)

# power = a^b
def exponent (a, b):
    return (a ** b)

# squareroot of the input
def squareroot (a):
    return (a ** (1/2))

# cuberoot of the input
def cuberoot (a):
    return (a ** (1/3))

# factorial of the input
def factorial(a):
    if a == 0 or a == 1:
        return (1)
    else:
        fact = 1
        while (a > 1):
            fact *= a
            a -= 1
        return (fact)

# combinations nCr
def combinations(a, b):
    if b < a:
        return (factorial(a) / (factorial(b) * factorial(a - b)))
    elif a == b:
        return (1)
    else:
        return("the second value has to be less than or equal to the first value")

# permutations nPr
def permutations (a,b):
    if b < a:
        return (factorial(a) / factorial(a - b))
    elif a == b:
        return (1)
    else:
        return("the second value has to be less than or equal to the first value")

# main function
def main (a, b):
    if args.add:
        print(add (args.Value1,args.Value2))
    elif args.subtract:
        print(subtract (args.Value1,args.Value2))
    elif args.multiply:
        print(multiply (args.Value1,args.Value2))
    elif args.divide:
        print(divide (args.Value1, args.Value2))
    elif args.exponent:
        print(exponent (args.Value1, args.Value2))
    elif args.squareroot:
        print(squareroot(args.Value1))
    elif args.cuberoot:
        print(cuberoot(args.Value1))
    elif args.factorial:
        print(factorial(args.Value1))
    elif args.combinations:
        print(combinations(args.Value1, args.Value2))
    elif args.permutations:
        print(permutations(args.Value1, args.Value2))

# calling the main function
if __name__ == "__main__":
    main(args.Value1, args.Value2)
