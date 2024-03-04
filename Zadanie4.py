def funkcja1():
    print("To jest funkcja 1")

def funkcja2(funkcja):
    print("Wywołuję funkcję przekazaną jako argument")
    funkcja()

funkcja2(funkcja1)
