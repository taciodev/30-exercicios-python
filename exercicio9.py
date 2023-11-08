# QUESTÃO 9

fahrenheit = input("Digite a temperatura em Fahrenheit: ")

try:
    fahrenheit = int(fahrenheit)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

celsius = 5 * ((fahrenheit - 32) / 9)
print(f"A temperatura em Celsius é {round(celsius, 2)}°C")