import matplotlib.pylab as plt
from sklearn import linear_model

reg=linear_model.LinearRegression()

X=[[1930],[1940],[1950],[1965],[1972],[1982],[1992],[2010],[2016]]
y=[59,62,70,69,71,74,75,76,78]

reg.fit(X,y)

print(reg.predict([[10]]))

plt.scatter(X,y,color='black')

y_pred=reg.predict(X)
print(reg.coef_)
print(reg.intercept_)
plt.plot(X,y_pred,color='blue',linewidth=3)

plt.show()
