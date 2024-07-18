Title: RPG Combat Simulator
Date: 2020-01-24 09:41
Modified: 2020-01-27 19:56
Category: Games
Tags: simulation, probability, object-oriented-programming
Slug: arena
Status: published
Comments: true


I have been thinking about combat in RPG games lately and wondering if I could come up with a way to model combat that I could use for machine learning. I'd like to be able to make decisions about the best weapon to wield and the best armor to wear, and to be able to predict the odds of surviving a particular battle. The obvious approach is to simulate the battle many times and use statistics!

Our combat system will be pretty basic. For simplicity it will only use melee weapons and not have any missile weapons or magic. Other than that it will work like many tabletop role-playing games: fighters take turns attacking each other and the outcome of each attack is randomly determined by rolling dice. A regular set of dice contains dice with 4, 6, 8, 10, 12, and 20 sides.

Combatants have three variables that describe their toughness and their state of health:

  * **Level** is a measure of a fighter's skill and experience.
  * **Health** or (**hit points**) is the amount of injury the fighter can withstand.
  * **Armor class** describes how easy or difficult it is to hit a fighter. The lower their AC, the harder they are to hit.

To attack, roll a 20-sided die to see if you hit your opponent. You need to roll a certain number or higher to hit. The formula is `22 - level - armor_class`. For example, to hit an opponent with armor class 10, a level 1 fighter needs to roll an 11 or higher (22 - 1 - 10 = 11).

If you hit, then roll to see how much damage you do. The number of dice and what kind of dice is determined by the weapon you are wielding.

Let's start by implementing rolls of the dice. We'll use this function any time we need to generate a random number.


```python
import random

def roll(dice, sides):
    total = 0
    for _ in range(0, dice):
        total += random.randint(1, sides)
    return total
```

And now we define the weapons and armor as dictionaries.

The amount of damage a weapon can do is represented as a tuple with three elements: the number of dice, the number of sides per die, and an addend. For example, a flail does 2-7 points of damage by rolling a 6-sided die and adding 1 (1d6+1).


```python
weapon_list = {
    None: (1,2,0),  # 1d2
    'axe': (1,6,0), # 1d6
    'battle axe': (1,8,0), # 1d8
    'club': (1,6,0),
    'dagger': (1,4,0),
    'flail': (1,6,1), # 1d6+1
    'hammer': (1,4,1),
    'mace': (1,6,1),
    'morning star': (2,4,0), # 2d4
    'scimitar': (1,8,0),
    'spear': (1,6,0),
    'quarterstaff': (1,6,0),
    'broad sword': (2,4,0),
    'long sword': (1,8,0),
    'short sword': (1,6,0),
    'trident': (1,6,1),
    'two-handed sword': (1,10,0)
}
```

The value for a type of armor is the amount of protection it provides. The values correspond to the difference in the die roll needed to hit an opponent. So if you need to roll a 13 to hit an enemy wearing ring mail, you'd need to roll a 15 to hit an opponent in chain mail.


```python
armor_list = {
    None: 0,
    'shield': 1,
    'padded armor': 2,
    'leather armor': 2,
    'studded leather': 3,
    'ring mail': 3,
    'scale mail': 4,
    'chain mail': 5,
    'splint mail': 6,
    'banded mail': 6,
    'plate mail': 7
}
```

## Fighter

Here is the `Fighter` class to represent a combatant.

The constructor takes the `name`, `level`, `faction`, `weapon`, and `armor` for the fighter. `Name` is the fighter's name (e.g., Frodo) and `faction` is the name of the "side" they are on. Fighters from the same faction will not attack each other. Values for `faction` could be 'good' and 'evil' or anything else you want. The `battle` member variable will be assigned a value when the fighter enters the arena. For now, set it to None.


```python
class Fighter:
    def __init__(self, name, level, faction, weapon, armor):
        self.name = name
        self.level = level
        self.max_health = sum(roll(1,10) for _ in range(0,level))
        self.health = self.max_health
        self.faction = faction
        self.weapon = weapon
        self.armor = armor
        self.armor_class = 10 - armor_list[self.armor]
        self.battle = None

    def __repr__(self):
        return f'{self.name} ({self.health}/{self.max_health}) \
            [Level {self.level} {self.__class__.__name__}, {self.weapon}, {self.armor}, {self.faction}]'
```

On each turn the fighter will make a list all the opponents in the battle (anybody not in their faction), and then randomly select one to attack.


