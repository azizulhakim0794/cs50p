def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


print(".".isalnum())


def is_valid(s: str):

    digits = "0123456789"

    for i in range(len(s) - 1):
        if s[i] in digits:
            if s[i] == "0" and (i == 2 or s[i - 1].isalpha()):
                return False

            for j in range(i, len(s)):
                if not s[j] in digits:
                    return False

            break

    if len(s) > 2 and len(s) <= 6:
        return True


main()
