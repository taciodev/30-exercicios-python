# QUESTÃO 23

def get_name():
    while True:
        name = input("NOME: ")
        if name.strip():
            return name
        else:
            print("Nome não pode estar em branco.")

def get_age():
    while True:
        age = input("IDADE: ")
        if age.isdigit():
            age = int(age)
            if age >= 0 and age <= 150: 
                return age
            else:
                print("Idade deve estar entre 0 e 120.")
        else:
            print("Idade deve ser um número inteiro válido.")

def get_salary():
    while True:
        salary = input("SALÁRIO: ")
        try:
            salary = float(salary)
            if salary >= 0:
                return salary
            else:
                print("Salário deve ser um valor não negativo.")
        except ValueError:
            print("Salário deve ser um número válido.")

def get_sex():
    while True:
        sex = input("SEXO(M/F): ").strip().lower()
        if sex in ("m", "f"):
            return sex
        else:
            print("Sexo deve ser 'M' ou 'F'.")

def get_marital_status():
    while True:
        marital_status = input("ESTADO CIVIL(S/C/V/D): ").strip().lower()
        if marital_status in ("s", "c", "v", "d"):
            return marital_status
        else:
            print("Estado civil deve ser 'S', 'C', 'V' ou 'D'.")

name = get_name()
age = get_age()
salary = get_salary()
sex = get_sex()
marital_status = get_marital_status()

print(
    f"NOME: {name}",
    f"IDADE: {age}",
    f"SALÁRIO: {salary}",
    f"SEXO: {sex}",
    f"ESTADO CIVIL: {marital_status}",
    sep="\n"
)