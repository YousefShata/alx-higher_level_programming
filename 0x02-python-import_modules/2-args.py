#!/usr/bin/python3
from sys import argv
args = len(argv) - 1
def print_args():
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))


if __name__ == "__main__":
    if (args == 0):
        print("{:d} arguments.".format(args))
    elif (args == 1):
        print("{:d} argument:".format(args))
        print_args()
    else:
        print("{:d} arguments:".format(args))
        print_args()
