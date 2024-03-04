def square_number(x):
    return x ** 2

def add_five(x):
    return x + 5

def compose_functions(*functions):
    def composed(result):
        for func in functions:
            result = func(result)
        return result
    return composed

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    composed_function = compose_functions(square_number, add_five)
    result = composed_function(num)
    print(f"Dla liczby {num}, wynik po zastosowaniu funkcji to:", result)
