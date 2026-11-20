# python names.py

# write the files
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# read the files
studnets = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(name)

# with open("names.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         studnet = {"name": name, "home": home}
#         studnets.append(studnet)
# // CSV reader
# import csv

# with open("names.csv") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         studnets.append({"name": row["name"], "location": row["location"]})

#     # for line in file:
#     #     name, home = line.rstrip().split(",")
#     #     studnet = {"name": name, "home": home}
#     #     studnets.append(studnet)

# for stduent in sorted(studnets, key=lambda stduent: stduent["name"]):
#     print(stduent["name"])

# print(studnets)

# // CSV writer 01601957882
import csv

name = input("what's your name: ")
location = input("what's your location: ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "location"])
    writer.writerow({"name": name, "location": location})
