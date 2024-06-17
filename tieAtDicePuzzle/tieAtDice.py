import numpy as np

def calculateProbabilityOfTie(n):
    arr = np.array([1] * 6)
    
    numerators = arr
    for _ in range(n - 1):
        numerators = np.convolve(numerators, arr)
          
    fractions = np.power((numerators / (6**n)), 2)
    result = np.sum(fractions)
    
    return result

nValuesToTest = list(range(1, 16))
for n in nValuesToTest:
    result = calculateProbabilityOfTie(n)
    print(f"For n = {n} dice, the probability of a tie is: {result}")
