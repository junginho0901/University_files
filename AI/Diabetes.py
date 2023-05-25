import matplotlib.pylab as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model

# 당뇨병 데이터 세트 적재
diabetes_X , diabetes_y = datasets.load_diabetes(return_X_y=True)

# BMI 만 추려내서 2차원 배열로 만듬, BMI 특징의 인덱스 = 2
diabetes_X_new = diabetes_X[:,np.newaxis,2] 

# 학습 데이터와 테스트 데이터를 분리
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(diabetes_X_new,diabetes_y,test_size=0.1,random_state=0)

# 선형 회귀 모델로 학습
regr = linear_model.LinearRegression()
regr.fit(X_train,y_train)

# 테스트 데이터 예측
y_prediction = regr.predict(X_test)

# 결과 그래프로 그리기
plt.scatter(X_test,y_test,color='black')
plt.plot(X_test,y_prediction,color='blue',linewidth=3)
plt.show()
