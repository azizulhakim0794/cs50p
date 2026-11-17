text = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

if text.lower() == "forty two" or text == "forty-two" or "42" in text:
    print("Yes")


elif text.lower() == "fifty" or (len(text) == 2 and int(text) == 50):
    print("No")
