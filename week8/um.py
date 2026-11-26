# python3 um.py
# hello, no, world
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = re.findall( r"\bno\b",s, re.IGNORECASE)
    return len(pattern)


if __name__ == "__main__":
    main()