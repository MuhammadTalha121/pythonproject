import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('china-map.jpg'))
x = np.random.randint(200, 370, size=200)
y = np.random.randint(10, 240, size=200)
linex = np.array([200])
liney = np.array([1.7])
plt.imshow(img)
plt.scatter(x, y, c='red', cmap="viridis")
plt.plot(x, y)
plt.plot(linex, liney)
plt.colorbar()
plt.show()