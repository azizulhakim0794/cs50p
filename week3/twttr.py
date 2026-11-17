# python twttr.py

text = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]

output = ""

for i in range(len(text)):
    if text[i].lower() not in vowels:
        output += text[i]

print(f"Output: {output}")
