from scipy import io
import numpy as np

array = np.array([1, 2, 3, 4, 7, 9])


# The savemat() function allows us to export data in Matlab format.
# Export the following array as variable name "vec" to a mat file:
io.savemat('array.mat', {'vec': a})


# The loadmat() function allows us to import data from a Matlab file.
# Import the array from following mat file.:
mydata = io.loadmat('array.mat')

print(mydata)


# Use the variable name "vec" to display only the array from the matlab data:

print(mydata['vec'])
