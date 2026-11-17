# python nutrition.py
fruits = [
    {"name": "Apple", "calories": 130},
    {"name": "Avocado", "calories": 50},
    {"name": "Banana", "calories": 110},
    {"name": "Cantaloupe", "calories": 50},
    {"name": "Sweet Cherries", "calories": 100},
    {"name": "strawberries", "calories": 50},
]

text = input("Item: ")

for fruit in fruits:
    if fruit["name"] == text:
        print(f"Calories: {fruit["calories"]}")