```python
    def take_turn(self):
        opponents = [f for f in self.battle.fighters if f.faction!=self.faction]
        if(opponents != []):
            target = random.choice(opponents)
            self.attack(target)
```

The attack hits its target if the fighter rolls a high enough number. That number is `22 - level - armor_class`.

If the attack hits then roll again to calculate the amount of damage and call the target's `take_damage` method.


```python
    def attack(self, opponent):
        if (roll(1,20) >= (22 - self.level - opponent.armor_class)):
            (dice, sides, plus) = weapon_list[self.weapon]
            damage = roll(dice, sides) + plus
            opponent.take_damage(damage, self)
        elif(self.battle.verbose):
            print(f'  {self.name} swings at {opponent.name} and misses')
```

Note here that when the target object's `take_damage` method is called, the program flow transfers from the attacker to the opponent. Now `self` no longer refers to the attacking fighter and instead it refers to the target.

When a fighter's health is reduced to zero they die.


```python
    def take_damage(self, damage, attacker):
        if self.battle.verbose:
            print(f'  {attacker.name} attacks {self.name} for {damage} damage')
        self.health -= damage
        if(self.health < 1):
            self.die()

    def die(self):
        if self.battle.verbose:
            print(f'  {self.name} dies!')
        self.battle.fighters.remove(self)
        self.battle = None
```

## Battle

Here we have a class to represent a battle between two or more fighters. The battle has a `title`, a list of `fighters`, a `turn` counter, and a `winner`. The constructor gets called with a list of `roles` that describe how each fighter object should be instantiated, and a boolean verbosity flag. When `verbose` is set to true then the play-by-play action of the battle is printed.

A `Fighter` object is created for each `role` passed to the `Battle` constructor. The fighters are then added to the battle by calling its `add_fighter` method.

The `roles` parameter is a list of dictionaries with the following keys (and example values):
```
{
  'name':    'Boromir',
  'faction': 'Gondor',
  'level':    9,
  'class':    Fighter,
  'weapon':  'long sword',
  'armor':   'chain mail'
}
```


```python
class Battle:
    def __init__(self, title, roles, verbose):
        self.title = title
        self.verbose = verbose
        self.fighters = []
        self.winner = None
        self.turn = 0
        for role in roles:
            fighter = role['class'](role['name'], role['level'], role['faction'], role['weapon'], role['armor'])
            self.add_fighter(fighter)

    def __repr__(self):
        return f'{self.title} turn {self.turn}'

    def add_fighter(self, fighter):
        self.fighters.append(fighter)
        fighter.battle = self
```

The battle proceeds in rounds. During a round each fighter is given their turn to attack. The battle ends when all the surviving fighters are from the same faction.


```python
    def fight_battle(self):
        if self.verbose:
            print(f'{self.title} fighters:')
            for fighter in self.fighters:
                print(fighter)
        while self.winner == None:
            self.play_round()
        if self.verbose:
            print(f'{self.winner} wins {self.title}!')
        return self.winner

    def play_round(self):
        self.turn += 1
        if self.verbose:
            print(f'{self}:')
        for f in self.fighters:
            f.take_turn()
        if len({f.faction for f in self.fighters}) == 1:
            self.winner = self.fighters[0].faction
```

We've got enough code written now to simulate a full battle. Let's give it a go.


```python
roles = [
    {'name': 'Bob', 'faction': 'Green Banner', 'level': 2,
     'class':Fighter, 'weapon':'scimitar', 'armor':'chain mail'},
    {'name': 'Alice', 'faction': 'Mithril Order', 'level': 1,
     'class':Fighter, 'weapon':'short sword', 'armor':'leather armor'},
    {'name': 'Eve', 'faction': 'Mithril Order', 'level': 1,
     'class':Fighter, 'weapon':'flail', 'armor':'shield'}
]

Battle('Test Battle', roles, True).fight_battle()
```

    Test Battle fighters:
    Bob (11/11) [Level 2 Fighter, scimitar, chain mail, Green Banner]
    Alice (8/8) [Level 1 Fighter, short sword, leather armor, Mithril Order]
    Eve (9/9) [Level 1 Fighter, flail, shield, Mithril Order]
    Test Battle turn 1:
      Bob swings at Alice and misses
      Alice swings at Bob and misses
      Eve attacks Bob for 6 damage
    Test Battle turn 2:
      Bob swings at Eve and misses
      Alice swings at Bob and misses
      Eve attacks Bob for 5 damage
      Bob dies!
    Mithril Order wins Test Battle!





    'Mithril Order'



