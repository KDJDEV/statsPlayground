import random
import matplotlib.pyplot as plt
from scipy.stats import norm 
import numpy as np

low = 0
high = 100
sampleMeans = []

n = 100
for _ in range(10000):
    sample = [random.uniform(low, high) for _ in range(n)]
    sampleMeans.append(sum(sample)/n)

plt.hist(sampleMeans, bins=30, color='skyblue', edgecolor='black', density=True)
plt.xlabel("Mean")
plt.ylabel("Frequency")
xAxis = np.arange(low, high, 0.01)

theoreticalSampleMean = (low + high) / 2
print(theoreticalSampleMean)
theoreticalSD = (high - low) / np.sqrt(12)
theoreticalSampleSD = theoreticalSD / np.sqrt(n)
plt.xlim(theoreticalSampleMean - theoreticalSampleSD * 3, theoreticalSampleMean + theoreticalSampleSD * 3)
plt.plot(xAxis, norm.pdf(xAxis, theoreticalSampleMean, theoreticalSampleSD), color='red') 
plt.show()