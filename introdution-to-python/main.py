import matplotlib.pyplot as pyplot
from sklearn import *
from numpy import *
from sklearn.model_selection import train_test_split

iris_dataset = datasets.load_iris()
iris_data: ndarray = iris_dataset.data
iris_target = iris_dataset.target

x = iris_data
y = iris_target

x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.25, random_state=33)


print(x_train.shape)
print("=======================================")
print(x_test.shape)
print("=======================================")
print(y_train.shape)
print("=======================================")
print(y_test.shape)

weights = 'uniform'
k_neighbors = 15

classifier = neighbors.KNeighborsClassifier(k_neighbors, weights=weights)
classifier.fit(x_train, y_train)

z = classifier.predict(x_train)
print(z.shape)

accuracy=classifier.score(x_train, y_train)
print("Accuracy model: " + str(accuracy))

sample = [[5,5,4,2]]
prediction = classifier.predict(sample)
print(prediction.shape)
print(prediction)
print("end")

k_range = range(1,26)
scores = []
for k in k_range:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_prediction = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_prediction))

pyplot.plot(k_range, scores)
pyplot.ylabel('some numbers')
pyplot.xlabel('Valeur de K pour KNN')
pyplot.ylabel('Testing  Accuracy')
pyplot.show()