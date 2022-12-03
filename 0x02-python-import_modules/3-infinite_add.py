#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number = (argv)
    ans = 0

    for num in number:
        if num != number[0]:
            ans += int(num)
    print(ans)
