Title: k-NN
Date: 2015-03-09 21:55
Status: draft

## k-NN

- k-NN?
- k-Nearest Neighbors?
- k개의 가까운 이웃?
- 아이디어: 내 주변의 이웃 k개를 봐서 내가 어떤 값을 가질지 투표하자!

[<img src="images/knn.png" width="300px">](http://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/KnnClassification.svg/440px-KnnClassification.svg.png)

### Calculating similarities

k-NN에서 가장 중요한 문제: 두 점 사이의 거리가 가까운지 먼지 어떻게 판단할 것인가? (distance를 정의하는 문제)

### Multiclass classification

What if there are not just two classes, but $k$ classes?
1. One-vs-all
2. One-vs-one
    - $k (k − 1) / 2$ binary classifiers for a K-way multiclass problem

### One class classification

TBD

## [Programming] k-NN with Scikit-learn

코드 출처: http://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#example-neighbors-plot-classification-py

1. 데이터 입력하기

        from sklearn import datasets
        d = datasets.load_iris()
        X = d.data[:, :2]   # take the first two features
        y = d.target

2. 파라미터 설정하기

        k = 15
        weights = 'uniform'     # uniform, distance 중 택일
        algorihtm = 'auto'      # ball_tree, kd_tree, brute 중 택일

3. Train

        from sklearn import neighbors
        knn = neighbors.KNeighborsClassifier(k, weights, algorithm)
        knn.fit(X, y)

4. Plot

        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
        cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
        cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

        h = .02 # step size in the mesh

        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.show()

## [Programming] Handling real datasets

다시 한 번 얘기하지만, 실제 데이터는 이렇게 구조화되어 있지 않다. 보통은 우리가 데이터를 구하고, 전처리해서 지금 로딩하는 데이터의 형태, 또는 우리가 데이터 마이닝 알고리즘을 편하게 돌릴 수 있는 형태로 만들어야 할 것이다.
(그리고 보통 실제 데이터는 아주아주아주 지저분하기 때문에 그렇게 데이터를 전처리하는 시간이 전체 데이터마이닝 프로세스의 절반 이상을 차지하기도 한다.)

- 예시: [관악구 신림동 지역의 부동산 가격](http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=&hscpTypeCd=&cortarNo=1162010200&mapLevel=10) 예측하기
- [들어가기 전 몇 가지 꿀팁](../tips/terminal.html)

### Data exploration

{% csv '''
공급면적($m^2$),전용면적($m^2$),층수,전체층수,매물가(만원)
113,84,20,20,13000
116,84,11,16,38800
81,59,17,20,31500
113,84,14,20,38500
''' %}


