# QUESTÃO 8

hourly_wage = input("Quanto você ganha por hora: ")
hours_worked_in_the_month = input("Quanto tempo você trabalha no mês: ")

try:
    hourly_wage = int(hourly_wage)
    hours_worked_in_the_month = int(hours_worked_in_the_month)
except ValueError:
    print("Os valores digitados não são números inteiros válidos.")
    exit()

salary =  hourly_wage * hours_worked_in_the_month
print(f"O seu salário no final do mês é {salary}")