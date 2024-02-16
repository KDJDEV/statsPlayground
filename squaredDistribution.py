import numpy as np
import matplotlib.pyplot as plt

def pdf(x):
    return 1/(20 * np.sqrt(x))
def cdf(x):
    return np.sqrt(x)/10
def invCdf(x):
    return (10 * x) ** 2

num_samples = 10000

samples = []
while len(samples) < num_samples:
    y = np.random.rand()
    x = invCdf(y)
    samples.append(x)

samples2 = []
while len(samples2) < num_samples:
    x = (np.random.rand() * 10) ** 2
    samples2.append(x)

plt.hist(samples, bins=100, density=True, alpha=0.5, color='g') #this is the plot based on sampling from the theoretical distribution
plt.hist(samples2, bins=100, density=True, alpha=0.5, color='r') #this is the plot based on sampling from the uniform distribution and squaring the result

x_values = np.linspace(0, 100, 100)
plt.plot(x_values, pdf(x_values), 'r--', label='True PDF')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Random Samples from a PDF over a Range')
plt.legend()
plt.show()
