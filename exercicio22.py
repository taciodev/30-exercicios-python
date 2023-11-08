# QUESTÃO 22

while True:
    user = input("DIGITE O USUÁRIO: ").lower()
    password = input("DIGITE A SENHA: ").lower()

    if user != password:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print(
            "O usuário e a senha não podem ser iguais!",
            "Digite novamente as informações"
        )