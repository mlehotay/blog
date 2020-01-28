Title: Solving the Knapsack Problem with a Genetic Algorithim
Date: 2020-01-26 22:43
Modified: 2020-01-28 03:34
Category: Data Science
Tags: genetic-algorithm, combinatorics, computational-complexity
Slug: knapsack
Status: published

Here's the code. I'll write the description in a day or two. I still need to add weapons and armor to the treasure chest and update the fitness calculations to include the probability defeating the troll.

### Treasure


```python
import random
import arena # https://github.com/mlehotay/arena.git
```


```python
NUM_ITEMS = 20 # number of items in treasure chest
MAX_WEIGHT = 100 # max weight of a single treasure item
MAX_VALUE = 100 # max value of a single treasure item
```


```python
treasure_names = ['gold', 'gem', 'ring', 'amulet', 'potion', 'scroll', 'wand', 'spellbook']
treasure = [{
        'description': random.choice(treasure_names),
        'weight': random.randint(1, MAX_WEIGHT),
        'value': random.randint(1, MAX_VALUE)
    } for _ in range(0, NUM_ITEMS)
]
```


```python
treasure
```




    [{'description': 'scroll', 'weight': 17, 'value': 89},
     {'description': 'ring', 'weight': 44, 'value': 75},
     {'description': 'gold', 'weight': 92, 'value': 98},
     {'description': 'scroll', 'weight': 100, 'value': 20},
     {'description': 'spellbook', 'weight': 56, 'value': 93},
     {'description': 'ring', 'weight': 26, 'value': 75},
     {'description': 'potion', 'weight': 47, 'value': 98},
     {'description': 'potion', 'weight': 30, 'value': 62},
     {'description': 'gem', 'weight': 16, 'value': 7},
     {'description': 'gem', 'weight': 51, 'value': 30},
     {'description': 'scroll', 'weight': 28, 'value': 46},
     {'description': 'amulet', 'weight': 74, 'value': 20},
     {'description': 'spellbook', 'weight': 73, 'value': 7},
     {'description': 'potion', 'weight': 19, 'value': 93},
     {'description': 'amulet', 'weight': 71, 'value': 91},
     {'description': 'amulet', 'weight': 57, 'value': 71},
     {'description': 'gold', 'weight': 7, 'value': 6},
     {'description': 'potion', 'weight': 43, 'value': 71},
     {'description': 'potion', 'weight': 23, 'value': 78},
     {'description': 'gold', 'weight': 25, 'value': 83}]



### Knapsack


```python
CAPACITY = 200 # max weight the knapsack can hold
```


```python
class Knapsack:
    def __init__(self, item_list, mask=None):
        if mask == None:
            mask = [False]*NUM_ITEMS # new knapsacks start out empty
        self.mask = mask
        self.items = [item for (item, selected) in zip(item_list, mask) if selected]
        self.weight = sum([item['weight'] for item in self.items])
        self.value = sum([item['value'] for item in self.items])
        self.valid = self.weight <= CAPACITY

    def __repr__(self):
        mask_string = ''.join([str(int(flag)) for flag in self.mask])
        return f'<knapsack mask:{mask_string} weight:{self.weight} value:{self.value}>'
    
    def print_contents(self):
        print(self)
        for item in self.items:
            print(f"  {item['description']} weight:{item['weight']} value:{item['value']}")
```

### Genetic Algorithm


```python
# genetic algorithm parameters
POPULATION_SIZE = 100 # number of individuals in population
MUTATION_RATE = 0.20 # probability that an individual mutates
SURVIVAL_RATE = 0.50 # percentage of generation that survives to have children
NUM_GENERATIONS = 100 # number of generations to simulate
```


```python
def fitness(knapsack): # survival of the fittest
    if knapsack.weight > CAPACITY:
        return -1 # illegal knapsacks have negative fitness
    else:
        return knapsack.value
```


```python
def mutate(knapsack, item_list):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, NUM_ITEMS-1) # randomly select one gene
        new_mask = knapsack.mask
        new_mask[i] = not new_mask[i] # "Mutation: it is the key to our evolution." -Professor X
        knapsack = Knapsack(item_list, new_mask)
    return knapsack
```


```python
def crossover(knapsack1, knapsack2, item_list): # combine DNA of parents to make child
    child_mask = [random.choice(gene) for gene in zip(knapsack1.mask, knapsack2.mask)]
    return Knapsack(item_list, child_mask)
```


```python
def select(population): #  this is where we simulate natural selection
    num_survivors = round(POPULATION_SIZE * SURVIVAL_RATE)
    population = sorted(population, key=fitness, reverse=True)[:num_survivors]
    return population
```


```python
def repopulate(population):
    while len(population) < POPULATION_SIZE:
        parents = random.sample(population, 2)
        child = crossover(parents[0], parents[1], treasure)
        population.append(child)
        return population
```

### Simulation


```python
population = [Knapsack(treasure) for _ in range(0, POPULATION_SIZE)]
```


```python
for _ in range(1, NUM_GENERATIONS):
    population = [mutate(k, treasure) for k in population]
    population = select(population)
    population = repopulate(population)
```


```python
# all valid individuals in final generation, sorted by fitness
population = sorted([k for k in population if k.valid], key=fitness, reverse=True)
population
```




    [<knapsack mask:10000110001000010001 weight:200 value:462>,
     <knapsack mask:11000101100000000100 weight:176 value:379>,
     <knapsack mask:00000000011001001011 weight:153 value:336>,
     <knapsack mask:00000000000001100110 weight:156 value:333>,
     <knapsack mask:11000100000000001010 weight:117 value:323>,
     <knapsack mask:01000010010000000100 weight:185 value:274>,
     <knapsack mask:00000000010001000110 weight:136 value:272>,
     <knapsack mask:01000000000100000100 weight:161 value:166>,
     <knapsack mask:00000000011000001010 weight:109 value:160>,
     <knapsack mask:10000000100000000000 weight:33 value:96>]




```python
# details of best solution
population[0].print_contents()
```

    <knapsack mask:10000110001000010001 weight:200 value:462>
      scroll weight:17 value:89
      ring weight:26 value:75
      potion weight:47 value:98
      scroll weight:28 value:46
      amulet weight:57 value:71
      gold weight:25 value:83


### Links

* [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
* [Genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
* [Solving the Knapsack Problem with a Simple Genetic Algorithm](https://www.dataminingapps.com/2017/03/solving-the-knapsack-problem-with-a-simple-genetic-algorithm/)
* [Genetic algorithms 1. A simple genetic algorithm](https://pythonhealthcare.org/2018/10/01/94-genetic-algorithms-a-simple-genetic-algorithm/)
* [Introduction to Optimization with Genetic Algorithm](https://www.linkedin.com/pulse/introduction-optimization-genetic-algorithm-ahmed-gad/)
