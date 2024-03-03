import math
import random

def polarToRect(lat, lon):
    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    return (x, y, z)

coords = []

def pickLocationProjectionMethod():
    #Credits to Brian M. Scott for this smart idea
    #https://math.stackexchange.com/a/1586015/1226290

    floats = [random.random(), random.random()]
    z = float(floats[0]) * 2 - 1
    lon = float(floats[1]) * math.pi * 2 - math.pi
    r = math.sqrt(1 - math.pow(z, 2))
    x = math.cos(lon) * r
    y = math.sin(lon) * r

    coords.append((x, y, z))

def pickLocation():
    floats = [random.random(), random.random()]
    x = float(floats[0]) * 2 * math.pi - math.pi
    y = float(floats[1]) * 2 - 1
    lon = x
    lat = math.pi / 2 - math.acos(y)
    coords.append(polarToRect(lat, lon))

import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, color='b', alpha=0.2)

for _ in range(100):
    pickLocationProjectionMethod()

for coord in coords:
    ax.scatter(coord[0], coord[1], coord[2], color='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()