# QUESTÃO 20

study_shift = input("Qual o turno em que você estuda (M-matutino/V-Vespertino/N-Noturno): ").upper()

if study_shift == "M":
    print("Bom dia!")
elif study_shift == "V":
    print("Boa tarde!")
else:
    print("Boa noite!")