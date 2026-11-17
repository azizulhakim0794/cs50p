# python bitcoin.py
import requests
import sys

bit_count = 0
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument ")

try:
    if sys.argv[1]:
        bit_count = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")

# print(bit_count)

try:

    if bit_count > 0:
        req = requests.request(
            "GET",
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=996fb1f4885a0e25d24a76ad353ec6eddf1cb4400bfa2602b95e49022c2fde62",
        )
        data = req.json()["data"]

        amount = bit_count * float(data["priceUsd"])
        # print("{:,.4f}".format(12345.123459))
        print(f"${amount:,.4f}")

except requests.RequestException:
    pass


# print("{:,.4f}".format(12345.123459))
# print(f"${amount:,.4f}")
