"""
This script answers the below question using Markov Chains.

"There is a set of n cards that come in randomized packs of 1. What is the expected number of packs you would have to open before you have the entire set?"

It essentially works by finding the state vectors after drawing certain numbers of packs and then computing the expected value by summing up the probabilities associated with the desired state (getting all of the cards).
"""

import numpy as np

n = 20 # number of cards to collect
packs = 1000 # number of packs to simulate up to (more packs gives better approximations of expectedValue)

matrix = np.zeros((n+1, n+1))
for i in range(n):
    p = (n - i) / n
    matrix[i][i] = 1 - p
    matrix[i][i + 1] = p
matrix[n][n] = 1

def getStateVector():
    stateVector = np.zeros((1, n + 1))
    stateVector[0][0] = 1
    return stateVector

stateVector = getStateVector()

expectedValue = 0
lastHaveAllNCardsProbability = 0
for i in range(1, packs + 1):
    stateVector = stateVector @ matrix
    haveAllNCardsProbability = stateVector[0][n]

    probabilityThatWeGotAllNCardsWhenOpeningThisPack = (haveAllNCardsProbability - lastHaveAllNCardsProbability) # the probability that we got the final card when opening the ith pack is the difference between the probability having all n cards at the ith pack minus the probability of having all cards at the (i - 1)th pack
    expectedValue += probabilityThatWeGotAllNCardsWhenOpeningThisPack * i
    lastHaveAllNCardsProbability = haveAllNCardsProbability

print("Expected value: " + str(expectedValue))

def nthHarmonic(n):
    if n == 1:
        return 1
    else:
        return nthHarmonic(n-1) + 1/n

trueExpectedValue = nthHarmonic(n) * n
print("Error: " + str(trueExpectedValue - expectedValue))


"""
EXTRA FUNCTION TO GRAPH PROBABILITY DISTRIBUTION OVER TIME FOR K PACKS
"""
import gif
@gif.frame
def plotProbabilities(packs):
    import matplotlib.pyplot as plt
    from numpy.linalg import matrix_power
    stateVector = getStateVector()
    data = (stateVector @ (matrix_power(matrix, packs))).flatten()
    plt.bar(range(len(data)), data)
    plt.xlabel('Number of Cards Collected')
    plt.ylabel('Probability')
    plt.title('Probability Distribution for ' + str(packs) + ' packs')
    plt.ylim(0, 1)

def createGif():
    frames = [plotProbabilities(i) for i in range(100)]
    gif.save(frames, 'images/cardPuzzle.gif', duration=150)

createGif()




