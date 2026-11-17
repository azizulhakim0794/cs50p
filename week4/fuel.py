def get_value():
    return input("Fraction: ")


def main():
    while True:
        nums = get_value().split("/")

        try:
            first_num = int(nums[0])
            sec_num = int(nums[1])

            if first_num >= 0 and sec_num > 0 and first_num <= sec_num:

                total = round((first_num / sec_num) * 100)

                if total >= 99:
                    print("F")
                elif total <= 1:
                    print("E")
                else:
                    print(f"{total}%")
                break

        except (ValueError, ZeroDivisionError, IndexError):
            continue


main()
