# QUESTÃO 27

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

first_is_bigger = first_number > second_number and first_number > third_number and first_number > fourth_number and first_number > fifth_number
second_is_bigger = second_number > first_number and second_number > third_number and second_number > fourth_number and second_number > fifth_number
third_is_bigger = third_number > first_number and third_number > second_number and third_number > fourth_number and third_number > fifth_number
fourth_is_bigger = fourth_number > first_number and fourth_number > second_number and fourth_number > third_number and fourth_number > fifth_number

if first_is_bigger:
    print(f"O número {first_number} é maior que o número {second_number}, {third_number}, {fourth_number} e {fifth_number}")
elif second_is_bigger:
    print(f"O número {second_number} é maior que o número {first_number}, {third_number}, {fourth_number} e {fifth_number}")
elif third_is_bigger:
    print(f"O número {third_number} é maior que o número {first_number}, {second_number}, {fourth_number} e {fifth_number}")
elif fourth_is_bigger:
    print(f"O número {fourth_number} é maior que o número {first_number}, {second_number}, {third_number} e {fifth_number}")
else:
    print(f"O número {fifth_number} é maior que o número {first_number}, {second_number}, {third_number} e {fourth_number}")