import matplotlib.pylab as plt
from sklearn import linear_model

reg=linear_model.LinearRegression()

X=[[30],[35],[20],[15],[3]]
y=[90,95,70,40,10]

reg.fit(X,y)

print(reg.predict([[10]]))

plt.scatter(X,y,color='black')

y_pred=reg.predict(X)
print(reg.coef_)
print(reg.intercept_)
plt.plot(X,y_pred,color='blue',linewidth=3)

plt.show()
