# python plates.py


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Must contain 2 to 6 characters
    # if len(s) < 2 or len(s) > 6:
    #     return False

    # Rule 2: Must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Rule 3: Numbers must be at the end
    # Rule 4: First number cannot be 0
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            return False

    # Rule 5: Only letters and numbers are allowed
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
