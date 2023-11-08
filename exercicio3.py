# QUESTÃO 3

first_number = input("Digite o primeiro número: ")
second_number = input("Digite o segundo número: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

result = first_number + second_number
print(f"A soma é {result}")