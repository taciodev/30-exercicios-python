# QUESTÃO 18

first_product = input("Digite o valor do primeiro produto: R$ ")
second_product = input("Digite o valor do segundo produto: R$ ")
third_product = input("Digite o valor do terceiro produto: R$ ")

try:
    first_product = float(first_product)
    second_product = float(second_product)
    third_product = float(third_product)
except ValueError:
    print("Os valores digitados não são números válidos.")
    exit()

first_is_smaller = first_product < second_product and first_product < third_product
second_is_smaller = second_product < first_product and second_product < third_product

if first_is_smaller:
    print(f"O primeiro produto no valor de R$ {first_product:,.2f} é o mais barato")
elif second_is_smaller:
    print(f"O segundo produto no valor de R$ {second_product:,.2f} é o mais barato")
else:
    print(f"O terceiro produto no valor de R$ {third_product:,.2f} é o mais barato")