from scipy import io
import numpy as np

a = np.array([1, 2, 3, 4, 7, 9])

io.savemat('a.mat', {'vec': a})

mdata = io.loadmat('a.mat')

print(mdata)