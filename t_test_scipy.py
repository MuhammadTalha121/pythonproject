import numpy as np
from scipy.stats import ttest_ind

value_1 = np.random.normal(size=1000)
value_2 = np.random.normal(size=1000)

res = ttest_ind(value_1, value_2)

print(res)