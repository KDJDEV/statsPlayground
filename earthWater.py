import math
from global_land_mask import globe

numSamples = 5000

def rad2deg(rad):
    return rad * (180 / math.pi)

coords = []
isOnLand = []

with open("data/10000RandomNumbers.txt", "r") as file: #data is from https://www.random.org/decimal-fractions/?num=10000&dec=10&col=1&format=plain&rnd=new
    text = file.read()
    randomNumbers = text.split("\n")
    for i in range(numSamples):
        x = float(randomNumbers[i * 2]) * 2 * math.pi - math.pi
        y = float(randomNumbers[i * 2 + 1]) * 2 - 1
        lon = rad2deg(x)
        latrad = math.pi / 2 - math.acos(y)
        lat = rad2deg(latrad)
        coords.append((lat, lon))
        isOnLand.append(globe.is_land(lat, lon))

print("Proportion that are in water: " + str(1 - isOnLand.count(True)/numSamples))
        

