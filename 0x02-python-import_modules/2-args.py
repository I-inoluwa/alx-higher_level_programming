#!/usr/bin/python3

def main():
    from sys import argv
    
    length = len(argv)
    ends = ":\n"
    if (length - 1) == 1:
        print("{:d} argument".format(length - 1), end=ends)
    else:
        if (length - 1) == 0:
            ends = ".\n"
        print("{:d} arguments".format(length - 1), end=ends)
    
    for i in range(1, length):
        print("{:d}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
