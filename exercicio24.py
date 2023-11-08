# QUESTÃO 24

population_A = 80000
population_B = 200000
years = 0

while population_A <= population_B:
    population_A = population_A * (1 + (3 / 100))
    population_B = population_B * (1 + (1.5 / 100))
    years += 1

print(f" A população A com {population_A:,.0f} habitantes ultrapassou a população B com {population_B:,.0f} habitantes em {years} anos.")
