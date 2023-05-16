import matplotlib.pylab as plt
from sklearn import linear_model

reg=linear_model.LinearRegression()

X=[[2015],[2016],[2017],[2018],[2019]]
y=[12,19,28,37,46]

reg.fit(X,y)

print(reg.predict([[10]]))

plt.scatter(X,y,color='black')

y_pred=reg.predict(X)
print(reg.coef_)
print(reg.intercept_)
plt.plot(X,y_pred,color='blue',linewidth=3)

plt.show()
