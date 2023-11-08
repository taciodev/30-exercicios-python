# QUESTÃO 26

sense = input("QUAL O SENTIDO EM QUE DESEJA IMPRIMIR OS NÚMEROS(V/H): ").upper() or "V"
end_operator = "\n"

if sense == "H":
    end_operator = " "

for num in range(1, 21):
    print(num, end=end_operator)