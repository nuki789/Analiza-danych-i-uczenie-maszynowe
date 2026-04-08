import matplotlib.pyplot as plt
import numpy as np

x = [np.random.randint(0, 100) for i in range(0, 100)]
y = [np.random.randint(0, 100) for i in range(0, 100)]

plt.scatter(x, y)
plt.show()
