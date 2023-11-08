# QUESTÃO 7

base = input("Digite a base do quadrado: ")
height = input("Digite a altura do quadrado: ")

try:
    base = int(base)
    height = int(height)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

square_area = base * height
print(f"A área desse quadrado é {square_area}, e seu dobro é {square_area * 2}")