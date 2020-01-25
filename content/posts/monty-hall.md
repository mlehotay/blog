Title: Probability Simulation in Python
Date: 2019-12-09 08:04
Slug: monty-hall

## Probability Simulation in Python

I've never really liked with the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem). The soution is counterintuative and my brain kind of breaks when I try to wrap my head around the conditional probabilities. In situations like this it can be beneficial to look at the problem empirically and estimate the probabilities of the outcomes in the event space in code. So, let's play the game ourselves and see what happens!

We start by creating a model of the game to simulate one iteration, or one time playing the game. I've included print statements to describe what happens are every step.


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

    Game begins. (The car is behind door 1).
    Player chooses door 3.
    Monty opens door 2 to reveal a goat.
    Player switches to door 1.
    Monty opens door 1 to reveal the car.
    Player wins!


At this point we have a working system that can play the game once. After testing it thoroughly to verify that it implements the behaviour described in the problem, let's turn it into a function so we can re-use it more easily.


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

We can call our function with a randomized strategy like this:


```python
monty_hall(random.choice([False, True]))
```

    Game begins. (The car is behind door 2).
    Player chooses door 2.
    Monty opens door 3 to reveal a goat.
    Player still chooses door 2.
    Monty opens door 2 to reveal the car.
    Player wins!


Now lets clean it up a bit and remove the print statements so it runs quietly.


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




    False



Now that we have create a model for the problem, we can estimate the probabilites with simulation. We run the model repeatedly and measure the frequency of each outcome over many iterations of the game. These frequencies represent our probabilites!

It looks like the probability of winning is about 0.5 when the player chooses to switch or stay with equal probability.


```python
N = 10000
results = []
for _ in range(N):
    results.append(monty_hall(random.choice([False, True])))
sum(results)/N
```




    0.4945



But when the player always sticks to their original guess, their win rate drops to about 0.33.


```python
results = []
for _ in range(N):
    results.append(monty_hall(False))
sum(results)/N
```




    0.3347



And if the player always changes their guess, their win rate increases to about 0.67.


```python
results = []
for _ in range(N):
    results.append(monty_hall(True))
sum(results)/N
```




    0.6625



We can change our loop to a list comprehension to make it python-y. (I'm hoping this will seem more readable to me after I get more practice with list comprehensions!)


```python
results = [monty_hall(True) for _ in range(N)]
sum(results)/N
```




    0.6674



And for conciseness, lets eliminate the results variable and run each simulation as a single expression.


```python
sum([monty_hall(True) for _ in range(N)])/N
```




    0.6638



Now with our model complete, we can easily simulate the Monty Hall problem with different parameters. Let's see what increasing the number of doors does:


```python
for doors in range(3, 10+1):
    for strategy in [False, True]:
        print(f'{doors}, {strategy}: {sum([monty_hall(strategy, doors) for _ in range(N)])/N}')
```

    3, False: 0.3334
    3, True: 0.6647
    4, False: 0.2464
    4, True: 0.3736
    5, False: 0.201
    5, True: 0.27
    6, False: 0.163
    6, True: 0.2104
    7, False: 0.1472
    7, True: 0.1691
    8, False: 0.1285
    8, True: 0.1499
    9, False: 0.1117
    9, True: 0.1266
    10, False: 0.0998
    10, True: 0.1105


Hmmm, it looks like no matter how many doors there are, it is always better to change your guess. See how easy it is to estimate this programatically!
