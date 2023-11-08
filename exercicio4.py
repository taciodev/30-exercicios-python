# QUESTÃO 4

note1 = input("Digite a primeira nota: ")
note2 = input("Digite a segunda nota: ")
note3 = input("Digite a terceira nota: ")
note4 = input("Digite a quarta nota: ")

try:
    note1, note2, note3, note4 = int(note1), int(note2), int(note3), int(note4)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

average = (note1 + note2 + note3 + note4) / 4
print(f"A média é {average}")