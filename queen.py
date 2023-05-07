import random

POPULATION_SIZE = 100
MUTATION_RATE = 0.05
GENERATIONS = 1000

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        attacks = 0
        for i in range(len(self.genes)):
            for j in range(i+1, len(self.genes)):
                if self.genes[i] == self.genes[j]:
                    attacks += 1
                elif abs(i-j) == abs(self.genes[i]-self.genes[j]):
                    attacks += 1
        return 1 / (attacks + 1)

def generate_individual():
    return Individual([random.randint(0, 7) for _ in range(8)])

def generate_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def crossover(parent1, parent2):
    pivot = random.randint(0, len(parent1.genes)-1)
    child_genes = parent1.genes[:pivot] + parent2.genes[pivot:]
    return Individual(child_genes)

def mutate(individual):
    if random.uniform(0, 1) <= MUTATION_RATE:
        gene_index = random.randint(0, len(individual.genes)-1)
        individual.genes[gene_index] = random.randint(0, 7)

def select_parent(population):
    fitness_sum = sum([individual.fitness for individual in population])
    rand_num = random.uniform(0, fitness_sum)
    partial_sum = 0
    for individual in population:
        partial_sum += individual.fitness
        if partial_sum >= rand_num:
            return individual

def evolve(population):
    new_population = []
    for _ in range(len(population)):
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    return new_population

def get_best_individual(population):
    return max(population, key=lambda individual: individual.fitness)

def solve():
    population = generate_population()
    for i in range(GENERATIONS):
        population = evolve(population)
        best_individual = get_best_individual(population)
        if best_individual.fitness == 1.0:
            return best_individual.genes
    return None

solution = solve()
if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
