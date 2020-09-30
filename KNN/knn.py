# K-Nearest Neighbors (K-NN)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

import os
import time
start_time = time.time()


# Path to the dataset file
DATASHEET_PATH = os.path.join("..", "Data", "DataSheet.csv")

# Importing the dataset
dataset = pd.read_csv(DATASHEET_PATH)
X = dataset.iloc[:, 1:10].values
y = dataset.iloc[:, 10].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting K-NN to the Training set
classifier = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Accuracy
acc = classifier.score(X_test, y_test)
print("\nAccuracy = ", acc*100,"%")


# Predicting the Test set results
knnPickle = open('knnpickle_file', 'wb')

pickle.dump(classifier, knnPickle)

# Loading the model
loaded_model = pickle.load(open('knnpickle_file', 'rb'))
result = loaded_model.predict(X_test)

# Displaying the predicted and actual values 
print("\n0 = star , 1 = galaxy")
for x in range(len(result)):
    print("Predicted: ", result[x], " Data: ", X_test[x], " Actual: ", y_test[x])

# Making the Confusion Matrix
cm = confusion_matrix(y_test, result)
print("\n The Confusion Matrix:")
print(cm)

'''
# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN (Training set)')
plt.xlabel('DistictNumpyArray')
plt.ylabel('Star or Galaxy')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN (Test set)')
plt.xlabel('DistictNumpyArray')
plt.ylabel('Star or Galaxy')
plt.legend()
plt.show()'''

print("--- %s seconds ---" % (time.time() - start_time))
