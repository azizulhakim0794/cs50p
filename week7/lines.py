# python3 lines.py
# inline sugges

import sys

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2 :
    print("Too many command-line arguments")
    sys.exit(1)

filename = sys.argv[1]

if filename[-3:-1]+filename[-1] != ".py":
    print("Not a Python file ")
    sys.exit(1)

try:
    count = 0
    with open(filename) as file:
        for line in file:
            line.strip()
            if line.strip() and not line.lstrip().startswith("#"):
                count+=1
    print(count)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

# print(filename[-3:-1]+filename[-1])

# for i in range(len(filename)):
