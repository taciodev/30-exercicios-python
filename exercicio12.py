# QUESTÃO 12

value = input("Digite um número: ")

try:
    value = int(value)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

if value >= 0:
    print(f"O número {value} é positivo")
else:
    print(f"O número {value} é negativo")

