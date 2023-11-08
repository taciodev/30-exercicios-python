# QUESTÃO 5

metros = input("Digite um valor em metros: ")

try:
    metros = int(metros)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

centimetros = metros * 100
print(f"{metros}m em centímetros é {centimetros}cm")