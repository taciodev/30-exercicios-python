# QUESTÃO 15

note1 = input("Digite a primeira nota: ")
note2 = input("Digite a segunda nota: ")

try:
    note1 = int(note1)
    note2 = int(note2)
except ValueError:
    print("Os valores digitados não são números válidos.")
    exit()

average = (note1 + note2) / 2

if average == 10:
    print(f"A média das notas é {average}, você foi aprovado com distinção!")
elif average >= 7:
    print(f"A média das notas é {average}, você foi aprovado!")
elif average < 7:
    print(f"A média das notas é {average}, você foi reprovado!")

