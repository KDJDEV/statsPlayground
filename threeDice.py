import itertools

# Number of dice
numDice = 3

# Number of sides on each die
numSides = 6

# Generate all possible combinations using itertools.product
allPerms = list(itertools.product(range(1, numSides + 1), repeat=numDice))

# Print all combinations
numPassCondition = 0
for perm in allPerms:
    #print(perm)
    count = 0
    for num in perm:
        if num>4:
            count += 1
    if count >= 2:
        numPassCondition += 1

from fractions import Fraction
print(Fraction(numPassCondition, 216))

