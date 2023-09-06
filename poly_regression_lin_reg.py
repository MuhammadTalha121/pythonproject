import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sklearn

x = np.random.randint(80, size=100)
y = np.random.randint(100, size=100)

slope, intercept, r, p, std_err = stats.linregress(x, y)


def my_func(x):
    return slope * x + intercept


model = list(map(my_func, x))
plt.subplot(2, 1, 1)
plt.scatter(x, y)
plt.plot(x, model)
plt.grid()


x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)


my_model = np.poly1d(np.polyfit(x, y, 10))

my_line = np.linspace(1, 100, 100)

speed = my_model(20)
plt.subplot(2, 1, 2)
plt.scatter(x, y)
plt.plot(my_line, my_model(my_line), speed)






plt.show()
