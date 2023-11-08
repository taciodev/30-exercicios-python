# QUESTÃO 19

first_number = input("Digite o primeiro número: ")
second_number = input("Digite o segundo número: ")
third_number = input("Digite o terceiro número: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    third_number = int(third_number)
except ValueError:
    print("Os valores digitados não são números válidos.")
    exit()

first_is_bigger = first_number > second_number > third_number
first_is_bigger_other = first_number > third_number > second_number
second_is_bigger = second_number > first_number > third_number
second_is_bigger_other = second_number > third_number > first_number
third_is_bigger = third_number > first_number > second_number
third_is_bigger_other = third_number > second_number > first_number

if first_is_bigger:
    print(f"{first_number} > {second_number} > {third_number}")
elif first_is_bigger_other:
    print(f"{first_number} > {third_number} > {second_number}")
elif second_is_bigger:
    print(f"{second_number} > {first_number} > {third_number}")
elif second_is_bigger_other:
    print(f"{second_number} > {third_number} > {first_number}")
elif third_is_bigger:
    print(f"{third_number} > {first_number} > {second_number}")
elif third_is_bigger_other:
    print(f"{third_number} > {second_number} > {first_number}")
else:
    print("Os números são iguais.")
