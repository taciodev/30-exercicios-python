# QUESTÃO 17

first_number = input("Digite o primeiro número: ")
second_number = input("Digite o segundo número: ")
third_number = input("Digite o terceiro número: ")

first_is_bigger = first_number > second_number and first_number > third_number
second_is_bigger = second_number > first_number and second_number > third_number

first_is_smaller = first_number < second_number and first_number < third_number
second_is_smaller = second_number < first_number and second_number < third_number

if first_is_bigger:
    print(f"O número {first_number} é maior que o número {second_number} e {third_number}")
elif second_is_bigger:
    print(f"O número {second_number} é maior que o número {first_number} e {third_number}")
else:
    print(f"O número {third_number} é maior que o número {first_number} e {second_number}")

if first_is_smaller:
    print(f"O número {first_number} é menor que o número {second_number} e {third_number}")
elif second_is_smaller:
    print(f"O número {second_number} é menor que o número {first_number} e {third_number}")
else:
    print(f"O número {third_number} é menor que o número {first_number} e {second_number}")