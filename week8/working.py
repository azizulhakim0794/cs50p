# python3 working.py

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)


    if pattern:
        time_parts = list(pattern.groups())

        for i in range(len(time_parts)):
            if (i == 1 or i == 4) and time_parts[i] == None:
                time_parts[i] = 0
            if ((i == 0 or i == 3) and int(time_parts[i]) > 12) or ((i == 1 or i == 4) and int(time_parts[i]) > 59):
                raise ValueError
            

        left_Full_time = hour_clock(time_parts[0], time_parts[1], time_parts[2])
        right_Full_time = hour_clock(time_parts[3], time_parts[4], time_parts[5])

        return f"{left_Full_time} to {right_Full_time}"
    else:
        raise ValueError


def hour_clock (hour, minute, indicators):
    if indicators == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour =  int(hour)
    
    return f"{new_hour:02}:{minute:02}"

if __name__ == "__main__":
    main()