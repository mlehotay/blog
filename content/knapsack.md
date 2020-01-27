Title: Knapsack Problem
Date: 2020-01-26 22:43
Modified: 2020-01-27 13:06
Category: Data Science
Tags: genetic
Slug: knapsack
Status: published

This is a draft version of the blog post. The final version should be up tonight. -ML


```python
import random
import arena # https://github.com/mlehotay/arena.git
```


```python
NUM_ITEMS = 5
MAX_WEIGHT = 100
MAX_VALUE = 100

CAPACITY = 250

POPULATION_SIZE = 10
MUTATION_RATE = 0.20
```


```python
class Knapsack:
    def __init__(self, item_list, mask=None):
        if mask == None:
            mask = [False]*NUM_ITEMS     
        self.mask = mask
        self.items = [item for (item, selected) in zip(item_list, mask) if selected]
        self.weight = sum([item['weight'] for item in self.items])
        self.value = sum([item['value'] for item in self.items])

    def __repr__(self):
        return f'Knapsack({self.mask}, weight:{self.weight}, value:{self.value})'
```


```python
def mutate(knapsack, item_list):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, NUM_ITEMS-1)
        new_mask = knapsack.mask
        new_mask[i] = not new_mask[i]    
        knapsack = Knapsack(item_list, new_mask)
    return knapsack
```


```python
def crossover(knapsack1, knapsack2):
    pass
```


```python
treasure = [{
    'weight': random.randint(1, MAX_WEIGHT),
    'value': random.randint(1, MAX_VALUE)
    } for _ in range(0, NUM_ITEMS)
]
treasure
```




    [{'weight': 2, 'value': 91},
     {'weight': 83, 'value': 11},
     {'weight': 79, 'value': 71},
     {'weight': 90, 'value': 87},
     {'weight': 63, 'value': 78}]




```python
population = [Knapsack(treasure) for _ in range(0, POPULATION_SIZE)]
```


```python
population
```




    [Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0),
     Knapsack([False, False, False, False, False], weight:0, value:0)]




```python
def selection(survival_size, weight):
    pass
```


```python

```
