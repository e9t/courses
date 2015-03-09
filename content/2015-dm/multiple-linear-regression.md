Title: Multiple linear regression
Date: 2015-03-13 09:00
Courseid: 2015-dm
Toc: True
Math: True

#### 공지사항

1. Assignment 제출방식 변경: 2015-dm@googlegroups.com -> e-class
1. Assignment 개수 변경: 4 -> 3
1. Project proposal 제출: 다음주 수요일(3/18)까지 e-class로
1. Project team 구성: 다음주 수요일(3/18)까지 e-class로
1. 수업 시간 변경: 09:00 -> 09:30
    - 저는 9시까지 올 것이니 질문 있으신 분들은 미리 와주세요
    - 9시 반에 출석 부르고 바로 수업 시작할 것



## Data mining process
<img src="images/process.png" width="500px">

## 학습(learning)이란 무엇을 의미하는가?
<img src="images/partition.png" width="500px">

## 목적에 따른 분류: Descriptive modeling vs Predictive modeling
- Descriptive modeling 
    - Look back to the past
    - To extract compact and easily understood information from large, sometimes gigantic database.
    - OLAP (online analytical processing), SQL (structured query language)
- Predictive modeling
    - Predict the future
    - Identify strong links between variables of data.
    - To predict the unknown consequence (dependent variable) based on the information provided (independent variable)
    - $y = f(x_1, x_2, ..., x_n) + \epsilon$

## 학습데이터에 따른 분류: Supervised learning vs Unsupervised learning
- Supervised learning
    - Goal: predict a single "target" or "outcome" variable $y$
    - Finds relations between $X$ and $y$
    - Train (learn) data where target value is known.
    - Score data where target value is not known.
    - 입출력(input-output)의 쌍으로 구성된 training set으로부터 입력을 출력을 사상하는 함수를 학습하는 과정.
    - 즉, 입력벡터를 x, 그에 대응하는 출력벡터(i.e., label)를 y라고 할 때, training set은 D={(x,y)}로 주어지게 되며, 모델은 이 training set에 기반하여 관측하지 않은 새로운 데이터 x'가 들어왔을 때 그에 해당되는 label, y'을 추론하는 방법을 배우게 된다.
    - 교사학습은 주로 분류(classification)와 회귀분석(regression) 문제 해결에 적합하다.
- Unsupervised learning
    - Explores intrinsic characteristics.
    - Estimates underlying distribution.
    - Segment data into meaningful groups or detect patterns.
    - There is no target (outcome) variable to predict or classify.
    - 출력값 없이 오직 입력값만 주어지며, 이러한 입력값들의 공통적인 특성을 파악하여 학습하는 과정.
    - 즉, training set은 D={(x)}로 주어지게 된다.
    - 비교사학습은 주로 군집화(clustering), 밀도추정(density estimation), 차원축소(dimension reduction) 등에 사용된다.
- cf. semi-supervised learning

## Data mining techniques
<img src="http://image.slidesharecdn.com/20121102seminar-121102055512-phpapp01/95/introduction-to-data-mining-for-newbies-15-1024.jpg?cb=1351855294" width="500px">

## Simple linear regression

- $x$: 독립변수
- $y$: 종속변수
- $a, b$: 파라미터

$$y = ax + b$$

## Multiple linear regression (MLR)

- $X$: 독립변수들
- $y$: 종속변수
- $A, b$: 파라미터

$$y = AX + b$$

### MLR in Python

1. 데이터 import 하기
    - 먼저 파이썬에서 MLR을 시행하기 위해서 [scikit-learn](http://scikit-learn.org/) 패키지를 사용해보자.
    - 보통은 데이터를 어디선가 다운로드 받고, 정제한 후 읽어들어야겠지만, scikit-learn 패키지에 이미 몇 가지 데이터셋이 준비되어 있으니 그 중 한 가지인 diabetes(당뇨병) 데이터셋을 써보자.
    - 파이썬에서 패키지를 사용하기 위해서는 `import some_package`을 입력하면 되고, 하나의 큰 패키지에서 일부만을 사용할 때는 `from some_package import a_subpackage`를 입력하면 된다.
우리는 먼저 scikit-learn의 일부인 `dataset` subpackage 사용할 것이니 `from sklearn import datasets`를 하고, 데이터를 로딩해보자.

            :::python
            from sklearn import datasets
            d = datasets.load_diabetes()

    - 우리가 다른 곳에서 (ex: [UCI Datasets](http://archive.ics.uci.edu/ml/)) 데이터를 다운로드 받았다면 별도의 전처리 과정을 거쳐야했겠지만 친절하게도 scikit-learn은 데이터를 이미 전처리해서 data (X), target (y)로 나누어 놓았다. 이를 각각 `X`, `y`에 넣어보자.

            :::python
            print(d.keys())  # returns ['target', 'data']
            X = d['data']
            y = d['target']

    - 다른 작업을 진행하기 이전에 X, y 데이터에 대한 탐색을 해보자.

            :::python
            print(X.shape)      # returns (442, 10)

1. Simple linear regression
    - 먼저 하나의 변수를 정해 simple linear regression부터 해보자.

            :::python
            import numpy as np
            X2 = X[:, np.newaxis][:, :, 2]
    
    - 변수를 선택하고 나면 X2, y를 각각 training set, validation set으로 나눈다. 현재 데이터의 개수가 442개이므로 validation set을 약 10%인 40개로 해보자.

            :::python
            X2_train, X2_test = X2[:-40], X2[-40:]
            y_train, y_test = y[:-40], y[-40:]

    - Train

            :::python
            from sklearn.linear_model import LinearRegression
            slr = LinearRegression()
            slr.fit(X2_train, y_train)

            # The coefficients
            print('Coefficients: \n', slr.coef_)

            # mean square error
            print("RSS: %.2f" % np.mean((slr.predict(X2_test) - y_test) ** 2))

            # Explained variance score: 1 is perfect prediction
            print('Variance score: %.2f' % slr.score(X2_test, y_test))

    - Plot
            
            :::python
            import matplotlib.pyplot as plt
            plt.scatter(X2_test, y_test,  color='black')
            plt.plot(X2_test, slr.predict(X2_test), color='blue', linewidth=3)
            plt.xticks(())
            plt.yticks(())
            plt.show()

1. Multiple linear regression
    - Data partitioning

            :::python
            X_train, X_test = X[:-40], X[-40:]
            y_train, y_test = y[:-40], y[-40:]

    - Train

            :::python
            from sklearn.linear_model import LinearRegression
            mlr = LinearRegression()
            mlr.fit(X_train, y_train)

            # The coefficients
            print('Coefficients: \n', mlr.coef_)

            # mean square error
            print("RSS: %.2f" % np.mean((mlr.predict(X_test) - y_test) ** 2))

            # Explained variance score: 1 is perfect prediction
            print('Variance score: %.2f' % mlr.score(X_test, y_test))
