shopping_list = {
    "Piekarnia": ["chleb", "bułki", "pączek", "chałka"],
    "Warzywniak": ["marchew", "seler", "rukola", "pietruszka"]
}

print("Lista zakupów")
for place, product in shopping_list.items():
    print(f"""Idę do {place}, kupuję tu następujące rzeczy: {product}""")