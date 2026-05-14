shopping_list = {"piekarnia":["chleb","pączek","bułki"],
                 "warzywniak":["marchew","seler","rukola"]}

for key in shopping_list.keys():
    products = [v.capitalize() for v in shopping_list[key]]
    print(f"Idę do {key.capitalize()}, kupuję następujące rzeczy: {products}")

print(f"W sumię kupuję {sum(len(v) for v in shopping_list.values())} produktów")








