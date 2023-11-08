# QUESTÃO 6

pi = 3.14
raio = input("Digite o valor do raio: ")

try:
    raio = int(raio)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

circle_area =  pi * (raio ** 2)
print(f"A área desse circulo é {circle_area}")