def main():
    text = input("Greeting: ").lower()
    print(value(text))


def value(greeting):
    if greeting == "Hello" or greeting == "Hello, Newman":
        return 100
    if greeting in ["Hey", "How you doing?", "How's it going"]:
        return 20
    if greeting in ["What's happening?", "What's up? "]:
        return 0


if __name__ == "__main__":
    main()
