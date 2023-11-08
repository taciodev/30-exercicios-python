# QUESTÃO 25

def calculate_growth_rate(smaller_population, smaller_population_rate, larger_population, larger_population_rate):
    years = 0
    while smaller_population <= larger_population:
        smaller_population = smaller_population * (1 + (smaller_population_rate / 100))
        larger_population = larger_population * (1 + (larger_population_rate / 100))
        years += 1
    
    return years

population_A = input("Digite a população A: ")
population_growth_A = input("Digite a taxa de crescimento da população A: ")
population_B = input("Digite a população B: ")
population_growth_B = input("Digite a taxa de crescimento da população B: ")

try:
    population_A = float(population_A)
    population_B = float(population_B)
    population_growth_A = float(population_growth_A)
    population_growth_B = float(population_growth_B)
except ValueError:
    print("Os valores digitados não são números válidos.")
    exit()

if population_A < population_B:
    years = calculate_growth_rate(population_A, population_growth_A, population_B, population_growth_B)
    print(f"A população A com {population_A:,.0f} habitantes ultrapassará a população B com {population_B:,.0f} habitantes em {years} anos.")
else:
    years = calculate_growth_rate(population_B, population_growth_B, population_A, population_growth_A)
    print(f"A população B com {population_B:,.0f} habitantes ultrapassará a população A com {population_A:,.0f} habitantes em {years} anos.")
