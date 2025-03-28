from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 100  # Set this to a high enough value for the required precision

numberOfRounds = 100
populationSize = Decimal('1' * numberOfRounds)
print("Population size:", populationSize)
probabilityThatEveryoneIsKilled = Decimal(1) / Decimal(36)

def probabilityThatYouGetPutInRoundN(n):
    peopleInRound = Decimal(10) ** (n - 1)
    peopleRemainingInPopulation = populationSize - numberWithNOnes(n - 1)
    if peopleRemainingInPopulation < peopleInRound:
        return False
    return (Decimal(1) - probabilityThatEveryoneIsKilled) ** (n - 1) * peopleInRound / peopleRemainingInPopulation

def probabilityThatYouGetPutInSomeRound():
    sum = Decimal(0)
    n = 1
    while True:
        result = probabilityThatYouGetPutInRoundN(n)
        if result == False:
            break
        sum += result
        n += 1
    return sum

def probabilityThatYouWillDieInRoundN(n):
    return probabilityThatYouGetPutInRoundN(n) * probabilityThatEveryoneIsKilled

def probabilityOfDeath():
    sum = Decimal(0)
    n = 1
    while True:
        result = probabilityThatYouWillDieInRoundN(n)
        if result == False:
            break
        sum += result
        n += 1
    return sum

def probabilityThatIfYouDieYouWillDieInTheLastRound():
    return probabilityThatYouWillDieInRoundN(len(str(populationSize))) / probabilityOfDeath()

def numberWithNOnes(n):
    if n == 0:
        return Decimal(0)
    onesStr = '1' * n
    onesNumber = Decimal(onesStr)
    return onesNumber

print("Probability of death:", probabilityOfDeath())
print("Probability that if you do die it will be in the last round:", probabilityThatIfYouDieYouWillDieInTheLastRound())
print("Probability that you are put in some round rather than being excluded from the game:", probabilityThatYouGetPutInSomeRound())
for i in range(1, numberOfRounds + 1):
    roundProbability = probabilityThatYouGetPutInRoundN(i) / probabilityThatYouGetPutInSomeRound()
    print(f"Probability that given that you are in a round that you are in round {i}: {roundProbability}")
print("Probability that if you get chosen it will be the death round:")