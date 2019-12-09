Title: Probability Simulation in Python
Date: 2019-12-09 08:04
Slug: probability-simulation

## Probability Simulation in Python

This is the code. Still need to write text.

### Monty Hall

https://en.wikipedia.org/wiki/Monty_Hall_problem


```python
import random
```


```python
# game setup
NUM_DOORS = 3
assert NUM_DOORS > 2, 'not enough doors'
random.seed()
winning_door = random.randint(1, NUM_DOORS) # randomly select the winning door
print(f'Game begins. (The car is behind door {winning_door}).')

# player chooses one of the doors
player_door = random.randint(1, NUM_DOORS)
print(f'Player chooses door {player_door}.')

# Monty opens a different door to reveal a goat
while(True):
    goat_door = random.randint(1, NUM_DOORS)
    if(goat_door != winning_door and goat_door != player_door):
        break
print(f'Monty opens door {goat_door} to reveal a goat.')

# player chooses another door, if they want to
switch = random.choice([False, True])
if(switch):
    while(True):
        new_door = random.randint(1, NUM_DOORS)
        if(new_door != player_door and new_door != goat_door):
            break
    player_door = new_door
    print(f'Player switches to door {player_door}.')
else:
    print(f'Player still chooses door {player_door}.')

# determine the outcome
print(f'Monty opens door {winning_door} to reveal the car.')
if player_door == winning_door:
    print('Player wins!')
else:
    print('Player loses.')
```

    Game begins. (The car is behind door 3).
    Player chooses door 3.
    Monty opens door 2 to reveal a goat.
    Player still chooses door 3.
    Monty opens door 3 to reveal the car.
    Player wins!



```python
def monty_hall(switch, n=NUM_DOORS):
    assert n > 2, 'not enough doors'

    # game setup
    winning_door = random.randint(1, n) # randomly select the winning door
    print(f'Game begins. (The car is behind door {winning_door}).')

    # player chooses one of the doors
    player_door = random.randint(1, n)
    print(f'Player chooses door {player_door}.')

    # Monty opens a different door to reveal a goat
    while(True):
        goat_door = random.randint(1, n)
        if(goat_door != winning_door and goat_door != player_door):
            break
    print(f'Monty opens door {goat_door} to reveal a goat.')

    # player chooses another door, if they want to
    if(switch):
        while(True):
            new_door = random.randint(1, n)
            if(new_door != player_door and new_door != goat_door):
                break
        player_door = new_door
        print(f'Player switches to door {player_door}.')
    else:
        print(f'Player still chooses door {player_door}.')

    # determine the outcome
    print(f'Monty opens door {winning_door} to reveal the car.')
    if player_door == winning_door:
        print('Player wins!')
    else:
        print('Player loses.')
```


```python
monty_hall(random.choice([False, True]))
```

    Game begins. (The car is behind door 1).
    Player chooses door 3.
    Monty opens door 2 to reveal a goat.
    Player still chooses door 3.
    Monty opens door 1 to reveal the car.
    Player loses.



```python
def monty_hall(switch, n=NUM_DOORS):
    assert n > 2, 'not enough doors'
    winning_door = random.randint(1, n) # randomly select the winning door

    # player chooses one of the doors
    player_door = random.randint(1, n)

    # Monty opens a different door to reveal a goat
    while(True):
        goat_door = random.randint(1, n)
        if(goat_door != winning_door and goat_door != player_door):
            break

    # player chooses another door, if they want to
    if(switch):
        while(True):
            new_door = random.randint(1, n)
            if(new_door != player_door and new_door != goat_door):
                break
        player_door = new_door

    # determine the outcome
    return (player_door == winning_door)
```


```python
monty_hall(random.choice([False, True]))
```




    True




```python
N = 10000
results = []
for _ in range(N):
    results.append(monty_hall(random.choice([False, True])))
sum(results)/N
```




    0.5008




```python
results = []
for _ in range(N):
    results.append(monty_hall(False))
sum(results)/N
```




    0.3362




```python
results = []
for _ in range(N):
    results.append(monty_hall(True))
sum(results)/N
```




    0.6713




```python
results = [monty_hall(True) for _ in range(N)]
sum(results)/N
```




    0.6703




```python
sum([monty_hall(True) for _ in range(N)])/N
```




    0.6672




```python
for doors in range(3, 10+1):
    for strategy in [False, True]:
        print(f'{doors}, {strategy}: {sum([monty_hall(strategy, doors) for _ in range(N)])/N}')
```

    3, False: 0.3347
    3, True: 0.669
    4, False: 0.2522
    4, True: 0.3763
    5, False: 0.2046
    5, True: 0.2619
    6, False: 0.1746
    6, True: 0.2126
    7, False: 0.1453
    7, True: 0.1731
    8, False: 0.1259
    8, True: 0.1445
    9, False: 0.1097
    9, True: 0.1255
    10, False: 0.0928
    10, True: 0.1124



```python
# pelican cheat sheet

# rm -rf output; mkdir output
# pelican -s pelicanconf.py -o output -t theme content
# cd output; python -m http.server
# ghp-import -m "xyzzy" -b gh-pages output
# git push origin gh-pages
```
