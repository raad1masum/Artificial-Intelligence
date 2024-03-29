import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as pyplot
import pickle
import tensorflow
import keras
from sklearn import linear_model
from matplotlib import style
from sklearn.utils import shuffle

data = pd.read_csv("Data/student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# Train data
'''
best = 0
for _ in range(1000):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
'''

# Save data in .pickle file
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# Print aspects of linear regression
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

# Calculate predictions
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

# Create matplotlib plot of predictions
p = 'studytime'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()