#Estimates pi using Euler Product

import random
import math

lower_bound = 1
upper_bound = math.pow(10, 20)

n = int(math.pow(10, 6))
random_pairs = [(random.randint(lower_bound, upper_bound), random.randint(lower_bound, upper_bound)) for _ in range(n)]

def are_coprime(a, b):
    return math.gcd(a, b) == 1

# Filter coprime pairs
coprime_pairs = [(x, y) for x, y in random_pairs if are_coprime(x, y)]
a = len(coprime_pairs) / len(random_pairs)
pi = math.sqrt(6/a)
print(pi)

