from functools import reduce

numbers = [3, 7, 2, 8, 5, 12, 9, 4, 3, 6, 8]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Największa liczba w liście:", max_number)

def calculate_average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers) if numbers else 0

numbers = [1, 2, 3, 4, 5, 9, 6, 7, 5, 3, 2]
average = calculate_average(numbers)
print("Średnia z listy liczb:", average)
