import numpy as np

u1 = 1

u2 = 3.5

u3 = 9

totalError = 0
steinTotalError = 0

n = 1000000
for i in range(n):
    """
    x1 = np.random.normal(loc=u1, scale=1.0, size=None)
    x2 = np.random.normal(loc=u2, scale=1.0, size=None)
    x3 = np.random.normal(loc=u3, scale=1.0, size=None)
    """
    x1 = np.random.uniform(low=u1-5, high=u1+5, size=None)
    x2 = np.random.uniform(low=u2-5, high=u2+5, size=None)
    x3 = np.random.uniform(low=u3-5, high=u3+5, size=None)

    ols = np.square(x1 - u1) + np.square(x2 - u2) + np.square(x2 - u2)
    totalError += ols

    jamesStein = 1 - 1/((np.square(x1)) + np.square(x2) + np.square(x3))

    x1 *= jamesStein
    x2 *= jamesStein
    x3 *= jamesStein

    ols = np.square(x1 - u1) + np.square(x2 - u2) + np.square(x2 - u2)
    steinTotalError += ols

print(totalError/n)
print(steinTotalError/n)

