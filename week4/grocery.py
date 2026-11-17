# python grocery.py


def get_value():
    return input("").upper()


total = 0

items = {}

while True:
    try:
        text = get_value()
        items[text] = items.get(text, 0) + 1

    except EOFError, KeyboardInterrupt:
        for text in sorted(items):
            print(f"{items[text]} {text}")
        break
