# python numb3rs.py
import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    print(ip)
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9][0-9]?)$"
    if re.search(pattern,ip):
        return True
    else:
        
        return False


if __name__ == "__main__":
    main()


import re

def main():
    print(validate(input("IPv4 Address: ").strip))

def validate(addy):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", addy)
    if matches and (int(matches.group(1)) <= 255 and int(matches.group(2)) <= 255 and int(matches.group(3)) <= 255 and int(matches.group(4)) <= 255):
        return True
    else:
        return False

if __name__ == "__main__":
	main()