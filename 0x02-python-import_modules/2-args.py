#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    elif length > 1:
        print("{} arguments:".format(length))

    lists = (argv)
    if length >= 1:
        length = 0
        for lit in lists:
             if length != 0:
                 print("{}: {}".format(length, lit))
            length += 1
