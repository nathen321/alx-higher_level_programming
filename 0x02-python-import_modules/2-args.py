#!/usr/bin/python3
import sys

lise = sys.argv
siz = len(lise) - 1

if __name__ == "__main__":
    if siz == 0:
        print("{:d} arguments.".format(siz))
    elif siz > 1:
        print("{:d} arguments:".format(siz))
        for i in range(1, siz + 1):
            print("{:d}: {}".format(i, lise[i]))
    elif siz == 1:
        print("{:d} argument:".format(siz))
        for i in range(1, siz + 1):
            print("{:d}: {}".format(i, lise[i]))
