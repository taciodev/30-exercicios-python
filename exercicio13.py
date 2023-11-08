# QUESTÃO 13

letter = input("Digite F ou M para o seu sexo: ").upper()

if letter == "M":
    print(f"Sexo masculino")
elif letter == "F":
    print(f"Sexo feminino")
else:
    print(f"Sexo inválido")