import random

POPULATION_SIZE = 4
MUTATION_RATE = 0.1
SIZE = 5

# 염색체를 클래스로 정의
class Chromosome :
    def __init__(self,g=[]):
        self.genes = g.copy() # 유전자는 리스트로 구현
        self.fitness = 0 # 적합도
        if self.genes.__len__() == 0 : # 염색체가 초기 상태이면 초기화
            i = 0
            while i < SIZE:
                if random.random() >= 0.5 : self.genes.append(1)
                else: self.genes.append(0)
                i+=1

    def cal_fitness(self): 
        self.fitness = 0
        value = 0
        for i in range(SIZE): # 이진수 계산
            value += self.genes[i]*pow(2,SIZE-1-i)
        self.fitness = value
        return self.fitness
    
    def __str__(self): # 객체를 문자열로 변환하여 반환
        return self.genes.__str__()
    
# 염색체와 적합도를 출력
def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #",i,"=",x,"적합도", x.cal_fitness())
        i+=1
    print("")

# 선택 연산
def select(pop):
    max_value = sum([c.cal_fitness() for c in population]) 
    pick = random.uniform(0,max_value)
    current = 0

    # 룰렛 휠에서 어떤 조작에 속하는지 알아내는 루프
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c
        
# 교차 연산
def crossover(pop):
    father = select(pop)
    mother = select(pop)
    index = random.randint(1,SIZE-1) # 1 부터 SIZE -1 사이의 정수 랜덤 반환
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + father.genes[index:]
    return (child1,child2)

# 돌연변이 연산
def mutate(c):
    for i in range(SIZE): # i += 1
        if random.random() < MUTATION_RATE: # random.random() 0.0 ~ 1.0 사이의 float형 랜덤 반환
            if random.random() < 0.5:
                c.genes[i] = 1
            else:
                c.genes[i] = 0

# 메인 프로그램
population = []
i = 0

# 초기 염색체를 생성하여 객체 집단에 추가

while i < POPULATION_SIZE: # population 리스트에 염색체 추가
   population.append(Chromosome())
   i+=1

count = 0
population.sort(key=lambda x: x.cal_fitness(), reverse=True) # reserve = True : 내림차순
print("세대 번호 = ",count)
print_p(population)
count = 1

while population[0].cal_fitness() < 31: # 범위 : 0~31 == 적합도가 31이 되면 반복 종료
    new_pop = []

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2): # // : 몫 연산자
        c1,c2 = crossover(population);
        new_pop.append(Chromosome(c1));
        new_pop.append(Chromosome(c2));

    # 자식 세대가 부모 세대를 대체
    # 깊은 복사 수행
    population = new_pop.copy()

    # 돌연변이 연산
    for c in population : mutate(c)

    # 출력을 위한 정렬 
    population.sort(key=lambda x: x.cal_fitness(),reverse=True) # reserve = True : 내림차순
    print("세대 번호 = ",count)
    print_p(population)
    count+=1
    if count > 100 : break;
