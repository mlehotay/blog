Title: Probability Simulation in Python
Date: 2019-12-09 06:50
Slug: probability-simulation

# Probability Simulation in Python

Intro. Model probability problems with random variables and frequency. Simulate the problem by running the model many times.

### Monty Hall

description of problem. pictures of goats.
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

    Game begins. (The car is behind door 2).
    Player chooses door 1.
    Monty opens door 3 to reveal a goat.
    Player switches to door 2.
    Monty opens door 2 to reveal the car.
    Player wins!


summary of how this model represents the problem


```python
# run the simulation many times
```

explain results of the simulation, discuss how frequency represents probability


```python
# show some graphs
```

conclusion


```python
# pelican cheat sheet

# rm -rf output; mkdir output
# pelican -s pelicanconf.py -o output -t theme content
# cd output; python -m http.server
# ghp-import -m "xyzzy" -b gh-pages output
# git push origin gh-pages
```
