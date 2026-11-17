import emoji

text = input("Input: ")

full_sentance = ""

for word in text.split(" "):
    if word in [":earth_africa:", ":earth_americas:", ":earth_asia:"]:
        full_sentance += " 🌏"
        continue
    if word == ":thumbsup:":
        full_sentance += "👍"
        continue
    full_sentance += " " + word

print(emoji.emojize(f"Output {full_sentance}"))
