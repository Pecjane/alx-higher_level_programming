#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for p in dir(hidden_4):
        if p[0] == "_":
            continue
        print(p)
