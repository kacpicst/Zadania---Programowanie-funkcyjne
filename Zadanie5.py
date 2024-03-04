def liczby_parzyste(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

pole_prostokata = lambda a, b: a * b

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wynik = liczby_parzyste(lista_liczb)
print("Liczby parzyste z listy:", wynik)

dlugosc_boku_a = 5
dlugosc_boku_b = 10
print("Pole prostokąta:", pole_prostokata(dlugosc_boku_a, dlugosc_boku_b))
