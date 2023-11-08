# QUESTÃO 28

first_number = input("Digite o primeiro número: ")
second_number = input("Digite o segundo número: ")
third_number = input("Digite o terceiro número: ")
fourth_number = input("Digite o quarto número: ")
fifth_number = input("Digite o quinto número: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    third_number = int(third_number)
    fourth_number = int(fourth_number)
    fifth_number = int(fifth_number)
except ValueError:
    print("Os valores digitados não são números válidos.")
    exit()

summation = first_number + second_number + third_number + fourth_number + fifth_number
average = summation / 5
print(f"A soma dos números é {summation} e a média é {average}")