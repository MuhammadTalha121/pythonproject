import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()


df = pd.read_csv('data.csv')


X = df[['Weight', 'Volume', ]]
y = df['CO2']

scalex = scale.fit_transform(X)


regr = linear_model.LinearRegression()
regr.fit(scalex, y)

scaled = scale.transform([[20000, 13000]])
predictCO2 = regr.predict([scaled[0]])

print(predictCO2)