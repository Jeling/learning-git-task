import os
clear = lambda: os.system('cls')
clear()

shopping_list = {
    "Piekarnia": ["chleb", "bułki", "pączek", "chałka"],
    "Warzywniak": ["marchew", "seler", "rukola", "pietruszka"]
}

counter = 0
print("Lista zakupów")
for place, product in shopping_list.items():
    print(f"""Idę do {place}, kupuję tu następujące rzeczy: {product}""")
    counter += len(product)
print(f"""W sumie kupuję {counter} produktów
""")