## Arena

Now we need to repeat many `iterations` of the battle so that we can estimate each faction's probability of winning. 1000 times should be plenty.

We create a set of `factions` by adding the faction of each `role`. Using a set ensures that we only count each faction once. Then we start fighting battles and counting `wins`.

The `print_probabilities` method prints the probability of each faction winning based on their observed win frequencies.


```python
class Arena:
    def __init__(self, roles, iterations=1000, verbose=False):
        self.roles = roles
        self.iterations = iterations
        self.verbose = verbose
        self.factions = {role['faction'] for role in roles}
        self.wins = {faction:0 for faction in self.factions}
        self.winner = None

    def simulate_battle(self):
        for i in range(0, self.iterations):
            winner = Battle(f'Battle {i+1}', self.roles, self.verbose).fight_battle()
            self.wins[winner] += 1

    def print_probabilities(self):
        print('Estimated Probabilities of Victory:')
        for faction in sorted(self.factions):
            print(f'{faction}: {self.wins[faction]/self.iterations}')
```

That's it! We are done! Let's see how it works with more than one iteration.


```python
arena = Arena(roles, iterations=2, verbose=True)
arena.simulate_battle()
arena.print_probabilities()
```

    Battle 1 fighters:
    Bob (11/11) [Level 2 Fighter, scimitar, chain mail, Green Banner]
    Alice (10/10) [Level 1 Fighter, short sword, leather armor, Mithril Order]
    Eve (1/1) [Level 1 Fighter, flail, shield, Mithril Order]
    Battle 1 turn 1:
      Bob attacks Eve for 6 damage
      Eve dies!
      Alice swings at Bob and misses
    Battle 1 turn 2:
      Bob attacks Alice for 8 damage
      Alice swings at Bob and misses
    Battle 1 turn 3:
      Bob swings at Alice and misses
      Alice swings at Bob and misses
    Battle 1 turn 4:
      Bob attacks Alice for 1 damage
      Alice swings at Bob and misses
    Battle 1 turn 5:
      Bob swings at Alice and misses
      Alice swings at Bob and misses
    Battle 1 turn 6:
      Bob swings at Alice and misses
      Alice swings at Bob and misses
    Battle 1 turn 7:
      Bob attacks Alice for 7 damage
      Alice dies!
    Green Banner wins Battle 1!
    Battle 2 fighters:
    Bob (6/6) [Level 2 Fighter, scimitar, chain mail, Green Banner]
    Alice (6/6) [Level 1 Fighter, short sword, leather armor, Mithril Order]
    Eve (2/2) [Level 1 Fighter, flail, shield, Mithril Order]
    Battle 2 turn 1:
      Bob swings at Alice and misses
      Alice swings at Bob and misses
      Eve swings at Bob and misses
    Battle 2 turn 2:
      Bob attacks Alice for 2 damage
      Alice attacks Bob for 6 damage
      Bob dies!
    Mithril Order wins Battle 2!
    Estimated Probabilities of Victory:
    Green Banner: 0.5
    Mithril Order: 0.5


That works pretty well. I am happy with that! Let's do it again with 1000 iterations.


```python
arena = Arena(roles)
arena.simulate_battle()
arena.print_probabilities()
```

    Estimated Probabilities of Victory:
    Green Banner: 0.606
    Mithril Order: 0.394


It looks like the Green Banner has the edge in this battle. They are predicted to win about 60% of the time.


```python
arena = Arena(roles)
arena.simulate_battle()
arena.print_probabilities()
```

    Estimated Probabilities of Victory:
    Green Banner: 0.617
    Mithril Order: 0.383


And the predictions are pretty repeatable. Awesome! I wonder what happens if we give one of the Mithril Order fighters some better equipment.


```python
roles[2] = {'name': 'Eve', 'faction': 'Mithril Order', 'level': 1,
            'class':Fighter, 'weapon':'broad sword', 'armor':'splint mail'}

arena = Arena(roles)
arena.simulate_battle()
arena.print_probabilities()
```

    Estimated Probabilities of Victory:
    Green Banner: 0.423
    Mithril Order: 0.577


Way to go Mithril Order!

I put the code for this blog post on GitHub: [https://github.com/mlehotay/arena](https://github.com/mlehotay/arena)
