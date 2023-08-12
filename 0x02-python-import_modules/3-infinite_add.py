#!/usr/bin/python3
from sys import argv
args = 0


if __name__ == "__main__":
    for i in range(1, len(argv)):
        args += int(argv[i]);
    print(args)
