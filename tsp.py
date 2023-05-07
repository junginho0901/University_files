import random
import math

POPULATION_SIZE = 100
MUTATION_RATE = 0.05
GENERATIONS = 1000

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        distance = 0
        for i in range(len(self.genes)-1):
            city1 = self.genes[i]
            city2 = self.genes[i+1]
            distance += math.sqrt((city2[0]-city1[0])**2 + (city2[1]-city1[1])**2)
        return 1 / (distance + 0.001)

def generate_individual(cities):
    return Individual(random.sample(cities, len(cities)))

def generate_population(cities):
    return [generate_individual(cities) for _ in range(POPULATION_SIZE)]

def crossover(parent1, parent2):
    pivot = random.randint(0, len(parent1.genes)-1)
    child_genes = parent1.genes[:pivot] + [gene for gene in parent2.genes if gene not in parent1.genes[:pivot]]
    return Individual(child_genes)

def mutate(individual):
    if random.uniform(0, 1) <= MUTATION_RATE:
        index1, index2 = random.sample(range(len(individual.genes)), 2)
        individual.genes[index1], individual.genes[index2] = individual.genes[index2], individual.genes[index1]

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

def tsp(cities):
    population = generate_population(cities)
    for i in range(GENERATIONS):
        population = evolve(population)
        best_individual = get_best_individual(population)
        if i % 100 == 0:
            print(f"Generation {i}: Best Distance = {1/best_individual.fitness}")
    best_individual = get_best_individual(population)
    return best_individual.genes

cities = [(0,0), (1,3), (2,1), (3,4), (4,2)]
solution = tsp(cities)
print("Solution found:", solution)
