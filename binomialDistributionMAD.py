import numpy as np
import math
from decimal import Decimal, getcontext

n = 10000
p = 0.1

samples = np.random.binomial(n, p, size=100000)

mean = np.mean(samples)
mad = np.mean(np.abs(samples - mean))

print("Approximated MAD:", mad)

def expectation_np_X(n, p):
    # thanks to this answer for the MAD formula: https://stats.stackexchange.com/a/147771/406639
    getcontext().prec = 50

    floor_np = int(n * p)
    expectation = Decimal(2) * (Decimal(1-p)**(n - floor_np)) * (Decimal(p)**(floor_np + 1)) * (Decimal(floor_np + 1)) * Decimal(math.comb(n, floor_np + 1))
    return expectation

result = expectation_np_X(n, p)
print("Exact MAD:", result)

