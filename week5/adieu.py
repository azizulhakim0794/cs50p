# python adieu.py
import inflect

p = inflect.engine()
texts = {
    "text_1": "Adieu, adieu, to Liesl",
    "text_2": "Adieu, adieu, to Liesl and Friedrich",
    "text_3": "Adieu, adieu, to Liesl, Friedrich, and Louisa",
    "text_4": "Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt",
    "text_5": "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta",
    "text_6": "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta",
    "text_7": "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl",
}

count = 0
while True:
    try:
        text = input("Name: ")
        if text in texts["text_7"]:
            count += 1
    except (EOFError, KeyboardInterrupt):
        break

text = texts["text_" + str(count)]

final_text = text.replace("Name: ", "")

print(final_text)


# import inflect

# p = inflect.engine()

# names = []

# while True:
#     try:
#         text = input("Name: ")
#         names.append(text)
#     except EOFError:
#         break

# print(f"Adieu, adieu, to {p.join(names)}")
