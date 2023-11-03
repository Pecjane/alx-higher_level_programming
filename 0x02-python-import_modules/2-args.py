#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x_p = 1
    n_p = len(sys.argv)
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    else:
        if n_p == 2:
            print("{:d} argument:".format(n_p - 1))
        else:
            print("{:d} arguments:".format(n_p - 1))
        while x_p < n_p:
            print("{:d}: {}".format(x_p, sys.argv[x_p]))
            x_p += 1
