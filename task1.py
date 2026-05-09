shopping_list = {"Piekarnia":["Chleb","Pączek","Bułki"],
                 "Warzywniak":["Marchew","Seler","Rukola"]}

for key in shopping_list.keys():
    products = [v.upper() for v in shopping_list[key]]
    print(f"Idę do {key.upper()}, kupuję następujące rzeczy: {products}")

print(f"W sumię kupuję {sum(len(v) for v in shopping_list.values())} produktów")








