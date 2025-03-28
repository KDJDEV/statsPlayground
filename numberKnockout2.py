from fractions import Fraction

# Equation: (1 + (1/4)^n)^a + (1/2)^(2n) = 22^b
# We will now allow a and b to be fractions.

def equation(a, b, n):
    lhs = (1 + (1/4)**n)**a + (1/2)**(2*n)
    rhs = 22**b
    return lhs == rhs

# Brute-force search for much larger ranges of a, b (fractions), and n
solutions = []
t = 30
# Try different values for a, b as fractions, and n as integers
for p in range(1, t):  # Numerator of a (larger range)
    for q in range(1, t):  # Denominator of a (larger range)
        for r in range(1, t):  # Numerator of b (larger range)
            for s in range(1, t):  # Denominator of b (larger range)
                a = Fraction(p, q)
                b = Fraction(r, s)
                for n in range(0, t):  # Try different values of n (larger range)
                    if equation(a, b, n):
                        solutions.append((a, b, n))

print(solutions)
