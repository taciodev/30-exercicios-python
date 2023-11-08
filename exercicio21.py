# QUESTÃO 21

while True:
    note = input("Digite uma nota entre 0 e 10: ")
    is_note_valid = None
    is_between_zero_and_ten = new_note >= 0 and new_note <= 10

    try:
        new_note = int(note)
        is_note_valid = True
    except:
        is_note_valid = False

    if is_note_valid and is_between_zero_and_ten:
        print("Número válido")
        break
    else:
        print("Número inválido")