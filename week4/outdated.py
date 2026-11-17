months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
# month_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# day_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19,20,21, 22, 23, 24, 25, 26, 27, 28, 29,30, ]


# Here’s how to test your code manually:
# /1/0,',/./.'
# Run your program with python outdated.py. Type 9/8/1636 and press Enter.
# Your program should output:
# 1636-09-08
# Run your program with python outdated.py. Type September 8, 1636 and press Enter.
# Your program should output:
# 1636-09-08
# Run your program with python outdated.py. Type 23/6/1912 and press Enter.
# Your program should reprompt the user.
# Run your program with python outdated.py. Type December 80, 1980 and press Enter.
# Your program should reprompt the user.


# python outdated.py

# import re
# from datetime import datetime


# def get_dates():
#     return input("Date: ")


# month_index = [str(day) for day in range(1, 12)]
# day_index = [str(day) for day in range(1, 31)]

# data = []

# while True:
#     try:
#         # text = get_dates()
#         # data = re.split(r"[/ ,.']", text)
#         text = get_dates()
#         data = re.split(r"[/ ,.']", text)

#         month = ""
#         day = ""
#         year = ""

#         for i in range(len(data)):

#             if (data[i] in months and i == 0) or (data[i] in month_index and i == 0):

#                 if data[i] in months:
#                     month = str(months.index(data[i]) + 1)
#                 else:
#                     month = data[i]

#             elif i == 1 and data[i] in day_index:
#                 day = data[i]

#         year = data[len(data) - 1]

#         if year and month and day:

#             date = datetime(int(year), int(month), int(day))

#             formatted_date = date.strftime("%Y-%m-%d")

#             print(formatted_date)

#             break

#     except EOFError, KeyboardInterrupt:
#         continue


import re
from datetime import datetime


def get_dates():
    return input("Date: ")


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

month_index = [str(month) for month in range(1, 13)]
day_index = [str(day) for day in range(1, 32)]


while True:
    try:
        text = get_dates().strip()

        if "/" in text:
            data = text.split("/")

            if not all(item.isdigit() for item in data):
                continue

        elif "," in text:
            data = re.split(r"[ ,]+", text)

            if data[0] not in months:
                continue

        else:
            continue

        month = ""
        day = ""
        year = ""

        for i in range(len(data)):

            if i == 0 and (data[i] in months or data[i] in month_index):

                if data[i] in months:
                    month = str(months.index(data[i]) + 1)
                else:
                    month = data[i]

            elif i == 1 and data[i] in day_index:
                day = data[i]

        year = data[-1]

        if year and month and day:

            date = datetime(int(year), int(month), int(day))

            print(date.strftime("%Y-%m-%d"))
            break

    except (EOFError, KeyboardInterrupt, ValueError):
        break
