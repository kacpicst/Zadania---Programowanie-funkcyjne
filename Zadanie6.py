lista_slow = ["ananas", "banan", "arbuz", "limonka", "awokado"]

slowa_zaczynajace_na_a = list(filter(lambda x: x.startswith("a"), lista_slow))

print("Słowa zaczynające się na literę 'a':", slowa_zaczynajace_na_a)

lista_liczb = [1, 2, 3, 4, 5]

kwadraty_liczb = list(map(lambda x: x**2, lista_liczb))

print("Kwadraty liczb:", kwadraty_liczb)
