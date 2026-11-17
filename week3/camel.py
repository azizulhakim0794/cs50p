# python camel.py

text = input("camelCase: ")

snack_case = ""
for i in range(len(text)):
    if text[i].isupper():
        snack_case += "_" + text[i].lower()
    else:
        snack_case += text[i]

print(f"snack_case: {snack_case}")
