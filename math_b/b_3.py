import numpy as np
import math

# 参数定义
D_center = 110 # 中心深度
alpha = math.radians(1.5)   # 坡度角度
theta = math.radians(120.0)     #换能器开角
width = 4 * 1852    # 东西 宽度 (单位 : m)
d_min = 2 * D_center * math.tan(theta/2) * 0.10 # 基于10%重叠率的两条线之间的最小距离
d_max = 2 * D_center * math.tan(theta/2) * 0.20 # 基于20%重叠率的两条线之间的最大距离

# 遗传算法参数 :
population_size = 100
num_generations = 120
elite_size = int(0.1 * population_size)
num_crossover_points = 2

# 适应度函数
def fitness(chromosome):
    coverage = 0
    last_line = 0
    for line in chromosome:
        coverage_width = 2 * (D_center + (line - width/2) * math.tan(alpha)) * math.tan(theta / 2)
        overlap = coverage_width - (line - last_line)
        if overlap < d_min or overlap > d_max :
            return 0    # 无效的解
        coverage += coverage_width
        last_line = line
    return coverage

# 多点交叉函数
def crossover(parent1,parent2) :
    points = sorted(np.random.choice(range(1,len(parent1)), num_crossover_points, replace=False))
    child1 , child2 = parent1.copy() , parent2.copy()
    for i in range(len(points) + 1) :
        start = points[i-1] if i != 0 else 0
        end = points[i] if i < len(points) else len(parent1)
        if i%2==0 :
            child1[start:end],child2[start:end] = parent2[start:end], parent1[start:end]
    return child1 , child2

# 自适应变异函数
def adaptive_mutation(chromosome, fitness_value , fitness_values):
    if fitness_value < np.mean(fitness_values):
        mutation_rate = 0.3 # 为适应度较低的染色体增加变异率
    else:
        mutation_rate = 0.1 # 为适应度较低的染色体增加变异率

    if np.random.rand() < mutation_rate:
        mutation_point = np.random.randint(len(chromosome))
        chromosome[mutation_point] += np.random.uniform(-d_min/10,d_min/10)

# 增强版遗传算法
def enhanced_genetic_algorithm():
    # 初始化种群
    population = np.random.uniform(low=d_min, high=d_max, size=(population_size,int(width/d_min)))

    # 遗传算法主循环
    for generation in range(num_generations):
        # 评估适应度
        fitness_values = [fitness(chromo) for chromo in population]

        # 精英策略 , 选择最佳的染色体
        elite_indices = np.argsort(fitness_values)[-elite_size:]
        new_population = [population[i] for i in elite_indices]

        # 交叉和变异
        while len(new_population) < population_size :
            #选择父代
            parents = np.argsort(fitness_values)[-2:]

            # 交叉
            child1,child2 = crossover(population[parents[0]], population[parents[1]])
            new_population.extend([child1,child2])

            # 自适应变异
            for chromo in new_population[-2:]:
                adaptive_mutation(chromo, fitness(chromo), fitness_values)

        population = np.array(new_population)
    return population[np.argmax([fitness(chromo) for chromo in population])]

best_solution_with_comments = enhanced_genetic_algorithm()
best_solution_with_comments






