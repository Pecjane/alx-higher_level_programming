#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    p = 1
    while p < len(sys.argv):
        sum += int(sys.argv[p])
        p += 1
    print(sum)
