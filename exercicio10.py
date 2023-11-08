# QUESTÃO 10

celsius = input("Digite a temperatura em Celsius: ")

try:
    celsius = int(celsius)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

fahrenheit = (celsius * 1.8) + 32
print(f"A temperatura em Fahrenheit é {round(fahrenheit, 2)}°F")