import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)

plt.subplot(2, 1, 1)
plt.scatter(x, y, c=colors, cmap='OrRd', alpha=0.6, s=sizes)
plt.title("2022_Growth")
plt.xlabel("Reach_AGING")
plt.ylabel("Growth_Population")
plt.colorbar()
plt.grid()



# plot2

x = np.random.randint(150, size=150)
y = np.random.randint(150, size=150)
colors = np.random.randint(150, size=150)
sizes = 10 * np.random.randint(150, size=150)
plt.title("2020_Growth")
plt.xlabel("Reach_AGING")
plt.ylabel("Growth_Population")
plt.subplot(2, 1, 2)

plt.scatter(x, y, c=colors, cmap='OrRd', alpha=0.6, s=sizes)
plt.suptitle("Diseases_Growth_per_year_2020-2022 ")
plt.colorbar()
plt.grid()
plt.show()