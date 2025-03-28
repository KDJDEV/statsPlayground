import numpy as np

pos = np.array((range(1,13)))
neg = np.array((range(1,13))) * -1

numbers = np.concatenate((pos, neg)).tolist()
print(numbers)

def convertToBalancedTernary(n):
    ternaryNum = []
    while n != 0:
        remainder = n % 3 - 3 * ((n % 3) // 2)
        quotient = (n+1) // 3
        ternaryNum = [remainder] + ternaryNum
        n = quotient
    return ternaryNum

ternaryNumbers = []
for n in numbers:
    ternaryNumbers.append(convertToBalancedTernary(n))
print(ternaryNumbers)

print(convertToBalancedTernary(5), convertToBalancedTernary(6), convertToBalancedTernary(7))