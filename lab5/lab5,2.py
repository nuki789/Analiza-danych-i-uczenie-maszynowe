import matplotlib.pyplot as plt
import numpy as np

x = [i * 0.01 for i in range(0, 1000)]
y = [i * 0.01 for i in range(0, 1000)]
z = [[np.sin(x[i]) * np.cos(y[j]) for j in range(1000)] for i in range(1000)]

x, y = np.meshgrid(x, y, indexing='ij')
Z = np.array(z)
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot_surface(x, y, Z, cmap='viridis', linewidth=0)
plt.show()