# python3 scourgify.py students.csv ans.csv
import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3 :
    print("Too many command-line arguments")
    sys.exit(1)

read_file = sys.argv[1]
write_file = sys.argv[2]


if not read_file.endswith(".csv") or not write_file.endswith(".csv"):
    print("Not a CSV file ")
    sys.exit(1)

students = []

try:

    # read and copything in the naming formate 
    with open(read_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            names = row["name"].split(" ")
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house":row["house"]})

    # write the file 
    with open(write_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)