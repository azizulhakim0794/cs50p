# python coke.py

total = 50


while total:
    print(f"Amount Due {total}")
    if total != 0:
        money = int(input("Insert Coin: "))

    if money <= 25:
        total = total - money

    if total <= 0:
        print(f"Change Owed: {abs(total)}")
        break


total = 50

while total > 0:
    print(f"Amount Due: {total}")
    money = int(input("Insert Coin: "))

    if money == 25 or money == 10 or money == 5:
        total = total - money

print(f"Change Owed: {abs(total)}")
