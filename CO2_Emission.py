import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv('data.csv')




plt.figure(figsize=(12, 6))
sns.scatterplot(x='Weight', y='CO2', data=data)
plt.title('CO2 Emission')



plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.regplot(x='Weight', y='CO2', data=data, ci=None, scatter_kws={"s": 100})
plt.title('Regression Line for CO2')
plt.show()

