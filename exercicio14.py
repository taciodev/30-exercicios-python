# QUESTÃO 14

letter = input("Digite uma letra: ").upper()

if letter in ("A", "E", "I", "O", "U"):
    print(f"A letra {letter} é uma vogal")
else:
    print(f"A letra {letter} é uma consoante")