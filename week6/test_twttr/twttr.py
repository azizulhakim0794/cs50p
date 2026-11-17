# python twttr.py


# (A, E, I, O, and U)
def main():
    text = input("Input: ")

    print(shorten(text))


def shorten(word):
    with_out_vouwle = ""

    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            with_out_vouwle += char
    return with_out_vouwle


if __name__ == "__main__":
    main()
