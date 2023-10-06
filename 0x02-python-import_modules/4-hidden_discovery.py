#!/usr/bin/python3

import hidden_4


def main():
    hidden_funcs = dir(hidden_4)

    for each in sorted(hidden_funcs):
        if each[:2] != "__":
            print(each)


if __name__ == "__main__":
    main()
