# python fuel.py
def main():
    while True:
        try:
            fraction = input("Fraction: ").split("/")

            first_num = convert(fraction[0])
            second_num = convert(fraction[1])

            if first_num > second_num:
                continue

            total = round((first_num / second_num) * 100)

            print(gauge(total))
            break

        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    if fraction in "0123456789":
        return fraction


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()
